"""
{{cookiecutter.project_name}}
------------------------------------
{{cookiecutter.project_description}}
"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("{{ccookiecutter.project_name}}")
except PackageNotFoundError:
    __version__ = "unknown"

