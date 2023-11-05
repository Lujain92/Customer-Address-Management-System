from fastapi import APIRouter
from controllers.models.customer import Customer, CustomerBase
from uuid import UUID
from repositories import customer

customer_router = APIRouter()

@customer_router.get('/', response_model=list[Customer])
def get_all_customers():
    """
    Retrieve a list of all customers.
    
    Returns:
        list[Customer]: List of customer objects.
    """
    return customer.get() 
    

@customer_router.get('/{customer_id}', response_model=Customer)
def get_customer(customer_id: UUID):
    """
    Retrieve customer information by customer ID.
    
    Args:
        customer_id (UUID): The ID of the customer to retrieve.
    
    Returns:
        Customer: Customer object with the specified ID.
    """
    return customer.get_by_id(customer_id)


@customer_router.post('/', response_model=Customer)
def create_customer(new_customer: CustomerBase):
    """
    Create a new customer.
    
    Args:
        customer (CustomerBase): Customer data to create a new customer.
    
    Returns:
        Customer: Newly created customer object.
    """
    return customer.create(new_customer)
    

@customer_router.delete('/{customer_id}')
def delete_customer(customer_id: UUID):
    """
    Delete a customer by ID.
    
    Args:
        customer_id (UUID): ID of the customer to be deleted.
    
    Returns:
        dict: Success message if the customer is deleted.
    """
    return customer.delete(customer_id)

@customer_router.put('/{customer_id}')
def update_customer(customer_id: UUID, updated_customer: CustomerBase):
    """
    Update customer information by ID.
    
    Args:
        customer_id (UUID): ID of the customer to be updated.
        updated_customer (CustomerBase): Updated customer data.
    
    Returns:
        dict: Success message if the customer is updated.
    """
    return customer.update(customer_id, updated_customer)
   

@customer_router.get('/{customer_id}/address')
def get_customer_address(customer_id: UUID):
    """
    Retrieve the address of a specific customer by customer ID.

    Args:
        customer_id (UUID): The ID of the customer whose address needs to be retrieved.

    Returns:
        dict: Address information for the specified customer.
    """
    return customer.get_address(customer_id)

