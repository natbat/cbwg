from django.http import HttpResponsePermanentRedirect


class CustomRedirectMiddleware:
    """
    Middleware to handle custom hard-coded redirects.
    Designed to run first in the middleware chain.
    """

    def __init__(self, get_response):
        self.get_response = get_response

        # Hard-coded redirects mapping (source path -> destination URL)
        self.redirects = {
            "/": "https://www.pacwestbats.org/cbwg",
            "/about/": "https://www.pacwestbats.org/about-cbwg",
            "/regional-groups/": "https://www.pacwestbats.org/california-regional-groups",
            "/resources/": "https://www.pacwestbats.org/cbwg-resources",
            "/contact/": "https://www.pacwestbats.org/contact-cbwg",
        }

    def __call__(self, request):
        path = request.path
        if not path.endswith("/"):
            path += "/"
        if path in self.redirects:
            return HttpResponsePermanentRedirect(self.redirects[path])
        return self.get_response(request)
