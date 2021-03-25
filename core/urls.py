from django.urls import path

from .views import IndexView, ErrorView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('404/', ErrorView.as_view(), name='404')
]
