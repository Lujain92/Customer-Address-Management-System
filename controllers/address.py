from fastapi import APIRouter
from controllers.models.address import Address, AddressBase
from uuid import UUID
from repositories import address

address_router = APIRouter()

@address_router.get('/', response_model=list[Address])
def get_all_addresses():
    """
    Retrieve a list of all addresses.
    
    Returns:
        list[Address]: List of address objects.
    """
    return address.get()

@address_router.get('/{address_id}', response_model=Address)
def get_address(address_id: UUID):
    """
    Retrieve address information by address ID.
    
    Args:
        address_id (UUID): The ID of the address to retrieve.
    
    Returns:
        Address: Address object with the specified ID.
    """
    return address.get_by_id(address_id)

@address_router.post('/', response_model=Address)
def create_address(new_address: AddressBase):
    """
    Create a new address.
    
    Args:
        address (AddressBase): Address data to create a new address.
    """
    return address.create(new_address)

@address_router.put('/{address_id}')
def update_address(address_id: UUID, updated_address: AddressBase):
    """
    Update address information by ID.
    
    Args:
        address_id (UUID): ID of the address to be updated.
        updated_address (AddressBase): Updated address data.
    
    Returns:
        dict: Success message if the address is updated.
    """
    return address.update(address_id,updated_address)

@address_router.delete('/{address_id}')
def delete_address(address_id: UUID):
    """
    Delete an address by ID.
    
    Args:
        address_id (UUID): ID of the address to be deleted.
    
    Returns:
        dict: Success message if the address is deleted.
    """
    return address.delete(address_id)


