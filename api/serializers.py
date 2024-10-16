from django.core import serializers
import json

def dump_object(object: dict) -> dict:
    return {"pk": object["pk"]}|object["fields"]

def get_model(object: dict) -> str:
    return object["model"].partition(".")[-1]

def serialize(objects: list[dict]|dict) -> dict:
    data = json.loads(serializers.serialize("json", objects))
    if not data:
        return {}
    if isinstance(data, list):
        return {get_model(data[0]): [dump_object(object) for object in data]}
    if isinstance(data, dict):
        return {get_model(data): dump_object(data)}