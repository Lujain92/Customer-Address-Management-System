from fastapi import APIRouter, HTTPException
from models.address import Address, AddressBase
from models.address_db import fake_address_db, address_id_counter

router = APIRouter()

@router.get('/addresses/', response_model=list[Address])
def get_all_addresses():
    """
    Retrieve a list of all addresses.
    
    Returns:
        list[Address]: List of address objects.
    
    Raises:
        HTTPException(404): Raised if no addresses are found.
    """
    return fake_address_db

@router.get('/addresses/{address_id}', response_model=Address)
def get_address(address_id: int):
    """
    Retrieve address information by address ID.
    
    Args:
        address_id (int): The ID of the address to retrieve.
    
    Returns:
        Address: Address object with the specified ID.
    
    Raises:
        HTTPException(404): Raised if the address with the specified ID is not found.
    """
    for address in fake_address_db:
        if address['id'] == address_id:
            return address
    raise HTTPException(status_code=404, detail="Address not found")

@router.post("/addresses/", response_model=Address)
def create_address(address: AddressBase):
    """
    Create a new address.
    
    Args:
        address (AddressBase): Address data to create a new address.
    
    Returns:
        Address: Newly created address object.
    """
    global address_id_counter
    address_data = address.model_dump()
    address_data["id"] = address_id_counter
    response = Address(**address_data)
    fake_address_db.append(address_data)
    address_id_counter += 1
    return response

@router.put("/addresses/{address_id}")
def update_address(address_id: int, updated_address: AddressBase):
    """
    Update address information by ID.
    
    Args:
        address_id (int): ID of the address to be updated.
        updated_address (AddressBase): Updated address data.
    
    Returns:
        dict: Success message if the address is updated.
    
    Raises:
        HTTPException(404): Raised if the address with the specified ID is not found.
    """
    for i, address in enumerate(fake_address_db):
        if address["id"] == address_id:
            updated_address_data = updated_address.model_dump()
            updated_address_data["id"] = address_id
            fake_address_db[i] = updated_address_data
            return {"message": "Address updated successfully"}
    raise HTTPException(status_code=404, detail="Address not found")

@router.delete('/addresses/{address_id}')
def delete_address(address_id: int):
    """
    Delete an address by ID.
    
    Args:
        address_id (int): ID of the address to be deleted.
    
    Returns:
        dict: Success message if the address is deleted.
    
    Raises:
        HTTPException(404): Raised if the address with the specified ID is not found.
    """
    for i, address in enumerate(fake_address_db):
        if address_id == address['id']:
            del fake_address_db[i]
            return {"message": "Address deleted successfully"}
    raise HTTPException(status_code=404, detail="Address not found")

