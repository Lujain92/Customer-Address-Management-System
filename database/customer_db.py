from controllers.models.customer import Gender
from uuid import UUID

fake_customer_db = [

    {'id': UUID('3fa85f64-5717-4562-b3fc-2c963f66afa6'), 'first_name': 'Mohammad', 'last_name': 'Ahmad', 'age': 25,
        'gender': Gender.male, 'adult': True, 'address_id':  UUID('39135827-7cb4-4ebe-9df9-bb7ae15dda17'), },
    {'id': UUID('9192ce1c-19ca-4d64-aedf-2586a573e570'), 'first_name': 'Ali', 'last_name': 'Mousa', 'age': 17,
     'gender': Gender.male, 'adult': False, 'address_id': UUID('f77ef186-1716-4f73-b8ba-75cea832a834'), },
    {'id': UUID('f63eccff-8fa2-456c-ad83-9d929cf8c67e'), 'first_name': 'Fadwa', 'last_name': 'Kareem', 'age': 22,
     'gender': Gender.female, 'adult': True, 'address_id': UUID('735a1c0b-cf49-48d3-b225-1f446f3cf8ba'), },
    {'id': UUID('9d246d91-2290-4e59-b9a8-80a5c6d7ac47'), 'first_name': 'Salwa', 'last_name': 'Belal', 'age': 32,
     'gender': Gender.female, 'adult': True, 'address_id': UUID('c5474254-fd21-4196-9e14-66676e2be943'), },
]
