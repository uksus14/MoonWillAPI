from django import http
import json

def HttpResponse(*args, **kwargs):
    kwargs["headers"] = kwargs.get("headers", {})|{"Access-Control-Allow-Origin": "https://uksus14.github.io"}
    return http.HttpResponse()

def JsonResponse(data: list[dict]|dict):
    return HttpResponse(json.dumps(data), headers={"Content-Type": "application/json"})