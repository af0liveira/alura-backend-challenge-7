# Alura Challenge -- Backend 7

This project has been developed within the [**7th Edition of the Alura Back-End Challenge**](https://www.alura.com.br/challenges/back-end-7?host=https://cursos.alura.com.br).

The challenge is to build an API that will be integrated with the frontend to provide information and resources from a database related to possible travel destinations, displaying photos and eye-catching text that instigates the user to want to visit that destination.

In addition, the API will provide resources on testimonials from other travelers and use AI to automatically generate attractive descriptions of destinations whenever necessary.

The conception of the frontend (not part of the this challenge) is available [here](https://www.figma.com/proto/1qD4hmpnvxoeHRC1cbWKgR/Angular_-Componentização-e-Design-com-Angular-Material-_-Jornada-Milhas?type=design&node-id=4-6408&scaling=min-zoom&page-id=0%3A1).

The duration of the challenge is four weeks, with implementation requirements being informed on a weekly basis.

## Development stack

The API has been developed using Python and Django REST Framework (DRF).
This combination provides all the necessary components for the development of a RESTful API.

The AI integration has been implemented using the [OpenAI API](https://platform.openai.com/docs/introduction).

## How to run the API

### Setting up the virtual environment

The virtual environment used in the implementation of the API is specified in `requirements.txt`.
You can use the following shell commands to replicate the environment:

```bash
python3 -m venv ./venv           # environment creation
source ./venv/bin/activate       # environment activation 
pip install -r requirements.txt  # installation of dependencies
```

### Specifying authentication keys

For privacy reasons, authentication keys are not stored in the repository.
Instead, they must be specified locally, in a file named `.env`, located in the root directory of the API code.
The `.env` file should look like this:

```sh
# Content of the file '.env'

SECRET_KEY = '<django-secret-key>'
OPENAI_API_KEY = '<openai-api-secret>'
```

You can generate your own `SECRET_KEY` value with the command

```sh
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' 
```

For the `OPENAI_API_KEY`, you will need an OpenAI account (more info [here](https://openai.com/blog/openai-api)).
However, this is only needed for the AI features of the API.

### Starting the database

Once you have everything configured and the virtual environment activated, run the following commands to create the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Running the API server

Finally, you can start the server locally with the command

```bash
python manage.py runserver [port]  # default port: 8000
```

The API will be accessible at `http://localhost:port`.
If `port` is not provided, it will default to `8000`.

### Creating a superuser for the API

The API will require an authenticated user for methods other than GET, HEAD or
OPTIONS.
Regular users can be created with Django Admin.
However, you will need to be authenticated as superuser to do so.

In order to create a superuser for the API, you can run the command

```bash
python manage.py createsuperuser  # start superuser creation
```

and follow the instructions.

### Accessing the Django Admin interface

The Django Admin interface can be used for managing users and the database.
By default, it is accessible via the `/admin/` endpoint.
However, in this project this endpoint leads to a fake login page (honeypot) mimicking Django Admin.

The actual Django Admin interface can be accessed via the endpoint `/api-cockpit/` -- e.g., `http://localhost:8000/api-cockpit/` if using the default server.

## Automated tests

The automated test suite can be executed with the command

```sh
python manage.py test
```

## API documentation

Once the server is up an running, the auto-generated documentation can be accessed via on the following URLs:

- `http://<domain>/swagger`
- `http://<domain>/doc`

---
