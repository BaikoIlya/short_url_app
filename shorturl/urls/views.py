import time
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from hashids import Hashids
from .forms import UrlForm
from .models import Url


User = get_user_model()


def url_create(request):
    form = UrlForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        hashids = Hashids()
        hashid = hashids.encode(int(time.time()))
        answer = 'http://127.0.0.1:8000/' + hashid + '/'
        instance.short_url = hashid
        instance.save()
        context = {
            'form': form,
            'answer': answer
        }
        return render(request, 'urls/main.html', context)
    return render(request, 'urls/main.html', {'form': form})


def profile(request, username):
    auth = User.objects.get(username=username)
    url_list = Url.objects.filter(author=auth.pk)
    return render(request, 'urls/users_urls.html', {'url_list': url_list})


def redirect_outside(request, slug):
    cur_short_url = slug
    cur_obj = get_object_or_404(Url, short_url=cur_short_url)
    return redirect(cur_obj.long_url)
