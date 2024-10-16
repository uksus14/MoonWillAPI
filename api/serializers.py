from django.core import serializers
import json

def dump_object(object: dict) -> dict:
    return {"pk": object["pk"]}|object["fields"]

def get_model(object: dict) -> str:
    return object["model"].partition(".")[-1]

def serialize(objects: list[dict]|dict) -> list[dict]|dict:
    data = json.loads(serializers.serialize("json", objects))
    if not data:
        return {}
    if isinstance(data, list):
        return [dump_object(object) for object in data]
    if isinstance(data, dict):
        return dump_object(data)