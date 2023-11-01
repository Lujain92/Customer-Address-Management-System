from fastapi import APIRouter
from controllers.models.customer import Customer, CustomerBase
from pydantic.types import UUID4
from repositories.customer import get, get_by_id, create, delete, update, get_address
router = APIRouter()

@router.get('/', response_model=list[Customer])
def get_all_customers():
    """
    Retrieve a list of all customers.
    
    Returns:
        list[Customer]: List of customer objects.
    """
    result = get()
    return result 
    

@router.get('/{customer_id}', response_model=Customer)
def get_customer(customer_id: UUID4):
    """
    Retrieve customer information by customer ID.
    
    Args:
        customer_id (UUID4): The ID of the customer to retrieve.
    
    Returns:
        Customer: Customer object with the specified ID.
    """
    result = get_by_id(customer_id)
    return result


@router.post('/', response_model=Customer)
def create_customer(customer: CustomerBase):
    """
    Create a new customer.
    
    Args:
        customer (CustomerBase): Customer data to create a new customer.
    
    Returns:
        Customer: Newly created customer object.
    """
    result = create(customer)
    return result
    

@router.delete('/{customer_id}')
def delete_customer(customer_id: UUID4):
    """
    Delete a customer by ID.
    
    Args:
        customer_id (UUID4): ID of the customer to be deleted.
    
    Returns:
        dict: Success message if the customer is deleted.
    """
    result = delete(customer_id)
    return result

@router.put('/{customer_id}')
def update_customer(customer_id: UUID4, updated_customer: CustomerBase):
    """
    Update customer information by ID.
    
    Args:
        customer_id (UUID4): ID of the customer to be updated.
        updated_customer (CustomerBase): Updated customer data.
    
    Returns:
        dict: Success message if the customer is updated.
    """
    result = update(customer_id, updated_customer)
    return result
   

@router.get('/{customer_id}/address')
def get_customer_address(customer_id: UUID4):
    """
    Retrieve the address of a specific customer by customer ID.

    Args:
        customer_id (UUID4): The ID of the customer whose address needs to be retrieved.

    Returns:
        dict: Address information for the specified customer.
    """
    result = get_address(customer_id)
    return result
