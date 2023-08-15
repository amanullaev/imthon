from django.urls import path
from .views import *


urlpatterns = [
    path('', All_Create_News.as_view()),
    path('category/', All_Create_Category.as_view()),
    path('get_by_index_news/<int:id>', Detail_News.as_view()),
    path('update_news/<int:id>', UpdateNews.as_view()),
    path('delete_news/<int:id>', Detail_News.as_view()),
    path('get_by_index_category/<int:id>', Detail_Category.as_view()),
    path('update_category/<int:id>', UpdateCategory.as_view()),
    path('delete_category/<int:id>', DeleteCategory.as_view()),
    path('get_by_category/<int:id>/', Get_News_By_Category.as_view())
]