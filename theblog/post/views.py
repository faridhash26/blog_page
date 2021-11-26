from django.shortcuts import get_object_or_404, render, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView

# from django.http import HttpResponse
from .models import Post, Comment, Category
# Create your views here.


def add_variable_to_context(req):
    return {'categorys': Category.objects.all()}


def HomePage(req):
    posts = Post.objects.values(
        'slug', 'title', 'short_description', 'wirter__username', 'create_on')

    return render(req, 'pages/index.html', {'posts': list(posts)})


def Category_filter(req, category):
    posts = Post.objects.filter(category__title=category).values(
        'slug', 'title', 'short_description', 'wirter__username', 'create_on')
    return render(req, 'pages/index.html', {'posts': list(posts)})


def AboutPage(req):
    return render(req, 'pages/about.html')


def ContactPage(req):
    return render(req, 'pages/contact.html')


# def PostPage(req, slug):
#     print(id)
#     # post = Post.objects.get(id=id)
#     return render(req, 'pages/post.html')

class PostPage(DetailView):
    template_name = "pages/post.html"
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all post's comments
        context['comments'] = Comment.objects.filter(
            post=kwargs['object'].id)

        return context
