## Task-1

For this task and the following ones, we'll try to build a music platform on which artists can sign up
and put up their albums for sale

1. Create a personal repository on GitLab called `django-training`
2. Create a Django project under the repository called `musicplatform`
3. Create an app `artists`
4. In `artists` Create an `Artist` model with the following fields (make the right assumptions)
   - Stage name
     - required
     - unique
     - must be used as the model's default ordering
   - Social link field
     - This field is to store each artist's social media profile (e.g. https://www.instagram.com/drake/)
     - What is a suitable field for this type of data?
     - This field is optional, but it shouldn't be null ([why?](https://docs.djangoproject.com/en/4.0/ref/models/fields/#null))
5. Create an app `albums`
6. In `albums`, Create an `Album` model with the following fields (you might think it's an overkill creating a whole app for one model, for the sake of this practice we could have added the `Album` model to the `artists` app, but in the real world, think of how your app will scale if there are multiple types of artists, each with its own model, for example `GuestArtist`, and multiple types of albums, each with its own model)
   - an artist can have `0 or many` albums, an album must have an artist associated with it
   - name (if name is not provided, it should be called `New Album`)
   - creation datetime (the date when the album instance is created and stored in the database) (hint: respect the timezone)
   - release datetime **which cannot be empty** (hint: respect the timezone)
   - cost
     - required
     - use what you find suitable between `FloatField` and `DecimalField`
7. Create a `RESULTS.md` under `musicplatform/`
8. using `manage.py shell` (type the queries you used and their results in `RESULTS.md`):
   - create some artists
   - list down all artists
   - list down all artists sorted by name
   - list down all artists whose name starts with `a`
   - in 2 different ways, create some albums and assign them to any artists (hint: use `objects` manager and use the related object reference)
   - get the latest released album
   - get all albums released before today
   - get all albums released today or before but not after today
   - count the total number of albums (hint: count in an optimized manner)
   - in 2 different ways, for each artist, list down all of his/her albums (hint: use `objects` manager and use the related object reference)
   - list down all albums ordered by cost then by name (cost has the higher priority)
