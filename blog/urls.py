from django.urls import include, path

from . import views
from .feeds import AtomSiteNewsFeed, LatestPostsFeed

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    path("blog/create", views.PostView.as_view(), name="create_post"),
    path("blog/update/<int:pk>/", views.PostUpdateView.as_view(), name="update_post"),
    path("blog/delete/<int:pk>/", views.PostDeleteView.as_view(), name="delete_post"),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
]
