from . import views
from django.urls import path


urlpatterns = [
    path('', views.PerformerListView.as_view(), name='all_performers')
]
