from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseBadRequest
from api.models import Section
from api.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def section_view(request: WSGIRequest, pk: int=None):
    if request.method == "GET":
        return HttpResponse(serialize(Section.objects.all()), content_type="application/json")
    elif request.method == "PUT":
        Section.objects.create(title=request.GET.get('title'))
    elif request.method == "DELETE":
        Section.objects.get(pk=pk).delete()
    else:
        return HttpResponseBadRequest()
    return HttpResponse()