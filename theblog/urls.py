from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AuthorDetailView, \
    AddPostView, UpdatePostView, DeletePostView, \
    AddCategoryView, CategoryView, ContactView, \
    CategoryListView, LikeView, AddCommentView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_detail"),
    path('author/<int:pk>', AuthorDetailView.as_view(), name="author_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/<int:pk>/edit', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:choices>/', CategoryView, name="category"),
    path('contact/', ContactView, name="contact"),
    path('category_list/', CategoryListView, name="category_list"),
    # path('favorites/<str:user>', FavoriteView(), name="favorites"),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
]
