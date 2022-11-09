## Task

1. Under each app that we have, create a `tests` directory and don't forget `__init__.py`
2. If the app has endpoints, create a file `tests/test_endpoints.py` or `tests/test_views.py`
3. Create a global fixture `auth_client` that returns a function, if that function is passed a user instance, it'll return an instance of DRF's `APIClient` authenticated by that user instance, otherwise, it'll return an instance of `APIClient` authenticated by an arbitrary user instance. example:

```
def test_something(api_client):
    client = api_client(user)
    # or
    client = api_client()


    client.get(url)
```

4. For each endpoint, test the following:
   - If the view has permission classes, test making requests that will obey and disobey the permissions, For example, if a view has `IsAuthenticatedOrReadOnly` permission class, test that making a write and non-authenticated request will return `403 Forbidden` status code
   - If the view is expecting a certain set of required fields, test that making a request with one or more missing fields will return `400` status code and a proper error message
   - If a view is expected to return a set of fields, test that these fields are indeed returned, and that their values match what you expect. For example, if I make a request to `/users/1` I expect that the data returned will be that that of the user whose id is 1
