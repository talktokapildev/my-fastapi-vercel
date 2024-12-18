# api/index.py
from main import app
from mangum import Mangum

handler = Mangum(app)

def main(request):
    return handler(request)
