from pydantic import BaseModel


class FormData(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    comment: str
