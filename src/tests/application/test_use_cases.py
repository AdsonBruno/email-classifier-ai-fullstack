from unittest.mock import MagicMock 
import pytest

from src.application.use_cases import ClassifyEmailUseCase
from src.domain.entities import Email
from src.domain.value_objects import Classification

def test_classify_email_use_case_execution(): 
  mock_service = MagicMock()

  mock_service.analyze.return_value = Email(
    content = "Request to update the customer database",
    classification = Classification.PRODUCTIVE,
    suggested_response = "I'm on it."
  )

  use_case = ClassifyEmailUseCase(email_analysis_service=mock_service)
  result_email = use_case.execute(email_content="Request to update the customer database.")

  assert isinstance(result_email, Email)
  assert result_email.classification == Classification.PRODUCTIVE
  assert result_email.suggested_response == "I'm on it."

  mock_service.analyze.assert_called_once()
  called_with_email = mock_service.analyze.call_args[0][0]
  assert called_with_email.content == "Request to update the customer database."
  assert called_with_email.classification is None