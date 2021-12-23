
from django.urls import path
from .views import indexView

urlpatterns = [
    path('<programmer_id>/', indexView, name='index-view')
]
