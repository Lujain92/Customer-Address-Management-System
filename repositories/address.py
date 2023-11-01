from fastapi import  HTTPException
from controllers.models.address import Address
from uuid import uuid4

fake_address_db = []

def get():
    """
    Retrieve all addresses from the fake_address_db.

    Returns:
        List[dict]: A list of address objects.
    """
    return fake_address_db

def get_by_id(id):
    """
    Retrieve an address by its ID from the fake_address_db.

    Parameters:
        id (UUID4): The unique identifier of the address to be retrieved.

    Returns:
        dict: Address details as a dictionary.

    Raises:
        HTTPException: If the address with the specified ID is not found, a 404 error is raised.
    """
    for address in fake_address_db:
        if address['id'] == id:
            return address
        
    raise HTTPException(status_code=404, detail='Address not found')

def create(address):
    """
    Create a new address and add it to the fake_address_db.

    Parameters:
        address (Address): An instance of the Address model representing the new address to be created.

    Returns:
        Address: The newly created Address object.
    """
    address_data = address.dict()

    address_data['id'] = uuid4()

    response = Address(**address_data)
    fake_address_db.append(address_data)

    return response

def delete(id):
    """
    Delete an address by its ID from the fake_address_db.

    Parameters:
        id (UUID4): The unique identifier of the address to be deleted.

    Returns:
        dict: A message indicating the successful deletion of the address.

    Raises:
        HTTPException: If the address with the specified ID is not found, a 404 error is raised.
    """
    for i, address in enumerate(fake_address_db):
        if id == address['id']:
            del fake_address_db[i]
            return {'message': 'Address deleted successfully'}
        
    raise HTTPException(status_code=404, detail='Address not found')

def update(id, updated_address):
    """
    Update an existing address with new data based on its ID in the fake_address_db.

    Parameters:
        id (UUID4): The unique identifier of the address to be updated.
        updated_address (Address): An instance of the Address model containing updated data for the address.

    Returns:
        dict: A message indicating the successful update of the address.

    Raises:
        HTTPException: If the address with the specified ID is not found, a 404 error is raised.
    """
    for i, address in enumerate(fake_address_db):
        if address['id'] == id:
            updated_address_data = updated_address.dict()
            updated_address_data['id'] = id

            fake_address_db[i] = updated_address_data

            return {'message': 'Address updated successfully'}
        
    raise HTTPException(status_code=404, detail='Address not found')
