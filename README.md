# DRF IP Restrictions

[![PyPI version](https://img.shields.io/pypi/v/drf-ip-restrictions.svg)](https://pypi.org/project/drf-ip-restrictions/)
[![Run linter and tests](https://github.com/anexia/drf-ip-restrictions/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/anexia/drf-ip-restrictions/actions/workflows/test.yml)
[![Codecov](https://img.shields.io/codecov/c/gh/anexia/drf-ip-restrictions)](https://codecov.io/gh/anexia/drf-ip-restrictions)

A library that allows IP restrictions for views/endpoints in Django REST framework.

## Installation

1. Install using pip:

```sh
pip install drf-ip-restrictions
```

2. Add the library to your INSTALLED_APPS list.

```python
INSTALLED_APPS = [
    ...
    'drf_ip_restrictions',
    ...
]
```

4. Override the allowed IP addresses your `settings.py` according to your needs:

```python
# within settings.py

DRF_IP_RESTRICTION_SETTINGS = {
    "ALLOWED_IP_LIST": ["127.0.0.1"],
}
```

## Usage

Add the AllowedIpList class to any views / endpoints that should only provide access for the
configured IP addresses, e.g. to restrict a view set:

```python
# within views.py

class MyViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowedIpList,)
    ...
```

or to restrict only a single action:

```python
# within views.py

class MyViewSet(viewsets.ModelViewSet):
    ...

    @action(
        detail=False,
        methods=["get"],
        http_method_names=["get"],
        authentication_classes=[],
        permission_classes=[AllowedIpList],  # <-- this is the important part for IP restrictions to work
        url_path=r"my-method",
    )
    def my_method(self, request, *args, **kwargs):
        # do stuff and return rest_framework.response.Response in the end
```
## Auto-formatter setup
We use ruff (https://github.com/astral-sh/ruff) for local auto-formatting and for linting in the CI pipeline.
The pre-commit framework (https://pre-commit.com) provides GIT hooks for these tools, so they are automatically applied
before every commit.

Steps to activate:
* Install the pre-commit framework: `pip install pre-commit` (for alternative installation options see https://pre-commit.com/#install)
* Activate the framework (from the root directory of the repository): `pre-commit install`

Hint: You can also run the formatters manually at any time with the following command: `pre-commit run --all-files`


## Django Compatibility Matrix

If your project uses an older verison of Django or Django Rest Framework, you can choose an older version of this project.

| This Project | Python Version              | Django Version | Django Rest Framework  |
|--------------|-----------------------------|----------------|------------------------|
| 1.1.*        | 3.9, 3.10, 3.11, 3.12. 3.13 | 4.2, 5.0, 5.1  | 3.12, 3.13, 3.14, 3.15 |
| 1.0.*        | 3.7, 3.8, 3.9, 3.10         | 3.2, 4.0       | 3.12, 3.13             |
