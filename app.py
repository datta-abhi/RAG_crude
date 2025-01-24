# imports
import os
import glob
from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI

from prompt import *

# openai model selection
MODEL = 'gpt-4o-mini'

# load environ variables from env
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
openai = OpenAI()

# print(add_context("Who is Carllm"))

def chat(message,history):
    """
    generates a chat response using a conversational history and new user message;
    history is a list of tuples, each tuple in format (user_message,assistant_message)
    """
    messages = [{"role":"system",'content':system_message}]
    
    for user_message,assistant_message in history:
        messages.append({"role":"user","content":user_message})
        messages.append({"role":"assistant","content":assistant_message})
        
    message = add_context(message)
    messages.append({"role":"user","content":message})
    
    # generate stream chats, sends responses in chunks instead of single block of text
    stream = openai.chat.completions.create(model=MODEL, messages = messages, stream= True)
    
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        yield response
        
# gradio chat interface
view = gr.ChatInterface(chat).launch()