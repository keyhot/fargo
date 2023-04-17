from django.http import HttpResponsePermanentRedirect


class HttpsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.is_secure():
            url = request.build_absolute_uri(request.get_full_path())
            if url.startswith("http://www."):
                secure_url = url.replace("http://www.", "https://www.")
            elif url.startswith("https://fargo"):
                secure_url = url.replace("https://", "https://www.")
            elif url.startswith("http://fargo"):
                secure_url = url.replace("http://", "https://www.")
            else:
                secure_url = url.replace("http://", "https://")
            return HttpResponsePermanentRedirect(secure_url)
        response = self.get_response(request)
        return response