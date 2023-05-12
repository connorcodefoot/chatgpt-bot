import os
import openai
from dotenv.main import load_dotenv
load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']

while True:
  question = input("\033[31m What is your question?\033[0m\n")

  if question == "exit":
    print("\033[31m Goodbye \033[0m\n")
    break

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role": "system",
      "content": "You are an assistant, answer the given question"
    }, {
      "role": "user",
      "content": question
    }])

  print("\033[32m" + completion.choices[0].message.content + "\n")