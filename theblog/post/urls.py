from django.urls import path
from .views import PostPage, HomePage, AboutPage, ContactPage, Category_filter, login_view, logout_view, myRegister

# the urls
app_name = 'post'
urlpatterns = [
    path('', HomePage, name='home'),
    path('posts/<str:category>/', Category_filter),
    path('about/', AboutPage, name='about'),
    path('contact/', ContactPage, name='contact'),
    path('post/<slug>/', PostPage.as_view(), name='post_detail'),
    path('login/', login_view, name="login"),
    path('register/', myRegister, name="register"),
    path('logout/', logout_view, name='logout')
]
