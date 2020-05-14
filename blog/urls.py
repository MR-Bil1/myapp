from django.urls import path
from .import views
from .views import postlistview, postdetailview , CreatePost ,UpdatePost,PostDelete,user_postlistview

urlpatterns = [
    path('',postlistview.as_view() , name='blog-home'),
    path('post/<int:pk>/update',UpdatePost.as_view() , name='post-update'),
    path('post/<int:pk>/',postdetailview.as_view() , name='post-detail'),
    path('post/<int:pk>/delete/',PostDelete.as_view() , name='post-delete'),
    path('user/<str:username>',user_postlistview.as_view() , name='user-posts'),
    path('about/',views.about,name='blog-about'),
    path('post/new/',CreatePost.as_view() , name='create-post')

]
