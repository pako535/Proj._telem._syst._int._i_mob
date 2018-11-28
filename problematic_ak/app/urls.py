from django.urls import path, include
from .views import polls_view

urlpatterns = [
	path('', polls_view, name = 'polls'),

]