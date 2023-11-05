from fastapi import HTTPException
from typing import List

def validate_address_id(address_id: int, address_db: List[dict]):
    """
    Validates if the provided address_id exists in the address database.
    
    Args:
        address_id (int): The address ID to validate.
        address_db (List[dict]): The list of addresses to check against.
    
    Raises:
        HTTPException: Raises a 400 Bad Request error if the address_id is not valid.
    """
    if not any(address['id'] == address_id for address in address_db):
        raise HTTPException(status_code=400, detail='Address not found')
    
