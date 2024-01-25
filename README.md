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
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (login, register, logout)
- Create, update, and delete tasks
- Mark tasks as complete
- Search functionality to filter tasks
- Clean and responsive user interface

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

## Contributing

Contributions are welcome! If you find a bug or have an enhancement in mind, please open an issue or submit a pull request following the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
