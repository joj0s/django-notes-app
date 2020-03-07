# Basic Note keeping app using Django

## How to setup:
1. Clone the repository and navigate into it.
2. Run `python3 -m venv venv` . This creates a virtual environment so that you can install the project dependecies locally.
3. Run `. venv/bin/activate` . This activates the virtual environment.
4. Run `pip install -r requirements.txt`. This installs the project dependencies.
5. Run `python3 manage.py migrate`. This will apply the necessary database migrations. It has to be done locally since it uses sqlite as a development database.
5. Use `python3 manage.py runserver` to start a local server