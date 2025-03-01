from typing import List, Optional
from sqlalchemy.orm import Session

from app.db.repositories.chatbot_repository import ChatbotRepository
from app.services.nlp_service import NLPService
from app.services.survey_service import SurveyService
from app.services.response_service import ResponseService
from app.schemas.chatbot import (
    ChatbotRequest,
    ChatbotResponse,
    ConversationCreate,
    ConversationResponse
)


class ChatbotService:
    def __init__(self, db: Session):
        self.repository = ChatbotRepository(db)
        self.nlp_service = NLPService()
        self.survey_service = SurveyService(db)
        self.response_service = ResponseService(db)

    def create_conversation(
        self, conversation_in: ConversationCreate, user_id: int
    ) -> ConversationResponse:
        """Create a new chatbot conversation"""
        return self.repository.create_conversation(conversation_in, user_id)

    def process_message(self, message: ChatbotRequest, user_id: int) -> ChatbotResponse:
        """Process an incoming message from a user"""
        # Get the current conversation context
        conversation = self.repository.get_conversation(
            message.conversation_id)
        if not conversation:
            raise ValueError("Conversation not found")

        # Save the user message to the conversation history
        self.repository.add_message(
            conversation_id=message.conversation_id,
            content=message.message,
            is_user=True
        )

        # Process the message with NLP service
        intent, entities = self.nlp_service.analyze_message(message.message)

        # Generate response based on intent and entities
        response_text = self.generate_response(
            intent=intent,
            entities=entities,
            conversation_id=message.conversation_id,
            survey_id=conversation.survey_id,
            user_id=user_id
        )

        # Save the bot response to conversation history
        self.repository.add_message(
            conversation_id=message.conversation_id,
            content=response_text,
            is_user=False
        )

        return ChatbotResponse(
            message=response_text,
            conversation_id=message.conversation_id
        )

    def generate_response(
        self,
        intent: str,
        entities: dict,
        conversation_id: int,
        survey_id: int,
        user_id: int
    ) -> str:
        """Generate a response based on user intent and entities"""
        # This is a simplified example - in a real implementation,
        # this would contain more complex logic based on conversation state

        if intent == "greeting":
            return "Hi there! I'm here to help you take a survey. Let's get started!"

        elif intent == "answer_question":
            # Extract question ID and answer from entities
            question_id = entities.get("question_id")
            answer = entities.get("answer")

            if question_id and answer:
                # Save the response
                response_data = {
                    "survey_id": survey_id,
                    "question_id": question_id,
                    "answer": answer
                }
                self.response_service.create_response(response_data, user_id)

                # Get the next question
                # This is simplified - you would need logic to determine the next question
                return "Thanks for your answer! Next question..."

            return "I didn't quite understand your answer. Could you please rephrase?"

        elif intent == "help":
            return "I'm a survey chatbot. I'll ask you questions and record your responses."

        elif intent == "exit":
            return "Thank you for completing the survey! Have a great day."

        else:
            return "I'm not sure how to respond to that. Could you please rephrase or ask for help?"
