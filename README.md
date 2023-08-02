# Alura Challenge Backend 7

This project is being developed as part of the **7th Alura Backend Challenge**.
The goal is to develop the API to integrate to the frontend of a travel website,
which displays photos and an enticing information about travel destinations.
Moreover, the site will show statements made by other travelers about the
destination.

## Environment variables

Environment variables specific to this project should be declared in the `.env` file.
The goal is to keep sensitive information away from the development repository.

The following is a example of `.env` with the declaration of `SECRET_KEY` environment variable:

```sh
# Environment variables

SECRET_KEY = '<django-secret-key>'
```

To generate a random secret key from the command line, you can use the command

```sh
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' 
```

## Virtual Development Environment (VDE)

A virtual development environment (VDE) is used in the development of this project to ensure compatibility across local repositories.
The management of the VDE using _venv_ is described below.

### Creating the VDE

From the project's root directory, the VDE can be created with the command

```sh
python3 -m venv ./venv
```

Once the VDE has been created, it must be activated.
If you are using bash or zsh, you can use the command

```sh
source ./venv/bin/activate
```

For other shells, look for the appropriate activation script in `./venv/bin`

Once the virtual environment is activated, install the dependencies with

```sh
pip install -r requirements.txt
```

If all went well, you should be able to start the Django server with

```sh
python manage.py runserver
```

### Installing new dependencies

New dependencies should be installed using `pip`:

```sh
pip install <package>==<version>
```

> **Warning**
>
> If the package version is not specified, `pip` will try to install the latest version available, which can result in all previously installed packages being updated.
> In order to force `pip` to find the newest package that matches the specs in `requirements.txt`, you should use the command

```sh
pip install -c requirements.txt <package>
```

### Updating the VDE requirements

The virtual environment dependencies are stored in `requirements.txt`.
Every time a dependency is installed or updated, `requirements.txt` must be updated manually.
This can be done with the command

```sh
pip freeze > requirements.txt
```



---
