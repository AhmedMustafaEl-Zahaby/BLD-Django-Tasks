## Task

1. Feel free to remove any non-API views that we created from before
2. Create a class-based view at the path `/artists/` that returns a list of artists in JSON format for `GET` requests, the artist data should include the following fields.

```
{
    "id": ...
    "stage_name": ...
    "social_link": ...
}
```

3. The same view above should accept `POST` requests and accept all the fields on the artist model (excluding the id)
   - Include proper validation for each field as listed on the artist model:
     - this field is required
     - this field value already exists (for unique fields)
   - If the request passes the validation process, the given data should be used to create and save an artist instance
4. You may want to use a tool to make the HTTP requests and inspect them, I personally use [Postman](https://www.postman.com/) but there are other options like [curl](https://curl.se/) and [Insomnia](https://insomnia.rest/)
5. Feel free to write the API views yourself or use DRF's generic views.
6. Feel free to write the serializers yourself or use DRF's `ModelSerializer`
