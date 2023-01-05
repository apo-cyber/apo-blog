from django.views.generic import ListView, DetailView
from .models import BlogPost
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect


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


def goodfunc(request, pk):
    object = get_object_or_404(BlogPost, pk=pk)
    object.good += 1
    object.save()
    return redirect('blog:index')
