class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # Lógica antes de la vista
        print(f"Solicitud recibida: {request.method} {request.path}")
        response = self.get_response(request)
        # Lógica después de la vista
        return response