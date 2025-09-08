from dataclasses import dataclasses

@dataclasses
class Email: 
  content: str
  classification: 'Classification' = None
  suggested_classification: str = None
  