from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponse
from api.models import Section
from api.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

def OptionsResponse():
    return HttpResponse(headers={"Allow": "OPTIONS, GET, HEAD, POST", "Access-Control-Allow-Origin": "https://uksus14.github.io"})

@csrf_exempt
def section_view(request: WSGIRequest, pk: int=None):
    if request.method == "OPTIONS":
        return OptionsResponse()
    if request.method == "GET":
        return JsonResponse(serialize(Section.objects.all()))
    elif request.method == "PUT":
        Section.objects.create(title=request.GET.get('title'))
    elif request.method == "DELETE":
        Section.objects.get(pk=pk).delete()
    return HttpResponse()