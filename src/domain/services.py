from abc import ABC, abstractmethod
from .entities import Email

class IEmailAnalysisService(ABC):
    @abstractmethod
    def analyze(self, email: Email) -> dict:
        """"Analyze the email content to classify it and suggest a response."""
        pass