from config_parse import VisualConfig
from Taotie.agent_use import ChatAgent
from visual_logger import logger
import json
from random import randint
import os

visualconfig = VisualConfig("./visual_config.json")
class TaskDataGenerator():
    def __init__(self, visualconfig, task_pattern, local_model = "chatglm3-6b"):
        self.task_pattern = task_pattern
        self.model_name = local_model
        self.config = visualconfig
        self.task_prompts = None
        self.text_prompts = None
        self.ori_hidden_state_path = self.config.ori_hidden_state_path
        self.target_hidden_state_path = os.path.join(os.path.abspath(self.config.save_dir_path), self.task_pattern)
        self.processing_text_index = 0
        self.agent = ChatAgent(self.model_name)
        logger.info('using local model: {self.model_name}')
        self.init_prompts()
        if not os.path.exists(self.target_hidden_state_path):
            os.mkdir(self.target_hidden_state_path)

    def start_fetch(self, start_index, end_index):
        for i in range(start_index, end_index):
            self.processing_text_index = i
            self.fetch_one_date()

    def fetch_one_date(self):
        self.check_ori_hidden_state_path_empty()
        # 先随机取一个任务描述作为当前agent的行为准则
        tmp_task_prompt = self.get_random_task_prompt()
        self.agent.init_messages_by_sentence(tmp_task_prompt)
        # 第一次的初步post
        self.agent.prompt_add(tmp_task_prompt)
        logger.info(f'Current task prompt: \t{tmp_task_prompt}')
        init_result = self.agent.prompt_post()
        logger.info(f'task return: \t{init_result}')
        # 然后是后续的自由发挥

        # 然后是第二次的自由发挥
        for text in self.text_prompts[self.processing_text_index]:
            self.agent.prompt_add(text)
            logger.info(f'Next try: \t{text}')
            second_result = self.agent.prompt_post()
            logger.info(f'gpt return: \t{second_result}')
        # 整理结果，保存记录
        self.task_result_record()
        self.hidden_state_move()

    def check_ori_hidden_state_path_empty(self):
        # 检查self.ori_hidden_state_path文件夹中是否为空
        return not os.listdir(self.ori_hidden_state_path)

    def hidden_state_move(self):
        # 将参数文件移入具体的index对应文件夹中
        tmp_full_target_path = os.path.join(self.target_hidden_state_path, f'{str(self.processing_text_index)}')
        if not os.path.exists(tmp_full_target_path):
            os.makedirs(tmp_full_target_path)
        for file in os.listdir(self.ori_hidden_state_path):
            os.rename(os.path.join(self.ori_hidden_state_path, file), os.path.join(tmp_full_target_path, file))


    def get_random_task_prompt(self):
        return self.task_prompts[self.processing_text_index]

    def task_result_record(self):
        tmp_target_path = os.path.join(self.target_hidden_state_path, str(self.processing_text_index))
        if not os.path.exists(tmp_target_path):
            os.makedirs(tmp_target_path)
        with open(os.path.join(tmp_target_path, 'dialogue.txt'), 'w', encoding='utf-8') as f:
            json.dump(self.agent.messages, f,ensure_ascii=False)

    def init_prompts(self):
        with open(self.config.role_setting_prompt_json, 'r', encoding='utf-8') as f:
            role_setting_prompts = json.load(f)
        self.task_prompts = role_setting_prompts[self.task_pattern]
        logger.info(f"successfully load {str(len(self.task_prompts))} task_prompts of task: {self.task_pattern}")
        self.text_prompts = []
        with open(self.config.text_prompt_data_path[self.task_pattern], 'r', encoding='utf-8') as f:
            for line in f:
                self.text_prompts.append(line.split('\t'))
        logger.info(f"successfully load {str(len(self.text_prompts))} text_prompts of task: {self.task_pattern}")
    
    # 从预设的同一任务的多种任务描述中选取一种作为当前的prompt
    def get_random_task_prompt(self):
        return self.task_prompts[randint(0, len(self.task_prompts) - 1)]





test_TaskDataGenerator = TaskDataGenerator(visualconfig, task_pattern="translator")
test_TaskDataGenerator.start_fetch(0, 2)
