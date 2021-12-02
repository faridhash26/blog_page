from .forms import LoginForm, PostModelForm, UserRegister, CategoryModelForm
from .models import Post, Comment, Category
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.http import HttpResponse
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


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get(
                'username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                messages.success(request, f'خوش امدید {user}')
                return redirect(reverse('post:userdashbord'))
    else:
        form = LoginForm()
    return render(request, 'acounts/login.html', {'form': form})


def myRegister(request):
    form = UserRegister(None or request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])

    return render(request, 'acounts/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect("post:home")


def all_category(req):
    categorys = Category.objects.all()

    return render(req, 'pages/category.html', {'categorys': list(categorys)})


def category_edit(request, cat_id):
    category = get_object_or_404(Category, id=cat_id)
    form = CategoryModelForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect(reverse('post:category'))

    return render(request, 'forms/edit_category.html', {'form': form})


def adding_new_category(request):
    form = CategoryModelForm()
    if request.method == "POST":
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('post:category'))

    return render(request, 'forms/edit_category.html', {'form': form})


def delete_category_form(request, cat_id):

    category = get_object_or_404(Category, id=cat_id)

    form = CategoryModelForm(instance=category)
    if request.method == "POST":
        category.delete()
        return redirect(reverse('post:category'))

    return render(request, 'forms/delete_category_form.html', {'form': form, 'category': category})


@login_required(login_url="/login/")
def admin_dashbord(request):
    posts = Post.objects.filter(wirter__id=request.user.id).values(
        'id', 'slug', 'title', 'short_description', 'wirter__username', 'create_on')

    return render(request, 'pages/dashboard.html', {"posts": list(posts)})


@login_required(login_url="/login/")
def new_post(request):
    form = PostModelForm()
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.wirter = request.user
            post.save()
            return redirect(reverse('post:userdashbord'))
    return render(request, 'forms/new_post.html', {'form': form})


@login_required(login_url="/login/")
def post_delete(request, postid):

    user_post = get_object_or_404(Post, id=postid)

    form = PostModelForm(instance=user_post)
    if request.method == "POST":
        user_post.delete()
        return redirect(reverse('post:userdashbord'))

    return render(request, 'forms/delete_post.html', {'form': form, 'post': user_post})


@login_required(login_url="/login/")
def post_edit(request, postid):
    thepost = get_object_or_404(Post, id=postid)
    form = PostModelForm(request.POST or None, instance=thepost)
    if form.is_valid():
        form.save()
        return redirect(reverse('post:userdashbord'))

    return render(request, 'forms/edit_post.html', {'form': form})
