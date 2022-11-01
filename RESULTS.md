python manage.py shell

> > > from albums.models import _
> > > from artists.models import _
> > > Artist.objects.create(Stage_name = "Ahmed El-Zahaby" , Social_link = "https://www.facebook.com/1234")
> > > <Artist: Ahmed El-Zahaby>
> > > Artist.objects.create(Stage_name = "Afroto" , Social_link = "https://www.facebook.com/123445")
> > > <Artist: Afroto>
> > > Artist.objects.all()
> > > <QuerySet [<Artist: Afroto>, <Artist: Ahmed El-Zahaby>]>
> > > Artist.objects.order_by("Stage_name").all()
> > > <QuerySet [<Artist: Afroto>, <Artist: Ahmed El-Zahaby>]>
> > > Artist.objects.filter(Stage_name**startswith="a")
> > > <QuerySet [<Artist: Afroto>, <Artist: Ahmed El-Zahaby>]>
> > > ar1 = Artist.objects.get(id = 2)
> > > Album.objects.create(name = "Lights" , release_datetime = datetime(2023 , 12 , 1) , cost = 1345 , artist = ar1)
> > > <Album: Lights>
> > > album1 = Album(name = "Thunder" , release_datetime = datetime(2024 , 8 , 17) , cost = 12456 , artist = ar1)
> > > album1.save()
> > > Album.objects.order_by("release_datetime").all().first()
> > > <Album: Nights>
> > > Album.objects.filter(release_datetime**lt=datetime.today())
> > > <QuerySet [<Album: Nights>]>
> > > Album.objects.filter(release_datetime\_\_lte=datetime.today())
> > > <QuerySet [<Album: Nights>]>
> > > Album.objects.count()
> > > 3
> > > ar1.Album.all()
> > > <QuerySet [<Album: Lights>, <Album: Thunder>]>
> > > Album.objects.filter(artist_id = ar1.id)  
> > > <QuerySet [<Album: Lights>, <Album: Thunder>]>
> > > Album.objects.order_by("-cost","name")
> > > <QuerySet [<Album: Thunder>, <Album: Lights>, <Album: Nights>]>
