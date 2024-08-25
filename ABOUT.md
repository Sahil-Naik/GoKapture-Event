# Task Management System API

## Overview
This project is a RESTful API for a Task Management System, designed to manage user tasks with features like user authentication, task creation, assignment, and filtering.

## Technologies Used
- **Programming Language:** Python
- **Framework:** Flask
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT (JSON Web Tokens)
- **Containerization:** Docker

## Features Implemented
1. **User Registration & Authentication**
   - Secure user registration with hashed passwords.
   - Login functionality with JWT token generation for authenticated access.

2. **Task Management**
   - CRUD operations for tasks (Create, Read, Update, Delete).
   - Task assignment to users.
   - Filtering tasks by status, priority, and due date.
   - Search functionality for tasks by title or description.

3. **Database**
   - MySQL used as the relational database.
   - SQLAlchemy for ORM to interact with the database.
   - Automatic table creation and migrations.

4. **Containerization**
   - Dockerfile and `docker-compose.yml` for containerizing the application.
   - Separate containers for the Flask app and MySQL database.

## Additional Notes
- **Testing:** Endpoints have been tested using Postman.
- **Dependencies:** All necessary Python packages are listed in `requirements.txt`, including `flask_jwt_extended` for JWT support.

## Getting Started
1. **Install Dependencies:** `pip install -r requirements.txt`
2. **Run Migrations:** `flask db upgrade`
3. **Start the App:** `docker-compose up`
