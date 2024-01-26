# Django ToDo List Application

To Do list app with User Registration, Login, Search and full Create Read Update and DELETE functionality.

## Overview

This Django-based ToDo List application allows users to manage their tasks efficiently. Users can create, update, and delete tasks, mark them as complete, and search for specific tasks. The application uses Django's authentication system for user management.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Database Configuration](#database-configuration)
- [Deploying on Heroku](#deploying-on-heroku)
- [404page] (#404page)
- [Testing] (#testing)
- [Debug] (#debug)
- s[Contributing](#contributing) 
- [License](#license)

## Features

- User authentication (login, register, logout)
## Login:
    Purpose: The login process is initiated when a user wants to access a secured system, application,
#### Steps:
The user enters their username and password in the designated fields on the login page.
The system checks the entered credentials against stored user data (usually stored securely in a database).
If the provided credentials match the stored information, the user is granted access to the system, and a session is established.

## Register:

    Purpose: The registration process is necessary for new users who want to create an account and gain access to the system.

## Logout:

    Purpose: The logout process is initiated when a user wants to end their session and terminate access to the system. 
#### Steps:
The user initiates the logout process by clicking on a "logout" button or similar action.
The system terminates the user's session, removing any active authentication tokens or cookies associated with that session.
After logout, the user is typically redirected to a login page or a homepage, and they need to reauthenticate to access secure areas again.

- Create, update, and delete tasks

## Create Task:
    Purpose: The create task operation is used when a user wants to add a new task to their task list or project    
#### Steps:
The user navigates to the interface or page where tasks can be created.
They input relevant information for the new task, such as a title, description, 

## Update Task:
        Purpose: The update task operation allows users to modify the details of an existing task. 
#### Steps:
The user selects the task they want to update from their task list.
They navigate to the task details page or a task editing interface.


- Mark tasks as complete
    Here you keep track of your progress and stay organized. 
    When you finish a task or accomplish a specific goal, you can mark that task as complete. 

- Search functionality to filter tasks
Purpose: The primary goal of search functionality is to empower users to find particular tasks efficiently.

#### Search Bar:
The user interface typically includes a search bar where users can input keywords, phrases, or specific criteria related to the tasks they are trying to locate.

## Requirements

- Python 3.x
- Django 4.2
- elephantsql

## Installation

1. Clone the repository:

    ```bash
    git clone  https://github.com/JoannaAdermark1/My_django_project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd todo-list
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Applied database migrations:

    ```bash
    python manage.py migrate
    ```

5. Created a superuser account 

    ```bash
    python manage.py createsuperuser
    ```

## Usage
How to run and use Django application.
1. Run the development server:

    ```bash
    python manage.py runserver
    ```

2. Access the application in your web browser at `http://127.0.0.1:8000/`.

3. Log in with credentials or register for a new account.

4. Explore the ToDo list features, create tasks, and manage your daily activities.

## frameworks used 

 Framework used in the project is Django. Django Python web framework that encourages rapid development and clean, pragmatic design. It provides built-in features for handling common web development tasks.

Here are the key frameworks and libraries mentioned or implied in the project:

## Django:
Django is a high-level Python web framework that follows the model-view-controller (MVC) architectural pattern.
It simplifies the development of web applications by providing a clean and pragmatic design.

## dj_database_url (used in settings):
dj_database_url is a utility library to parse database connection URLs. It is often used to configure Django to use a database specified by a URL.

## Google Fonts:
External link to Google Fonts ('https://fonts.googleapis.com/css2?family=Lato:ital,wght@1,300&family=Nunito+Sans:opsz,wght@6..12,200&display=swap') is used for custom fonts.

## Deployment

. Open project in Gitpod

 Open the terminal (View -> new Terminal).

. Navigate to the project's root directory.

. Run: git init

. git add .

. git commit -m "added commit message here"

. Created a new repository on GitHub:

. Copy the URL of the newly created GitHub repository.

. Go back to gitpod terminal.

. Link the local repo to the GitHub repo: git remote add origin GITHUB_REPOSITORY_URL

. Push the code to GitHub:

. Push code: git push -u origin main


## Heroku deployment

Deployed using Heroku using the following steps:

Was deployed using Heroku with the following steps:

Login to Heroku Create an account if necessary.

Click New in the Heroku dashboard and select ”Create new app.”

Write a name for the app and choose your region and click ”Create App.”

Added two build pack scripts : Python and Nodejs in that order where python is on top of Nodejs

Connected Heroku with GitHub account and the repository that is been working on

At the bottom, choose to either automatic deploment or manual deploment, if you set to automatic you every time you make changes with your code and commit, heroku updated the changes.


## 404page

## Testing 
I tested the website in different browsers chrome,firefox,safari and i confirm that the results are correct.

## Debug
In url task was not in the pathe so the port was not listing and I tad to add tasks in.
and in setting.py i had set DEBUG = development and the appliction was not functional but then i had to turn it to DEBUG = True.

## credit 
Basic structure of and understanding of the page development taken from Code Institute project walkthrogh Hello Django and i think therefore i blog and 
https://www.youtube.com/watch?v=llbtoQTt4qw  Dennis Ivy

Acknowledgments:
I would like to express my sincere gratitude to the following for their valuable contributions and support throughout the project: Code institute tutor Jason, Oisin, Joanne, my mentor Jubril, my fellow student Femi Ashuri. thank you so much for your support.

## Contribution
Contributions to this project are welcome. If you have any suggestions, improvements, or bug fixes, please open an issue or create a pull request. Your contributions will help me as person come to unsderstan and buld more skills and other people. the project is piblic to everyone.

Fork the repository.
Create a new branch for your contributions.
Make your changes and improvements.
Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
