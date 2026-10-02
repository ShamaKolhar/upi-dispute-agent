import os
from dotenv import load_dotenv
from anthropic import Anthropic, AuthenticationError, APIConnectionError, RateLimitError

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

MODEL = "claude-haiku-4-5-20251001"


def ask_claude(prompt, max_tokens=200):
    """Send a prompt to Claude and return the reply text, or None if it fails."""
    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}],
        )
    except AuthenticationError:
        print("Error: your API key is wrong or missing. Check the .env file.")
        return None
    except APIConnectionError:
        print("Error: could not reach Claude. Check your internet connection.")
        return None
    except RateLimitError:
        print("Error: too many requests. Wait a moment and try again.")
        return None

    if response.stop_reason == "max_tokens":
        print("Warning: the reply was cut off. Try a higher max_tokens.")

    return response.content[0].text


if __name__ == "__main__":
    reply = ask_claude("My UPI payment failed but money was deducted. What should I do? Answer in 2 sentences.")
    print(reply)