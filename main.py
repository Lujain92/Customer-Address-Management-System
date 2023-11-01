from fastapi import FastAPI
from controllers import customer, address

app = FastAPI()

app.include_router(customer.router, tags=['customer'], prefix='/customer')
app.include_router(address.router,tags=['address'], prefix='/address')

@app.get('/')
def get_root():
    """
    Root endpoint to check if the app is running.
    """
    return 'The app is running'
