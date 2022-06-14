# DRF IP Restrictions

A library that allows IP restrictions for views/endpoints in Django REST framework.

## Installation

1. Install using pip:

```
pip install git+https://github.com/anexia-it/drf-ip-restrictions@main
```

2. Add the library to your INSTALLED_APPS list.

```
INSTALLED_APPS = [
    ...
    'drf_ip_restrictions',
    ...
]
```

4. Override the allowed IP addresses your `settings.py` according to your needs:
```
# within settings.py

DRF_IP_RESTRICTION_SETTINGS = {
    "ALLOWED_IP_LIST": ["127.0.0.1"],
}
```

## Usage

Add the AllowedIpList class to any views / endpoints that should only provide access for the 
configured IP addresses, e.g. to restrict a view set:
```
# within views.py

class MyViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowedIpList,)
    ...
```

or to restrict only a single endpoint:
```
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
