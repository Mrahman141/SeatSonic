from django.utils.translation import activate, get_language
from django.conf import settings


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)
        if language and language != get_language():
            activate(language)
        response = self.get_response(request)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, get_language())
        return response
