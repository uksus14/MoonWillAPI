from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponseBadRequest
from api.models import Section
from api.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def section_view(request: WSGIRequest, pk: int=None):
    if request.method == "GET":
        return JsonResponse(serialize(Section.objects.all()))
    elif request.method == "PUT":
        Section.objects.create(title=request.GET.get('title'))
    elif request.method == "DELETE":
        Section.objects.get(pk=pk).delete()
    else:
        return HttpResponseBadRequest()
    return JsonResponse({})