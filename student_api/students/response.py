from rest_framework.response import Response

def custom_response(data=None, message=None, status_code=200):
    if data is None:
        data = {}
    return Response({
        "status":status_code,
        "message": message,
        "data": data,
    }, status=status_code)
