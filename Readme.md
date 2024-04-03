# Notes API

Simple API service for notes and boards management written with FastAPI.

Requirements

    Python 3.10 or higher
    poetry
    PostgreSQL

### Installation

1. Clone the repository to your local machine and navigate to the project directory.
   ```bash
    git clone https://github.com/Maksvell129/notes-api
    cd online-chat-backend
    ```
2. Install the project dependencies by running:
    ```bash
    poetry install
    ```
3. Create a `.env` file in the project root directory and add the following lines to it:
    ```
    DATABASE_NAME=mydatabase
    DATABASE_USER=myusername
    DATABASE_PASSWORD=mypassword
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    ```
4. Migrate the database by running:
    ```bash
    alembic upgrade head
    ```

### Running the Server

1. Go to src/:
    ```bash
    cd src
    ```
2. Start the development server by running:
    ```bash
    poetry run python -m main
    ```
3. Access the development server at `http://127.0.0.1:8000`.
