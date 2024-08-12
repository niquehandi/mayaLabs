import openai

# Set your OpenAI API key
openai.api_key = 'API_KEY'  # Replace with your actual API key

def generate_text(prompt, max_tokens=100):
    """Generates text using OpenAI's GPT-3.5-turbo."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"An error occurred while generating text: {e}")
        return "Thank you for your comment!"

if __name__ == "__main__":
    # Example usage
    prompt = "PROMPT" # write the prompt that you want to use
    print(generate_text(prompt, max_tokens=50))
