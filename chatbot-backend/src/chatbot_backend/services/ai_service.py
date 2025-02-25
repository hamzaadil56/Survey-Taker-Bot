from langchain.chat_models import ChatOpenAI
from langchain.memory import MongoDBChatMessageHistory
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from datetime import datetime
from models.chat import ChatMessage, ChatSession
from repositories.chat_repository import ChatRepository


class AIChatService:
    def __init__(self, openai_api_key: str, chat_repository: ChatRepository):
        self.llm = ChatOpenAI(
            temperature=0.7,
            openai_api_key=openai_api_key,
            model_name="gpt-3.5-turbo"
        )
        self.chat_repository = chat_repository

    async def process_message(self, session_id: str, user_input: str) -> ChatMessage:
        try:
            # Create conversation chain
            conversation = self.create_chat_session(session_id)

            # Get AI response
            response = conversation.predict(input=user_input)

            # Save user message
            user_message = ChatMessage(
                session_id=session_id,
                message=user_input,
                role="user",
                timestamp=datetime.utcnow()
            )
            await self.chat_repository.save_message(user_message)

            # Save AI response
            ai_message = ChatMessage(
                session_id=session_id,
                message=response,
                role="assistant",
                timestamp=datetime.utcnow()
            )
            await self.chat_repository.save_message(ai_message)

            return ai_message

        except Exception as e:
            # Log error and raise custom exception
            raise ChatProcessingError(f"Error processing chat: {str(e)}")
