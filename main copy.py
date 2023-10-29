from fastapi import APIRouter,FastAPI,HTTPException
from fastapi.encoders import jsonable_encoder
from enum import Enum
# from .routers import customer
from pydantic import BaseModel

app = FastAPI()

# app.include_router(customer.router)

class Gender(str, Enum):
    male = "male"
    female = "female"

class AddressBase(BaseModel):
    phone: str
    # email: EmailStr
    country: str
    city: str
    street: str

class Address(AddressBase):
    id: int


class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: Gender
    adult: bool
    address_id: int


class Customer(CustomerBase):
    id: int

fake_customer_db = [
   {"id": 0, "first_name": "Mohammad", "last_name": "Ahmad", "age": 25, "gender": Gender.male, "adult": True, "address_id": 2,},
   {"id": 1, "first_name": "Ali", "last_name": "Mousa", "age": 17, "gender": Gender.male, "adult": False, "address_id": 0,},
   {"id": 2, "first_name": "Fadwa", "last_name": "Kareem", "age": 22, "gender": Gender.female, "adult": True, "address_id": 3,},
   {"id": 3, "first_name": "Salwa", "last_name": "Belal", "age": 32, "gender": Gender.female, "adult": True, "address_id": 1,},
]


fake_address_db = [
   {"id": 0, "phone": "0700000000", "email": "0@gmail.com", "country": "Jordan", "city": "Amman", "street": "Maka Street",},
   {"id": 1, 	 "phone": "07111111111", "email": "1@gmail.com", "country": "Jordan", "city": "Zarqa", "street": "Sadaa Street",},
   {"id": 2, "phone": "0722222222", "email": "2@gmail.com", "country": "Jordan", "city": "Irbid", "street": "University Street",},
   {"id": 3, "phone": "0733333333", "email": "3@gmail.com", "country": "Jordan", "city": "Jarash", "street": "Jarash Street",}
]

customer_id_counter = len(fake_customer_db)
address_id_counter = len(fake_address_db)


def validate_address_id(address_id):
    """
    Validates if the provided address_id exists in the address database.
    
    Args:
        address_id (int): The address ID to validate.
        address_db (List[dict]): The list of addresses to check against.
    
    Raises:
        HTTPException: Raises a 400 Bad Request error if the address_id is not valid.
    """
    if not any(address["id"] == address_id for address in fake_address_db):
        raise HTTPException(status_code=400, detail="Invalid address_id provided")

@app.get('/')
def get():
    return 'the app is running'

@app.get('/customers/')
def get_all_customer():
    return fake_customer_db

@app.get('/customers/{customer_id}')
def get_customer(customer_id: int):
    for customer in fake_customer_db:
        if customer["id"] == customer_id:
            return customer
    raise HTTPException(status_code=404, detail="Customer not found")

@app.post("/customers/", response_model= Customer)
def create_customer(customer: CustomerBase):
    global customer_id_counter
    validate_address_id(customer.address_id)
    customer_data = customer.model_dump()
    customer_data["id"] = customer_id_counter  
    response = Customer(**customer_data)
    fake_customer_db.append(customer_data)
    customer_id_counter += 1
    return response

@app.delete('/customers/{customer_id}')
def delete_customer(customer_id: int):
    for i,customer in enumerate(fake_customer_db):
        if customer_id == customer['id']:
           del fake_customer_db[i]
           return {"message": "Customer deleted successfully"}
    raise HTTPException(status_code=404, detail="Customer not found")

@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, updated_customer: dict):
    for i, customer in enumerate(fake_customer_db):
        if customer["id"] == customer_id:
            updated_customer['id'] = customer_id
            fake_customer_db[i] = updated_customer
            return {"message": "Customer updated successfully"}
    raise HTTPException(status_code=404, detail="Customer not found")


@app.get("/addresses/")
def get_all_addresses():
    return fake_address_db

@app.post("/addresses/",response_model=Address)
def create_address(address: AddressBase):
    global address_id_counter
    address_data = address.model_dump()
    address_data["id"] = address_id_counter  
    print(address_data)
    response = Address(**address_data)
    fake_address_db.append(address_data)
    print(fake_address_db)
    address_id_counter += 1
    return response

@app.get("/addresses/{address_id}", response_model=Address)
def get_address(address_id: int):
    for address in fake_address_db:
        if address['id'] == address_id:
            return address
    raise HTTPException(status_code=404, detail="Address not found")

@app.put("/addresses/{address_id}")
def update_address(address_id: int, updated_address: dict):
    for i, address in enumerate(fake_address_db):
        if address["id"] == address_id:
            updated_address['id']=address_id
            fake_address_db[i] = updated_address
            return {"message": "Address updated successfully"}
    raise HTTPException(status_code=404, detail="Address not found")

@app.delete('/addresses/{address_id}')
def delete_address(address_id: int):
    for i,address in enumerate(fake_address_db):
        if address_id == address['id']:
           del fake_address_db[i]
           return {"message": "Address deleted successfully"}
    raise HTTPException(status_code=404, detail="Address not found")

@app.get("/customers/{customer_id}/address")
async def get_customer_address(customer_id: int):
    for customer in fake_customer_db:
        if customer["id"] == customer_id:
            address_id = customer["address_id"]
        for address in fake_address_db:
            if address["id"] == address_id:
                return address
    raise HTTPException(status_code=404, detail="Address not found")

