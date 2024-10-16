from django import http
class CustomHttpResponse(http.HttpResponse):
    def __init__(self, *args, **kwargs):
        kwargs["headers"] = kwargs.get("headers", {})
        kwargs["headers"]["Access-Control-Allow-Origin"] = "https://uksus14.github.io/"
        super().__init__(*args, **kwargs)

http.HttpResponse = CustomHttpResponse