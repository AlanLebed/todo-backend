### Test for the full-stack engineer role

The backend API for the Todo List application is designed to handle all aspects of task management efficiently. This API is built using a lightweight web framework to ensure fast responses and easy maintenance. The main functionalities include:

    - Task Creation: Users can add new tasks to their todo list.
    - Task Retrieval: The API provides endpoints to retrieve all tasks, allowing users to see their entire todo list at a glance. 
    - Task Updating: Users can update details of an existing task. Updates can include marking a task as done or important.
    - Task Deletion: The API allows users to permanently remove tasks from their list.

This backend is crafted to provide robust, scalable support for a todo list application, aiming for simplicity and efficiency in task management.


### Installation
Follow these steps to set up and run the Todo List backend on your local machine:

### Prerequisites
- **Python**: Ensure Python 3.12.3 or higher is installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: Python's package installer, usually included with Python.

### Setup

1. **Clone the Repository**:
   Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/AlanLebed/todo-backend.git
   cd todo-backend


2. **Install Dependencies**:
    Install the required Python packages using pip:
    ```bash
    pip install -r requirements.txt

3. **Run the Application**:
    You can run the application directly by executing the app.py file. To do this, use the following command:
    ```bash
    python app.py




### Running the Application with Docker

This application can be run using Docker and Docker Compose to simplify dependency management and deployment. Follow these steps to get started:

### Prerequisites
- Docker installed on your machine. [Get Docker](https://www.docker.com/get-started)
- Docker Compose installed if you are using multiple containers. [Install Docker Compose](https://docs.docker.com/compose/install/)

### Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/AlanLebed/todo-backend.git
   cd todo-backend

2. Build and run the application using Docker Compose:
    ```bash
    docker-compose up --build


