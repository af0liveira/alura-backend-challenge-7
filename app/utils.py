"""Utility functions for the application."""

import os
import sys
import openai

openai.api_key = str(os.getenv('OPENAI_API_KEY'))

def ask_chatGPT(message):
    """Make a single request to ChatGPT.
    
    The message content is send to ChatGPT and the response message is returned
    at the end of the transaction.
    If an error is raised on the ChatGPT's end, a blank response is returned."""

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
        )
    except openai.APIError as err:
        print(f"OpenAI API returned an API error: {err}", file=sys.stderr)
        print(f"A blank response will be returned.")
        return ""
    else:
        return completion.choices[0].message.content.strip()
