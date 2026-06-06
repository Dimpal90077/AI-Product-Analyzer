from dotenv import load_dotenv
import os

print(load_dotenv())
print(os.getenv("MISTRAL_API_KEY"))