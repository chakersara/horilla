# Horilla Django Project

## Setup Instructions

1. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install dependencies**:
    ```bash
    pip3 install -r requirements.txt
    ```

3. **Apply migrations**:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

4. **Run the development server**:
    ```bash
    python3 manage.py runserver
    ```

5. **Access the application**:
    Open your browser and go to `http://127.0.0.1:8000/`
