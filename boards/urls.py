from django.urls import path, reverse_lazy
from django.contrib import admin

from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.BoardListView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('<int:pk>/', views.TopicListView.as_view(), name='board_topics'),
    path('<int:pk>/new/', views.new_topic, name='new_topic'),
    path('<int:pk>/topics/<int:topic_pk>/', views.PostListView.as_view(), name='topic_posts'),
    path('<int:pk>/topics/<int:topic_pk>/reply/', views.reply_topic, name='reply_topic'),
    # path('<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/', views.PostUpdateView.as_view(template_name='edit_post.html', success_url=reverse_lazy('boards:topic_posts')), name='edit_post'),
    path('<int:pk>/topics/<int:topic_pk>/posts/<int:post_pk>/edit/',
         views.PostUpdateView.as_view(),
         name='edit_post')
]