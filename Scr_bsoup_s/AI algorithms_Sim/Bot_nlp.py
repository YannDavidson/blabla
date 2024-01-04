from transformers import pipeline, Conversation

# --- 1. Setup ---
# Initialize a conversational pipeline using a pre-trained model
chatbot = pipeline("conversational")

# --- 2. Integration ---
def chat_with_bot(input_text):
    # Create a conversation object
    conversation = Conversation(input_text)
    
    # Let the model generate a response
    result = chatbot(conversation)
    return result.generated_responses[-1]

# --- 3. User Interaction ---
# Simulating a conversation with the chatbot
messages = ["Hello!", "What can you do?", "Tell me a joke!"]

for msg in messages:
    bot_response = chat_with_bot(msg)
    print(f"User: {msg}")
    print(f"Bot: {bot_response}\n")
