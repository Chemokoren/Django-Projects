from django.urls import path
from .views import contact, snippet_detail, formset_example

urlpatterns = [
    path('', contact),
    path('snippet/', snippet_detail),
    path('formset/', formset_example),

]
