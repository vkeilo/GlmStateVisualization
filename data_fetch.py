from config_parse import VisualConfig
from Taotie.agent_use import ChatAgent
from visual_logger import logger
import json
from random import randint

visualconfig = VisualConfig("./visual_config.json")
class TaskDataGenerator():
    def __init__(self, visualconfig, task_pattern, local_model = "chatglm3-6b"):
        self.task_pattern = task_pattern
        self.model_name = local_model
        self.config = visualconfig
        self.task_prompts = None
        self.agent = ChatAgent(self.model_name)
        logger.info('using local model: {self.model_name}')
        self.init_task_prompts()

    def start_fetch(self, start_index, end_index):
        for i in range(5):
            tmp_task_prompt = self.get_random_task_prompt()
            self.agent.init_messages_by_sentence(tmp_task_prompt)
            self.agent.prompt_add(tmp_task_prompt)
            logger.info(f'Current task prompt: \t{tmp_task_prompt}')
            result = self.agent.prompt_post()
            logger.info(f'task return: \t{result}')
            self.task_result_record(tmp_task_prompt, result)

    def load_prompts(self):
        pass

    def init_task_prompts(self):
        with open(self.config.role_setting_prompt_json, 'r', encoding='utf-8') as f:
            role_setting_prompts = json.load(f)
        self.task_prompts = role_setting_prompts[self.task_pattern]
        logger.info(f"successfully load {str(len(self.task_prompts))} task_prompts of task: {self.task_pattern}")
    
    # 从预设的同一任务的多种任务描述中选取一种作为当前的prompt
    def get_random_task_prompt(self):
        return self.task_prompts[randint(0, len(self.task_prompts) - 1)]

    def task_result_record(self, task_prompt, result):
        pass


test_TaskDataGenerator = TaskDataGenerator(visualconfig, task_pattern="translator")
test_TaskDataGenerator.start_fetch(0, 10)
