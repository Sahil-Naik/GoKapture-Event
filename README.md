# Created by
## _Sahil Naik_

Python SDE, Full-Stack Dev, Data Scientist, ML Engineer,
R, PHP, Java.

## Features
- Python
- RESTful API
- Flask
- Postman
- Docker

## Included Documentations
- Launching the APP locally
- Test cases to test on Postman (link: https://postman.com/)

> Postman is a standalone software testing API platform that allows users to build, test, design, modify, and document APIs
 
 ## IDE Used
 **PyCharm** ver. 2024.2.0.1
 
 ## Pre-requisite
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

## Softwares used

| Name |
| ------ |
| [Docker Desktop](https://www.docker.com/products/docker-desktop/) |
| [XAMPP](https://www.apachefriends.org/download.html) |
| Postman Agent |
|[Github Desktop](https://desktop.github.com/download/)|

## Docker Installation

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
