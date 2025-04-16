import numpy as np
from openai import OpenAI

def remove_code_block_markers(code_text):
    lines = code_text.strip().split('\n')
    if lines and lines[0].strip() == '```python':
        lines = lines[1:]  
    if lines and lines[-1].strip() == '```':
        lines = lines[:-1] 
    return '\n'.join(lines)

def get_rmp_update_code():
	f = open("rmp_prompt.txt", "r")
	rmp_prompt= f.read()
	client = OpenAI(api_key="sk-505a4ff57cfb432d8888a3d8d66a3133", base_url="https://api.deepseek.com")
	messages = [{"role": "user", "content": rmp_prompt}]
	response = client.chat.completions.create(
	    model="deepseek-chat",
	    messages=messages,
	    temperature=1.5,
	)
	messages.append(response.choices[0].message)
	text = messages[-1].content
	return remove_code_block_markers(text)

