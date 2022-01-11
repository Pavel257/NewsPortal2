from django.urls import path
from .views import *

urlpatterns = [
    # path('', AuthorsList.as_view()),
    # path('<int:pk>', AuthorsDetail.as_view()),
    # path('', CommentsList.as_view()),
    path('', PostsList.as_view()),
    path('<int:pk>', PostsDetail.as_view()),
#     path('<int:pk>', CategorysDetail.as_view()),
#     path('', PostCategorysList.as_view()),
#     path('<int:pk>', PostCategorysDetail.as_view()),

    # path('<int:pk>', NewsDetail.as_view()),
]