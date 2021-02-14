from django.urls import path
from apps.test_app import views as test_app_views

urlpatterns = [
    path('hello-world/', test_app_views.hello_world_view, name='hello_world'),
]
