from django.shortcuts import render


def films_list(request):
    films = News_post.objects.all()
    return render(request, 'film_list.html')