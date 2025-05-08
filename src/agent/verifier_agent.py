from anthropic import Anthropic

class VerifierAgent:
    def __init__(self, api_key):
        self.client = Anthropic(api_key=api_key)

    def verify_synthesis(self, synthesized_text):
        try:
            response = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": f"Please verify the following synthesized text for accuracy and completeness: {synthesized_text}"
                    }
                ]
            )
            return response.content
        except Exception as e:
            print(f"Error during Claude API call: {e}")
            return None

