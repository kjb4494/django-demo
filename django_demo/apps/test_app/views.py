from django.http import HttpResponse


# Create your views here.
def hello_world_view(request):
    return HttpResponse("Hello world")
