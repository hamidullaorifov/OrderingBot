from pydantic import BaseModel


class FormData(BaseModel):
    full_name: str
    phone_number: str
    comment: str
