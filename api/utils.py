from django.http import HttpResponse
import json

def JsonResponse(data: list[dict]|dict):
    return HttpResponse(json.dumps(data), headers={"Content-Type": "application/json", "Access-Control-Allow-Origin": "https://uksus14.github.io/"})