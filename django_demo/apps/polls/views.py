import logging
from django.http import HttpResponse

logger = logging.getLogger('debug')


# Create your views here.
def index(request):
    logger.debug('polls app test.')
    return HttpResponse("Hello, world. You're at the polls index.")
