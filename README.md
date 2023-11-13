# GlmStateVisualization
A object to visualize hidden state of chatglm3 model.

# Preparing
1. Make sure your [chatglm3-6b](https://github.com/THUDM/ChatGLM3) model is correctly prepared.
2. Copy file `THUDM\chatglm3-6b\config.json` and `THUDM\chatglm3-6b\modeling_chatglm_hid_save.py` to your chatglm3 model path (which seems like `E:\github_project\ChatGLM3\THUDM\chatglm3-6b`), this will cause two original files to be overwritten.


# data preparing
| task | nums | 
| :----: | :----: |
| translator | 1000 |
| summarizer | 1000 |
| first word selector | 1000 |
| word num counter | 1000 |