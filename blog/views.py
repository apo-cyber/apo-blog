from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpRequest, JsonResponse


class IndexView(ListView):
    template_name = 'index.html'
    model = BlogPost
    context_object_name = 'orderby_records'
    queryset = BlogPost.objects.order_by('-posted_at')
    paginate_by = 4


class BlogDetail(DetailView):
    template_name = 'post.html'
    model = BlogPost


class MountainView(ListView):
    template_name = 'mountain_list.html'
    model = BlogPost
    context_object_name = 'mountain_records'
    queryset = BlogPost.objects.filter(
        category='Mountain').order_by('-posted_at')
    paginate_by = 2


class FlowerView(ListView):
    template_name = 'flower_list.html'
    model = BlogPost
    context_object_name = 'flower_records'
    queryset = BlogPost.objects.filter(
        category='Flower').order_by('-posted_at')
    paginate_by = 2


class CatView(ListView):
    template_name = 'cat_list.html'
    model = BlogPost
    context_object_name = 'cat_records'
    queryset = BlogPost.objects.filter(category='Cat').order_by('-posted_at')
    paginate_by = 2


class DailylifeView(ListView):
    template_name = 'dailylife_list.html'
    model = BlogPost
    context_object_name = 'dailylife_records'
    queryset = BlogPost.objects.filter(
        category='Dailylife').order_by('-posted_at')
    paginate_by = 2


def toggle_like(request: HttpRequest, pk: int):
    post = get_object_or_404(BlogPost, pk=pk)
    liked = request.session.get('liked', [])

    if pk in liked:
        post.good = max(0, post.good - 1)
        liked.remove(pk)
        is_liked = False
    else:
        post.good += 1
        liked.append(pk)
        is_liked = True

    post.save()
    request.session['liked'] = liked

    # AJAXリクエストの場合はJSONで返す
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'good': post.good, 'is_liked': is_liked})

    return redirect(request.META.get('HTTP_REFERER', 'index'))
