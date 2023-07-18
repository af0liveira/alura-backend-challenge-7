# Jornada Milhas

This project is being developed as part of the **7th Alura Backend Challenge**.
The goal is to develop the API to integrate to the frontend of a travel website,
which displays photos and an enticing information about travel destinations.
Moreover, the site will show statements made by other travelers about the
destination.

## Virtual Development Environment (VDE)

A virtual development environment (VDE) is used in the development of this project to ensure compatibility across local repositories.
The management of the VDE using _conda_ is described below.

### Creating the VDE with conda

From the project's root directory, the VDE can be created with the command

```sh
conda create --prefix ./venv --file environment.yml
```

> It might be necessary to append `conda-forge` to your channels list
> wit the command `conda config --append channels conda-forge`

Once the VDE has been created, it can be activated with

```sh
conda activate ./venv
```

### Updating the VDE

If you install or update packages in the VDE, you should update the `envornment.yml` file with the command

```sh
conda list -e > environment.yml
```

---
