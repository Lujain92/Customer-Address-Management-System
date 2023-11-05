from pydantic import BaseModel, EmailStr
from uuid import UUID

class AddressBase(BaseModel):
    """
    Base model for address data input.
    """
    phone: str
    email: EmailStr
    country: str
    city: str
    street: str

class Address(AddressBase):
    """
    Address model including ID.
    """
    id: UUID

