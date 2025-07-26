from app.models import Conversation,Message
import json

print("--Tesing Model Creation --")

try:
    user_message=Message(sender="user", text="Hello, how are you?")
    ai_message=Message(sender="ai", text="I'm fine, thank you!")
    new_conversation=Conversation(
        user_id="test_user123",
        message=[user_message, ai_message]
    )
    print("Models created successfully:")
    print(new_conversation.model_dump_json(indent=2))
except Exception as e:
    print(f"Error creating conversation: {e}")    