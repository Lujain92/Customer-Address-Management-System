from fastapi import APIRouter
from controllers.models.address import Address, AddressBase
from pydantic.types import UUID4
from repositories.address import get, get_by_id, create, delete, update

router = APIRouter()

@router.get('/', response_model=list[Address])
def get_all_addresses():
    """
    Retrieve a list of all addresses.
    
    Returns:
        list[Address]: List of address objects.
    """
    result = get()
    return result

@router.get('/{address_id}', response_model=Address)
def get_address(address_id: UUID4):
    """
    Retrieve address information by address ID.
    
    Args:
        address_id (UUID4): The ID of the address to retrieve.
    
    Returns:
        Address: Address object with the specified ID.
    """
    result = get_by_id(address_id)
    return result

@router.post('/', response_model=Address)
def create_address(address: AddressBase):
    """
    Create a new address.
    
    Args:
        address (AddressBase): Address data to create a new address.
    """
    result = create(address)
    return result

@router.put('/{address_id}')
def update_address(address_id: UUID4, updated_address: AddressBase):
    """
    Update address information by ID.
    
    Args:
        address_id (UUID4): ID of the address to be updated.
        updated_address (AddressBase): Updated address data.
    
    Returns:
        dict: Success message if the address is updated.
    """
    result = update(address_id,updated_address)
    return result

@router.delete('/{address_id}')
def delete_address(address_id: UUID4):
    """
    Delete an address by ID.
    
    Args:
        address_id (UUID4): ID of the address to be deleted.
    
    Returns:
        dict: Success message if the address is deleted.
    """
    result = delete(address_id)
    return result

