# Causes API Development

## Project Overview

This project involves the development of a RESTful API to manage social causes and contributions. The API allows users to create, view, update, and delete causes, as well as contribute to specific causes. The application uses Django Rest Framework (DRF) for building the API and MySQL for data storage, with JWT authentication for secure user interactions.

## Technologies Used

- **Django & DRF**: Framework for building the API, serialization, and view handling.
- **MySQL**: Database for storing causes and contributions.
- **JWT Authentication**: Token-based authentication for secure API access.
- **Postman**: For testing and validating API endpoints.

## Key Features

- **User Registration**: Simple API endpoint for creating a new user.
- **Cause Management**: Endpoints for creating, updating, retrieving, and deleting causes.
- **Contributions**: Users can contribute to a cause by providing their name, email, and amount.

## Key API Endpoints

### User Registration & Authentication

- **POST /api/register/**: Register a new user with `username` and `password`.
  
- **POST /api/token/**: Obtain JWT token by providing `username` and `password`.
  
- **POST /api/token/refresh/**: Refresh the JWT token.

### Cause Management

- **POST /api/causes/**: Create a new cause (fields: `title`, `description`, `image_url`).
  
- **GET /api/causes/**: Retrieve a list of all causes.

- **GET /api/causes/{id}/**: Retrieve a specific cause by `id`.

- **PUT /api/causes/{id}/**: Update a cause by `id`.

- **DELETE /api/causes/{id}/**: Delete a specific cause by `id`.

### Contribution Management

- **POST /api/causes/{id}/contribute/**: Contribute to a cause (fields: `name`, `email`, `amount`).

- **GET /api/causes/{id}/contributions/**: Retrieve contributions for a specific cause.

- **GET /api/contributions/**: Retrieve all contributions across all causes.

## How to Use the API

### User Registration & Authentication

1. **Register a New User**:
   - POST request to `/api/register/` with the following body:
     ```json
     {
       "username": "john_doe",
       "password": "password123"
     }
     ```
   - Response:
     ```json
     {
       "message": "User created successfully"
     }
     ```

2. **Obtain JWT Token**:
   - POST request to `/api/token/` with the following body:
     ```json
     {
       "username": "john_doe",
       "password": "password123"
     }
     ```
   - Response:
     ```json
     {
       "access": "your_access_token",
       "refresh": "your_refresh_token"
     }
     ```

### Cause Operations

- **Create a Cause**:
  - POST request to `/api/causes/` with the following body:
    ```json
    {
      "title": "Save the Trees",
      "description": "A cause to protect the environment",
      "image_url": "http://example.com/image.jpg"
    }
    ```
  - Response:
    ```json
    {
      "id": 1,
      "title": "Save the Trees",
      "description": "A cause to protect the environment",
      "image_url": "http://example.com/image.jpg"
    }
    ```

- **Retrieve All Causes**:
  - GET request to `/api/causes/`.
  - Response:
    ```json
    [
      {
        "id": 1,
        "title": "Save the Trees",
        "description": "A cause to protect the environment",
        "image_url": "http://example.com/image.jpg"
      },
      {
        "id": 2,
        "title": "Save the Oceans",
        "description": "A cause to protect the oceans",
        "image_url": "http://example.com/ocean_image.jpg"
      }
    ]
    ```

- **Retrieve a Specific Cause**:
  - GET request to `/api/causes/{id}/`.
  - Response:
    ```json
    {
      "id": 1,
      "title": "Save the Trees",
      "description": "A cause to protect the environment",
      "image_url": "http://example.com/image.jpg"
    }
    ```

- **Update a Cause**:
  - PUT request to `/api/causes/{id}/` with the following body:
    ```json
    {
      "title": "Protect the Forests",
      "description": "A new initiative to protect forests",
      "image_url": "http://example.com/new_image.jpg"
    }
    ```
  - Response:
    ```json
    {
      "id": 1,
      "title": "Protect the Forests",
      "description": "A new initiative to protect forests",
      "image_url": "http://example.com/new_image.jpg"
    }
    ```

- **Delete a Cause**:
  - DELETE request to `/api/causes/{id}/`.
  - Response:
    ```json
    {
      "message": "Cause deleted successfully"
    }
    ```

### Contribution Operations

- **Contribute to a Cause**:
  - POST request to `/api/causes/{id}/contribute/` with the following body:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "amount": 100.00
    }
    ```
  - Response:
    ```json
    {
      "message": "Contribution added successfully",
      "cause_id": 1,
      "amount": 100.00
    }
    ```

- **Retrieve Contributions for a Cause**:
  - GET request to `/api/causes/{id}/contributions/`.
  - Response:
    ```json
    [
      {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "amount": 100.00
      },
      {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "amount": 50.00
      }
    ]
    ```

## Approach & Solution

- **Data Modeling**: The `Cause` and `Contribution` models define the core entities of the application.
- **Authentication**: JWT is used for secure user authentication.
- **Error Handling**: Each endpoint handles errors by returning appropriate status codes and messages (e.g., 400 for bad requests, 404 for not found).

## Challenges Faced

- **Token Authentication**: Initially struggled with token expiration and renewal, but resolved the issue for stable functionality.
- **Data Validation**: Ensured proper validation of data, such as only accepting positive contribution amounts.
- **Model Relationships**: Successfully linked contributions to causes using Django's ORM.

## Future Considerations

- **Logging**: Add logging to monitor activity and errors more efficiently.
- **Rate-Limiting**: Implement rate-limiting to prevent abuse of the contribution endpoints.
- **Pagination**: Add pagination to the GET `/causes/` endpoint for scalability.

## Conclusion

This API provides a platform for managing social causes and contributions. It integrates secure user authentication, CRUD operations for causes, and facilitates contributions to social causes. The system is built using Django and Django Rest Framework, ensuring a robust and extensible architecture.

---

Feel free to contribute to the project by forking the repository or opening an issue if you encounter any bugs or have suggestions for improvement.
