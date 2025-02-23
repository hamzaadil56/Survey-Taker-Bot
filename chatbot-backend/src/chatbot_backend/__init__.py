"""
Chatbot Backend Application

This package contains the backend implementation of the AI chatbot application.
"""

__version__ = "0.1.0"
__author__ = "Your Name"

from .core.config import load_config
from .services.ai_service import AIService
from .services.chat_service import ChatService

# Initialize core services
config = load_config()


def main() -> None:
    print("Hello from chatbot-backend!")
