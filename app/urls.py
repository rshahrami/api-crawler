from django.urls import path
from app.views import GetAllData, UpdateData, PostData, SearchData, DeleteData, \
                    FilterMultiFieldData, SearchMultiFieldData, SearchDataDate

urlpatterns = [
    path('get-all-data/', GetAllData.as_view()),
    path('update-data/<int:pk>/', UpdateData.as_view()),
    path('post-data/', PostData.as_view()),
    path('search-data/', SearchData.as_view()),
    path('search-data-date/', SearchDataDate.as_view()),
    path('delete-data/<int:pk>', DeleteData.as_view()),
    path('filter-multi-data/', FilterMultiFieldData.as_view()),
    path('search-multi-data/', SearchMultiFieldData.as_view()),
]