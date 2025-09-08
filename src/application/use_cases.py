from src.domain.entities import Email
from src.domain.services import IEmailAnalysisService

class ClassifyEmailUseCase: 
  """
  Orchestrates the email classification and response generation process.
  """
  def __init__(self, email_analysis_service: IEmailAnalysisService): 
    self.email_analysis_service = email_analysis_service

  def execute(self, email_content: str) -> Email: 
    """
      Executes the use case to classify an email and suggest a response.
      
      Args:
        email_content: The raw text content of the email.
      
      Returns:
        An Email entity with the classification and suggested response.
    """
    email = Email(content=email_content)
    analyzed_email = self.email_analysis_service.analyze(email)

    return analyzed_email