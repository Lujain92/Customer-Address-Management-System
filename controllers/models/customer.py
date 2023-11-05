from enum import Enum
from pydantic import BaseModel
from uuid import UUID

class Gender(str, Enum):
    male = 'male'
    female = 'female'

class CustomerBase(BaseModel):
    """
    Base model for customer data input.
    """
    first_name: str
    last_name: str
    age: int
    gender: Gender
    address_id: UUID

class Customer(CustomerBase):
    """
    Customer model including ID.
    """
    id: UUID
    adult: bool

