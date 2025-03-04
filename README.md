# User-Administrator

**Flask Application for CRUD Operations on MongoDB**

This repository contains a Flask-based REST API application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a `User` resource. The application is designed to be scalable, modular, and easy to maintain.

## Table of Contents

- [Features](#features)
- [Hosting](#hosted-application)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing with Postman](#testing-with-postman)
- [Docker Setup](#docker-setup)
- [Design Decisions](#design-decisions)

## Features

- **CRUD Operations**: Implements Create, Read, Update, and Delete operations for a `User` resource.
- **RESTful API**: Provides RESTful endpoints for interacting with the `User` resource.
- **MongoDB Integration**: Uses MongoDB as the backend database with `mongoengine` for ORM-like functionality.
- **Scalable Design**: Modular and clean code structure for scalability and maintainability.
- **Error Handling**: Includes robust error handling for invalid requests and database errors.
- **Dockerized**: The application is containerized using Docker for easy deployment.

## Hosted Application

This application is hosted on Amazon EC2 Server. \

- **Base URL**: http://3.107.203.197:8000/
- **Docs URL**: http://3.107.203.197:8000/docs

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.9 or higher
- Docker and Docker Compose
- MongoDB (optional, if not using the Dockerized MongoDB service)
- Postman (for testing the API)

## Project Structure

```
.
├── app/
│   ├── __init__.py          # Application initialization and database connection
│   ├── config.py            # Configuration settings and env variables
│   ├── models/              # Database models (e.g., User model)
│   ├── routes/              # API routes
│   ├── services/            # Business logic for CRUD operations
│   ├── templates/           # HTML templates for landing page and documentation
│   └── utils/               # Utility functions for request/response handling
├── env/                     # Environment variable management
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker configuration for the Flask app
├── docker-compose.yml       # Docker Compose configuration
├── run.py                   # Entry point for Gunicorn
└── README.md                # This file
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/masked-redhat/User-Administrator.git
cd User-Administrator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory and add the following variables:

```env
PORT=8000
HOST=0.0.0.0
MONGO_HOST=mongo
MONGO_PORT=27017
MONGO_DATABASE=corider-user-admin
ENV=prod
```

## Running the Application

### Option 1: Run Locally (Without Docker)

1. Start MongoDB locally or use an external MongoDB instance.
2. Run the Flask app:

```bash
python app.py
```

The app will start on `http://localhost:8000`.

### Option 2: Run with Docker

1. Build and start the containers:

```bash
docker compose up
```

2. Access the app at `http://localhost:8000`.

3. MongoDB data will persist in the `mongo_data` volume.

## API Endpoints

| Method   | Endpoint      | Description                    |
| -------- | ------------- | ------------------------------ |
| `GET`    | `/users`      | Retrieve a list of all users   |
| `GET`    | `/users/<id>` | Retrieve a specific user by ID |
| `POST`   | `/users`      | Create a new user              |
| `PUT`    | `/users/<id>` | Update an existing user by ID  |
| `DELETE` | `/users/<id>` | Delete a user by ID            |

### Example Request Payload (POST/PUT)

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "securepassword"
}
```

### Example Response

```json
{
  "message": "User created",
  "success": true,
  "id": "651b3f9a8f1b3f9a8f1b3f9a"
}
```

## Testing with Postman

1. Open Postman and create a new HTTP request for each endpoint.
2. Send requests to the endpoints to test CRUD operations.
3. Verify that the responses are correct and the database is updated.

## Docker Setup

### Build and Run

```bash
docker compose up
```

## Design Decisions

1. **Modular Architecture**: Divided into separate modules (`models`, `routes`, `services`, etc.) for better organization and scalability.
2. **MongoEngine ORM**: Used `mongoengine` for MongoDB integration to simplify database interactions.
3. **Custom Utilities**: Created utility classes (`ReqBody`, `SendResponse`) for consistent request parsing and response formatting.
4. **Error Handling**: Added custom exceptions (`NoUserError`) and centralized error handling for invalid requests and database errors.
5. **Environment Variables**: Used `.env` files for managing configuration, ensuring flexibility across environments.
6. **Dockerization**: Containerized the application for easy deployment and reproducibility.
