# import openai

# openai.api_key = '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'
# prompt=input('Enter Your Command ')

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt=prompt,
#   temperature=0.7,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )

# text=response.get("choices")[0].get('text')
# print(text)