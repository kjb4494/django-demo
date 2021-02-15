import logging
from django.http import HttpResponse

logger = logging.getLogger('debug')


# Create your views here.
def hello_world_view(request):
    logger.debug('This is hello world log.')
    return HttpResponse("Hello world")
