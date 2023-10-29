# FastAPI Customer Address Management System

### Author : Lujain Al-Jarrah
### Version : 1.0.0

This is a simple FastAPI project that demonstrates the implementation of CRUD (Create, Read, Update, Delete) operations for managing customers and addresses. It includes endpoints to create, retrieve, update, and delete customer and address records. The project utilizes FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+.

## Prerequisites

- Python 3.7+
- FastAPI and Uvicorn (for running the application)

## Installation

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/fastapi-customer-address.git
   cd fastapi-customer-address
   ```

2. **Create a Virtual Environment (Optional but recommended):**
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application:**
   ```
   uvicorn main:app --reload
   ```

   This will start the FastAPI application. By default, the API can be accessed at [http://localhost:8000](http://localhost:8000).

2. **API Endpoints:**

   - **Customers:**
     - `GET /customers/`: Retrieve all customers.
     - `GET /customers/{customer_id}`: Retrieve customer by ID.
     - `POST /customers/`: Create a new customer.
     - `PUT /customers/{customer_id}`: Update customer by ID.
     - `DELETE /customers/{customer_id}`: Delete customer by ID.
     
   - **Addresses:**
     - `GET /addresses/`: Retrieve all addresses.
     - `GET /addresses/{address_id}`: Retrieve address by ID.
     - `POST /addresses/`: Create a new address.
     - `PUT /addresses/{address_id}`: Update address by ID.
     - `DELETE /addresses/{address_id}`: Delete address by ID.

3. **API Documentation (Swagger UI):**
   The API documentation and interactive playground can be accessed at [http://localhost:8000/docs](http://localhost:8000/docs).
