from enum import Enum
from pydantic import BaseModel

class Gender(str, Enum):
    male = "male"
    female = "female"

class CustomerBase(BaseModel):
    """
    Base model for customer data input.
    """
    first_name: str
    last_name: str
    age: int
    gender: Gender
    adult: bool
    address_id: int

class Customer(CustomerBase):
    """
    Customer model including ID.
    """
    id: int
