import os
import Config
from openai import OpenAI
import google.generativeai as genai

def _query_deepseek(api_key, messages):
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        stream=False
    )
    return response.choices[0].message.content

def _clean_ai_response(response_content):
    response_content = response_content.strip()
    if response_content.startswith('"') and response_content.endswith('"'):
        response_content = response_content[1:-1]
    if response_content.startswith("```") and response_content.endswith("```"):
        
        first_newline = response_content.find('\n')
        if first_newline != -1:
            response_content = response_content[first_newline + 1:-3]
        else:
            response_content = response_content[3:-3]
    elif response_content.startswith("```"):
        first_newline = response_content.find('\n')
        if first_newline != -1:
            response_content = response_content[first_newline + 1:]
        else:
            response_content = response_content[3:]
    elif response_content.endswith("```"):
        response_content = response_content[:-3]
    
    response_content = response_content.replace('\\"', '"')
    return response_content.strip()

def _query_gemini(api_key, messages):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    system_prompt = ""
    history = []

    for msg in messages:
        if msg['role'] == 'system':
            system_prompt += msg['content'] + "\n"
        elif msg['role'] in ['user', 'assistant']:
            role = 'model' if msg['role'] == 'assistant' else 'user'
            history.append({'role': role, 'parts': [msg['content']]})
            
    if not history or history[-1]['role'] != 'user':
        return "Error: Last message in history is not from the user."

    final_prompt = history.pop()

    final_prompt['parts'][0] = system_prompt + final_prompt['parts'][0]

    chat = model.start_chat(history=history)
    response = chat.send_message(final_prompt['parts'])
    return response.text

def _query_chatgpt(api_key, messages):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
    )
    return response.choices[0].message.content

def get_ai_response(messages):
    config = Config.load_config()
    ai_service = config.get("ai_service")
    api_key = config.get("api_key")

    if not ai_service or not api_key:
        return "AI service is not configured. Please run init.py."

    if ai_service == "DeepSeek":
        raw_response = _query_deepseek(api_key, messages)
    elif ai_service == "Gemini":
        raw_response = _query_gemini(api_key, messages)
    elif ai_service == "ChatGPT":
        raw_response = _query_chatgpt(api_key, messages)
    else:
        return f"Unknown AI service: {ai_service}"
    
    return _clean_ai_response(raw_response)

def validate_api_key(ai_service, api_key):
    print(f"Testing {ai_service} API Key...")
    try:
        test_messages = [{"role": "user", "content": "Hello"}]
        if ai_service == "DeepSeek":
            _query_deepseek(api_key, test_messages)
        elif ai_service == "Gemini":
            _query_gemini(api_key, test_messages)
        elif ai_service == "ChatGPT":
            _query_chatgpt(api_key, test_messages)
        else:
            return False
        return True
    except ImportError as e:
        print(f"\n[Error] Library not found. Please install the required package for {ai_service}.")
        print(f"Details: {e}")
        return False
    except Exception as e:
        print(f"\n[Validation Failed] An error occurred: {e}")
        return False
