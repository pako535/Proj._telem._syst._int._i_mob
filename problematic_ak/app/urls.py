from django.urls import path, include
from .views import polls_view

urlpatterns = [
	path('polls', polls_view, name = 'polls'),

]