from groq import Groq
import os
from dotenv import load_dotenv

# load environment
load_dotenv()

#fetch the key
GROQ_KEY = os.getenv("GROQ_API_KEY")

# Initialize client

groq_client = Groq(api_key=GROQ_KEY)

def llm_call(msg):
    response = groq_client.chat.completions.create(
              model = "llama3-70b-8192",
              messages = [{"role":"user","content":msg}]

    )
    return response.choices[0].message.content


#### Hi What happen