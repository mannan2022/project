import openai

openai.api_key = "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"
prompt=input('Enter Your Command ')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)