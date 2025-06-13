import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

def interpret_goal(goal_text: str) -> str:
    prompt = f'Design an in silico molecular assay for: {goal_text}.'
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[{'role': 'user', 'content': prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content
