from fastapi import FastAPI
from controllers.customer import customer_router
from controllers.address import address_router


app = FastAPI()

app.include_router(customer_router, tags=['customer'], prefix='/customer')
app.include_router(address_router,tags=['address'], prefix='/address')

@app.get('/')
def get_root():
    """
    Root endpoint to check if the app is running.
    """
    return 'The app is running'

