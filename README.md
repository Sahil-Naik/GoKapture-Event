# Created by
## _Sahil Naik_

Python SDE, Full-Stack Dev, Data Scientist, ML Engineer,
R, PHP, Java.

# Features
- Python
- RESTful API
- Flask
- Postman
- Docker

# Included Documentations
- Launching the APP locally
- Test cases to test on Postman (link: https://postman.com/)

> Postman is a standalone software testing API platform that allows users to build, test, design, modify, and document APIs
 
 # IDE Used
 **PyCharm** ver. 2024.2.0.1
 
 # Pre-requisite
 1. For SQL I'm using XAMPP Server with the following configuration
- username: root
- password:
- database: task_db

2. An account on Postman (link: https://postman.com/).
## Installation

This code requires [Python](https://www.python.org/downloads/) 3.1x.x to run.

Install the dependencies and devDependencies.
project_name/requirements.txt

Enter the following in PyCharm Bash Shell (Terminal):
```sh
cd task_management_api
pip install -r requirements.txt
```
This will install all the necessary packages to run the APP.

For **SQL** environments:
project_name/task_management_api/initialize_db.py
```sh
python initialize_db.py
```
This will create all the necessay Tables and their columns inside MySQL Server

# Softwares used

| Name |
| ------ |
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) |
| [XAMPP](https://www.apachefriends.org/download.html) |
| Postman Agent |
|[Github Desktop](https://desktop.github.com/download/)|

# Directory
The following is the structure of the project. Your directory should look similar to this.
```sh
task_management_api/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
│
├──  migrations/
│   ├── .
│   └── .
│
├── docker-compose.yml
├── rquirements.txt
├── test.py
└── run.py

```

# Launching App
Open PyCharm Terminal and make sure the current directory is project_name/task_management_api/.

The following file must be present in the directory:
```sh
run.py
```

Next,
Type the following in the terminal:
```sh
python run.py
```

If done correctly,
The following should appear on the terminal:
```sh
* Serving Flask app 'app'
* Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
* Restarting with stat
* Debugger is active!
* Debugger PIN: xxx-xxx-xxx
```

Now the APP has launched!

## Testing the APP
### 1. Postman Account
1. Open the [Postman site](https://postman.com/)
2. Login/Signup into your account
 
### 2. Using Postman
1. Download and Install Postman: Download Postman.

2. Create a New Request:
Open Postman and click on “New” > “Request”.
Enter a name for your request and choose a collection if desired.

3. Set Up the Request:
**Method:** Choose POST (or other methods depending on the endpoint).
**URL:** Enter the URL of your endpoint, e.g., http://127.0.0.1:5000/api/register.
**Headers:** Add a header with Key: Content-Type and Value: application/json.
**Body:** Select raw and enter your JSON payload, e.g.
    ```sh
    {
      "username": "testuser",
      "password": "testpass"
    }
    ```

4. **Send the Request:** Click “Send” and view the response in the lower section of the Postman window.

### 3. Postman Test-cases
### A. User Registration
**Endpoint:** POST /api/register
**Request:**
**URL:** http://127.0.0.1:5000/api/register
**Method:** POST
**Headers:** Content-Type: application/json
**Body:**
```sh
{
  "username": "testuser",
  "password": "testpass"
}
```
**Expected Response:**
**Status Code:** 201 Created
**Body:**
```sh
{
  "message": "User registered successfully"
}
```

### B. User Login
**Endpoint:** POST /api/login
**Request:**
**URL:** http://127.0.0.1:5000/api/login
**Method:** POST
**Headers:** Content-Type: application/json
**Body:**
```sh
{
  "username": "testuser",
  "password": "testpass"
}
```
**Expected Response:**
**Status Code:** 200 OK
**Body:**
```sh
{
  "access_token": "your_jwt_token_here"
}
```

### C. Create Task
**Endpoint:** POST /api/tasks
**Request:**
**URL:** http://127.0.0.1:5000/api/tasks
**Method:** POST
**Headers:** Content-Type: application/json
**Authorization:** Bearer <your_jwt_token_here>
**Body:**
```sh
{
  "title": "Test Task",
  "description": "This is a test task.",
  "status": "Todo",
  "priority": "High",
  "due_date": "2024-08-31",
  "user_id": 1
}
```
**Expected Response:**
**Status Code:** 201 Created
**Body:**
```sh
{
  "message": "Task created successfully"
}
```

### D. Get Tasks
**Endpoint:** GET /api/tasks
**Request:**
**URL:** http://127.0.0.1:5000/api/tasks
**Method:** GET
**Headers:**
**Authorization:** Bearer <your_jwt_token_here>

**Expected Response:**
**Status Code:** 200 OK
**Body:**
```sh
[
    {
    "id": 1,
    "title": "Test Task",
    "description": "This is a test task.",
    "status": "Todo",
    "priority": "High",
    "due_date": "2024-08-31T00:00:00",
    "created_at": "2024-08-24T00:00:00",
    "updated_at": "2024-08-24T00:00:00",
    "user_id": 1
    }
]
```

### E. Update Task
**Endpoint:** PUT /api/tasks/<task_id>
**Request:**
**URL:** http://127.0.0.1:5000/api/tasks/1 (replace <task_id> with the actual task ID)
**Method:** PUT
**Headers:** Content-Type: application/json
**Authorization:** Bearer <your_jwt_token_here>
**Body:**
```sh
{
  "title": "Updated Task",
  "description": "This task has been updated.",
  "status": "In Progress",
  "priority": "Medium"
}
```
**Expected Response:**
**Status Code:** 200 OK
**Body:**
```sh
{
  "message": "Task updated successfully"
}
```

### F. Delete Task
**Endpoint:** DELETE /api/tasks/<task_id>
**Request:**
**URL:** http://127.0.0.1:5000/api/tasks/1 (replace <task_id> with the actual task ID)
**Method:** DELETE
**Headers:**
**Authorization:** Bearer <your_jwt_token_here>

**Expected Response:**
**Status Code:** 200 OK
**Body:**
```sh
{
  "message": "Task deleted successfully"
}
```

Notes:
•	Replace <your_jwt_token_here> with the JWT token you receive from the login endpoint.
•	Ensure that your Flask server is running and accessible at http://127.0.0.1:5000.
•	Adjust the test cases as needed based on your actual implementation and requirements.


# Docker Installation

### 1. Install Docker Desktop for Windows
If you haven’t already, install Docker Desktop for Windows:
- Download Docker Desktop from the [Official docker website](https://www.docker.com/products/docker-desktop/).
- Run the installer and follow the prompts.
- After installation, launch Docker Desktop and ensure it’s running. You should see the Docker icon in your system tray.

### 2. Enable WSL 2 (Optional, but Recommended)
For better performance, especially with file system operations, enable WSL 2 (Windows Subsystem for Linux):
- Go to the Docker Desktop settings.
- Under the General tab, check the option to Use the WSL 2 based engine.
- Install a Linux distribution from the Microsoft Store if you haven't already.

### 3. Open PyCharm
- Open your project in PyCharm.
- Ensure that you have your Dockerfile and docker-compose.yml files in the root directory of your project.

### 4. Open Terminal in PyCharm
In PyCharm, open the terminal by selecting View > Tool Windows > Terminal.
You should see a terminal window at the bottom of the PyCharm interface.

### 5. Build Docker Containers
In the terminal, navigate to the directory containing your docker-compose.yml file (if not already there) and run:
> Directory: project_name/task_management_api/.
```sh
docker-compose build
```
This command builds the Docker images according to the instructions in the Dockerfile.

### 6. Run Docker Containers
After the build process is complete, run the containers using:
```sh
docker-compose up
```
This will start your Flask app and MySQL database in their respective containers. You should see logs appearing in the terminal as the containers start.

7. Access Your Flask Application
Once the containers are running, you can access your Flask application by navigating to:

http://localhost:5000 or
http://127.0.0.1:5000
in your web browser.

### 8. Verify Everything is Working
Check the Docker Containers:
In Docker Desktop, you can see the running containers and their status.

Logs:
You can monitor the logs in the PyCharm terminal to see the output from your Flask app and database.

### 9. Stopping the Containers
When you’re done testing:
- Go to the PyCharm terminal.
- Press Ctrl + C to stop the running containers.

Alternatively, you can stop the containers using:
```sh
docker-compose down
```
This command will stop and remove the containers, networks, and any associated volumes.

### 10. Managing Docker from Docker Desktop
Docker Desktop provides a GUI to manage containers, images, networks, and volumes, making it easy to interact with your Docker environment without using the command line.
