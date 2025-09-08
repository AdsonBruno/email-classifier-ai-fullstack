from dataclasses import dataclass


@dataclass
class Email: 
  content: str
  classification: 'Classification' = None
  suggested_response: str = None
  