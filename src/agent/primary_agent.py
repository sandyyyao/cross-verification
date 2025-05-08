from openai import OpenAI

class PrimaryAgent:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error in generating response: {e}")
            return "Error generating response."

if __name__ == '__main__':
    # Example usage (requires API key to be set as an environment variable or directly passed)
    # For testing, you might need to set API key in your environment or replace 'YOUR_API_KEY'
    # with your actual key if you don't use environment variables for API keys.
    # IMPORTANT: Never hardcode API keys in production code.
    # This is for demonstration purposes only.
    # agent = PrimaryAgent(api_key='YOUR_API_KEY')
    # response = agent.generate_response("What is the capital of France?")
    # print(response)
    pass

