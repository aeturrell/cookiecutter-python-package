# cookiecutter-python-package

A modern Python package cookiecutter.

## Features

- Nox for isolated testing
- Modern Python dependency management with uv
- pytest for testing
- Documentation website with Quarto + GitHub pages
- Automatic code documentation with Quartodoc
- Code formatting with ruff (including formatting and import sorting)
- Git pre-commit hooks for code quality
  - Ruff lint/format/sort imports
  - check for added large files
  - check TOML
  - check YAML
  - end of file fixer
  - trailing whitespace trimmer
  - nbstripout
  - pydoclint
- Continuous Integration with GitHub Actions
  - tests with pytest + nox (cross-platform)
  - code coverage
  - release labeler
  - PyPI publishing
  - Docs build and deploy

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
