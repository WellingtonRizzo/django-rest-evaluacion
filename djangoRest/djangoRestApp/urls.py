from django.urls import path
from .views import TransformDataView, NewDataListView

urlpatterns = [
    path('transform/', TransformDataView.as_view(), name='transform-data'),
    path('newdata/', NewDataListView.as_view(), name='new-data-list'),
]
