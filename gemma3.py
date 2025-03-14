from transformers import pipeline
import torch

pipe = pipeline("text-generation", model="google/gemma-3-1b-pt", device="cuda", torch_dtype=torch.bfloat16)
output = pipe("Eiffel tower is located in", max_new_tokens=50)
