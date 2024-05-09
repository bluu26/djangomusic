from django.http import HttpResponse
from django.shortcuts import render, redirect

from mjuzik_app.models import Article, Band, GENRE_CHOICES, STATUS_CHOICES, Album


def index(request):
    return render(request, 'index.html')


def bands(request):
    bands = Band.objects.all()
    return render(request, 'bands.html', {'bands': bands})


def add_band(request):
    genre_n = GENRE_CHOICES
    if request.method == 'POST':

        name = request.POST.get('name')
        year = request.POST.get('year')
        still_active = request.POST.get('still_active') == 'on'
        genre = request.POST.get('genre')
        Band.objects.create(name=name, year=year, still_active=still_active, genre=genre)
    return render(request, 'add_band.html', {'genres': genre_n})


def delete_band(request, pk):
    band = Band.objects.get(id=pk)
    if request.method == "GET":
        return render(request, 'delete_band.html', {'band': band})
    else:
        action = request.POST['action']
        if action == 'YES':
            band.delete()
        return redirect('bands')


def update_band(request, pk):
    band = Band.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        still_active = request.POST.get('still_active') == 'on'
        genre = request.POST.get('genre')
        band.name = name
        band.year = year
        band.still_active = still_active
        band.genre = genre
        band.band_id = band
        band.save()
    return render(request, 'add_band.html', {'band': band})


def articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})


def add_article(request):
    status_n = STATUS_CHOICES
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        date_added = request.POST.get('date_added')
        status = request.POST.get('status')
        date_started = request.POST.get('date_started')
        date_ended = request.POST.get('date_ended')
        Article.objects.create(title=title, author=author, content=content,
                               status=status, date_added=date_added, date_ended=date_ended,
                               date_started=date_started)

    return render(request, 'add_article.html', {'status': status_n})


def albums(request):
    albums = Album.objects.all()
    return render(request, 'albums.html', {'albums': albums})


def add_album(request):
    if request.method == 'POST':
        album_title = request.POST.get('album_title')
        album_year = request.POST.get('album_year')
        rating = request.POST.get('rating')
        Album.objects.create(album_title=album_title, album_year=album_year, rating=rating)

    return render(request, 'add_album.html')











