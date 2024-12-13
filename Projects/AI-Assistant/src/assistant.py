from transformers import pipeline

class AIAssistant:
    def __init__(self):
        # Load a Hugging Face model for text generation
        self.chatbot = pipeline("text-generation", model="gpt2")

    def get_response(self, user_input):
        try:
            response = self.chatbot(user_input, max_length=100, num_return_sequences=1)
            return response[0]["generated_text"]
        except Exception as e:
            return f"An error occurred: {str(e)}"
