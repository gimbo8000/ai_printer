from gpt4all import GPT4All
import torch
#i love imports
from printer import *
print("Is CUDA available:", torch.cuda.is_available())
print("Current device:", torch.cuda.current_device())
print("Device name:", torch.cuda.get_device_name(torch.cuda.current_device()))

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
def AI(prompt):
    with model.chat_session():
        responce = model.generate(prompt, max_tokens=1024)
        return responce