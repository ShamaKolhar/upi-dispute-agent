import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Call 1: get a reply from Claude
response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=100,
    messages=[{"role": "user", "content": "Say hello in one sentence."}],
)
print(response.content[0].text)
print("Stop reason:", response.stop_reason)
print("Tokens used:", response.usage)

# Call 2: count tokens only (no reply is generated)
complaint = "My UPI payment failed but money was deducted"
count = client.messages.count_tokens(
    model="claude-haiku-4-5-20251001",
    messages=[{"role": "user", "content": complaint}],
)
print("Words:", len(complaint.split()))
print("Tokens:", count.input_tokens)