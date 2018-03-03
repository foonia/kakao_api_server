from functools import wraps
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
import json

User = get_user_model()
def bot(view_fn):
    @wraps(view_fn)
    @csrf_exempt
    def wrap(request, *args, **kwargs):
        if request.method == 'POST':
            print(request.body)
            request.JSON = json.loads(request.body.decode('utf-8'))
            # test varialbe
            request.TEMP = request.JSON
        else:
            request.JSON = {}
            return JsonResponse(view_fn(request, *args, **kwargs) or {})

        user_key = request.JSON.get('user_key')

        try:
            request.user = User.objects.get(username=user_key)
        except User.DoesNotExist:
            request.user = User.objects.create(username=user_key)

        return JsonResponse(view_fn(request, *args, **kwargs) or {})
    return wrap

