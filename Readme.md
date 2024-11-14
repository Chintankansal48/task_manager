# Django Task Management API

This is a Django-based Task Management API, set up to run with Docker and Docker Compose, using Sqlite as the database.

## Prerequisites

- Docker
- Docker Compose

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine.

```bash
git clone https://github.com/Chintankansal48/task_manager.git
cd task_manager
```

### 2. Run to build the Docker container and service will start at http://localhost:8000:

```bash
docker-compose up --build
```
Import the Postman collection.
Obtain Auth token from the Register User API and use that token in authorization header of tasks APIs.