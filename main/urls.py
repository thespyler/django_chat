from django.urls import path
from .views import *
urlpatterns = [
	path('', main),
	path('write/', write),
	path('delete/<int:get_id>', delete),
]