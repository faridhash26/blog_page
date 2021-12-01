from django.urls import path
from .views import PostPage, HomePage, AboutPage, ContactPage, Category_filter, adding_new_category, all_category, category_edit, delete_tag_form, login_view, logout_view, myRegister

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
    path('logout/', logout_view, name='logout'),
    path('categorys/', all_category, name='category'),
    path('categoryedit/<int:cat_id>', category_edit, name='category_edit'),
    path('newcategory/', adding_new_category, name='newcategory'),
    path('deletecategory/<int:cat_id>', delete_tag_form, name="deletecategory")

]
