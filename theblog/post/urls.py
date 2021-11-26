from django.urls import path
from django.urls.conf import include
from .views import PostPage, HomePage, AboutPage, ContactPage, Category_filter

# the urls
urlpatterns = [
    path('', HomePage, name='home'),
    path('posts/<str:category>/', Category_filter),
    path('about/', AboutPage, name='about'),
    path('contact/', ContactPage, name='contact'),
    path('post/<slug>/', PostPage.as_view(), name='post_detail'),
]
