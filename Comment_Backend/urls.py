from django.contrib import admin
from django.urls import path
from CommentApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/comment", views.CommentListView.as_view(), name="comments_list", ),
    path(
        "api/v1/comment/<int:pk>",
        views.CommentDetailView.as_view(),
        name="comment_detail",
    ),
]
