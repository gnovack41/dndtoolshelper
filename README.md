# Django REST API Template

A [repository template](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template) for a Django REST framework API.

## Setup

### Prerequisites

* Python (3.12)
* [Pipenv](https://pipenv.pypa.io/)
* [PostgreSQL](https://www.postgresql.org)

### Installation

Ensure that you are running these commands from within a virtualenv.

1. Create a PostgreSQL database for the app

    ```shell
   createdb database_name
    ```

2. Configure project environment variables (`.env` files supported)

3. Install dependencies with Pipenv

    ```shell
    pipenv install --dev
    ```

4. Apply migrations

    ```shell
   python manage.py migrate
    ```

5. Start the server

    ```shell
   python manage.py runserver 
   ```
