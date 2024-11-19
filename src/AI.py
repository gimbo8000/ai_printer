

from gpt4all import GPT4All

# Load the model in CPU-only mode
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf", device="cpu")

def AI(prompt):
    with model.chat_session():
        response = model.generate(prompt, max_tokens=1024)
        return response
