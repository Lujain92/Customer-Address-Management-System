from fastapi import FastAPI
from routers import customer, address

app = FastAPI()

app.include_router(customer.router)
app.include_router(address.router)

@app.get('/')
def get_root():
    """
    Root endpoint to check if the app is running.
    """
    return 'The app is running'
