# cookiecutter-python-package

A modern Python package cookiecutter.

## Features

- Nox for isolated testing
- Modern Python dependency management with uv
- Pre-configured testing with pytest
- Automatic documentation with Quarto
- Code formatting with ruff
- Git pre-commit hooks for code quality
- Continuous Integration with GitHub Actions

## Prerequisites

- the Python [package manager uv](https://docs.astral.sh/uv/)
- `cookiecutter` package (link [here](https://github.com/cookiecutter/cookiecutter))
- an installation of [Quarto](https://quarto.org/)

## How to use this template

To install cookiecutter, which will help you populate the template with details like your project's name, run

```bash
uv tool install cookiecutter
```

To create a new project folder based on this cookie cutter:

```bash
uv tool run cookiecutter https://github.com/aeturrell/cookiecutter-python-package.git
```

The new project folder will appear within the folder you ran the command in.
