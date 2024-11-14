from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class RequestProcessMiddleware(BaseHTTPMiddleware):
    def __init__(
            self,
            app
    ):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        # do something with the request object, for example
        # TODO: Implementar lógica para carregar o contexto da requisição (database, cache, etc)
        print(">>>>> Load context before process request")
        headers = request.headers.items();
        print(headers)
        # process the request and get the response    
        response = await call_next(request)
        print("Releas context after process request <<<<<")
        
        return response