from fastapi import APIRouter, HTTPException
from models.customer import Customer, CustomerBase
from models.customer_db import fake_customer_db, customer_id_counter
from models.address_db import fake_address_db
from utils.validator import validate_address_id

router = APIRouter()

@router.get('/customers/', response_model=list[Customer])
def get_all_customers():
    """
    Retrieve a list of all customers.
    
    Returns:
        list[Customer]: List of customer objects.
    
    Raises:
        HTTPException(404): Raised if no customers are found.
    """
    return fake_customer_db

@router.get('/customers/{customer_id}', response_model=Customer)
def get_customer(customer_id: int):
    """
    Retrieve customer information by customer ID.
    
    Args:
        customer_id (int): The ID of the customer to retrieve.
    
    Returns:
        Customer: Customer object with the specified ID.
    
    Raises:
        HTTPException(404): Raised if the customer with the specified ID is not found.
    """
    for customer in fake_customer_db:
        print(customer)
        if customer["id"] == customer_id:
            return customer
    raise HTTPException(status_code=404, detail="Customer not found")

@router.post("/customers/", response_model=Customer)
def create_customer(customer: CustomerBase):
    """
    Create a new customer.
    
    Args:
        customer (CustomerBase): Customer data to create a new customer.
    
    Returns:
        Customer: Newly created customer object.
    
    Raises:
        HTTPException(400): Raised if the provided address_id is not valid.
    """
    global customer_id_counter
    validate_address_id(customer.address_id, fake_customer_db)
    customer_data = customer.model_dump()
    customer_data["id"] = customer_id_counter
    response = Customer(**customer_data)
    fake_customer_db.append(customer_data)
    customer_id_counter += 1
    return response

@router.delete('/customers/{customer_id}')
def delete_customer(customer_id: int):
    """
    Delete a customer by ID.
    
    Args:
        customer_id (int): ID of the customer to be deleted.
    
    Returns:
        dict: Success message if the customer is deleted.
    
    Raises:
        HTTPException(404): Raised if the customer with the specified ID is not found.
    """
    for i, customer in enumerate(fake_customer_db):
        if customer_id == customer['id']:
            del fake_customer_db[i]
            return {"message": "Customer deleted successfully"}
    raise HTTPException(status_code=404, detail="Customer not found")

@router.put("/customers/{customer_id}")
def update_customer(customer_id: int, updated_customer: CustomerBase):
    """
    Update customer information by ID.
    
    Args:
        customer_id (int): ID of the customer to be updated.
        updated_customer (CustomerBase): Updated customer data.
    
    Returns:
        dict: Success message if the customer is updated.
    
    Raises:
        HTTPException(404): Raised if the customer with the specified ID is not found.
    """
    for i, customer in enumerate(fake_customer_db):
        if customer["id"] == customer_id:
            updated_customer_data = updated_customer.model_dump()
            updated_customer_data["id"] = customer_id
            fake_customer_db[i] = updated_customer_data
            return {"message": "Customer updated successfully"}
    raise HTTPException(status_code=404, detail="Customer not found")

@router.get("/customers/{customer_id}/address")
def get_customer_address(customer_id: int):
    """
    Retrieve the address of a specific customer by customer ID.

    Args:
        customer_id (int): The ID of the customer whose address needs to be retrieved.

    Returns:
        dict: Address information for the specified customer.
        
    Raises:
        HTTPException(404): Raised if the customer with the specified ID or their address is not found.
    """
    for customer in fake_customer_db:
        print(customer)
        if customer["id"] == customer_id:
            address_id = customer["address_id"]
            for address in fake_address_db:
                if address["id"] == address_id:
                    return address
    raise HTTPException(status_code=404, detail="Address not found")