from fastapi import  HTTPException
from database.address_db import fake_address_db
from database.customer_db import fake_customer_db
from utils.validator import validate_address_id
from controllers.models.customer import Customer
from uuid import uuid4


def get():
    """
    Retrieve all customers from the fake_customer_db.

    Returns:
        List[dict]: A list of customer objects.
    """
    return fake_customer_db

def get_by_id(id):
    """
    Retrieve a customer by their ID from the fake_customer_db.

    Parameters:
        id (UUID): The unique identifier of the customer to be retrieved.

    Returns:
        dict: Customer details as a dictionary.

    Raises:
        HTTPException: If the customer with the specified ID is not found, a 404 error is raised.
    """
    for customer in fake_customer_db:
        if customer['id'] == id:
            return customer
        
    raise HTTPException(status_code=404, detail='Customer not found')

def create(customer):
    """
    Create a new customer and add it to the fake_customer_db.

    Parameters:
        customer (Customer): An instance of the Customer model representing the new customer to be created.

    Returns:
        Customer: The newly created Customer object.

    Raises:
        HTTPException: If the associated address ID is not valid, a 400 error is raised.
    """

    validate_address_id(customer.address_id, fake_address_db)

    customer_data = customer.dict()

    customer_data['adult'] = True if customer_data['age'] >= 18 else False
    customer_data['id'] = uuid4()

    response = Customer(**customer_data)

    fake_customer_db.append(customer_data)

    return response

def delete(id):
    """
    Delete a customer by their ID from the fake_customer_db.

    Parameters:
        id (UUID): The unique identifier of the customer to be deleted.

    Returns:
        dict: A message indicating the successful deletion of the customer.

    Raises:
        HTTPException: If the customer with the specified ID is not found, a 404 error is raised.
    """
    for i, customer in enumerate(fake_customer_db):
        if id == customer['id']:
            del fake_customer_db[i]
            return {'message': 'Customer deleted successfully'}
        
    raise HTTPException(status_code=404, detail='Customer not found')

def update(id, updated_customer):
    """
    Update an existing customer with new data based on their ID in the fake_customer_db.

    Parameters:
        id (UUID): The unique identifier of the customer to be updated.
        updated_customer (Customer): An instance of the Customer model containing updated data for the customer.

    Returns:
        dict: A message indicating the successful update of the customer.

    Raises:
        HTTPException: If the customer with the specified ID is not found, a 404 error is raised.
    """
    for i, customer in enumerate(fake_customer_db):
        if customer['id'] == id:
            updated_customer_data = updated_customer.dict()
            updated_customer_data['id'] = id
            updated_customer_data['adult'] = True if updated_customer_data['age'] >= 18 else False


            fake_customer_db[i] = updated_customer_data

            return {'message': 'Customer updated successfully'}
        
    raise HTTPException(status_code=404, detail='Customer not found')

def get_address(id):
    """
    Retrieve the address associated with a customer by their ID from the fake_customer_db.

    Parameters:
        id (UUID): The unique identifier of the customer.

    Returns:
        dict: Address details as a dictionary.

    Raises:
        HTTPException: If the customer with the specified ID is not found or the associated address is not found, a 404 error is raised.
    """
    for customer in fake_customer_db:
        if customer['id'] == id:
            address_id = customer['address_id']

            for address in fake_address_db:
                if address['id'] == address_id:
                    return address
                
    raise HTTPException(status_code=404, detail='Address not found')
