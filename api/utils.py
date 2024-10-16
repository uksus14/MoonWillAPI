from django import http
import json

def HttpResponse(*args, **kwargs):
    kwargs["headers"] = kwargs.get("headers", {})|{"Access-Control-Allow-Origin": "https://uksus14.github.io", "Access-Control-Allow-Methods": "OPTIONS, GET, PUT, POST, DELETE, PATCH"}
    return http.HttpResponse(*args, **kwargs)

def JsonResponse(data: list[dict]|dict):
    return HttpResponse(json.dumps(data), headers={"Content-Type": "application/json"})