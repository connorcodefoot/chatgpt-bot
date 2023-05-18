import os
from langchain import OpenAI, ConversationChain
from dotenv.main import load_dotenv
load_dotenv()

OpenAI.api_key = os.environ['OPENAI_API_KEY']

llm = OpenAI(temperature=0)
conversation = ConversationChain(llm=llm, verbose=True)

x = 0
while x < 10: 
  output = conversation.predict(input=input())
  print(output)
  x += 1

