from django.urls import path
from apps.polls import views as polls_views

app_name = 'polls'
urlpatterns = [
    path('', polls_views.IndexView.as_view(), name='index'),
    path('<int:pk>/', polls_views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', polls_views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', polls_views.vote, name='vote'),
]
