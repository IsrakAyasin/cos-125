import openai
openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model = 'gpt-3.5-turbo',
  messages = [
    {'role': 'user', 'content': 'Hello!'}
  ],
  temperature = 0  
)

print(completion['choices'][0]['message']['content'])