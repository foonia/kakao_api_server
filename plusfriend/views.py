from django.shortcuts import render
from django.http import HttpResponse
import json

def keyboard(request):

    if request.method == 'GET':
        res = {
                "type" : "buttons",
                "buttons" : ["선택 1", "선택 2", "선택 3"]
                }
        return HttpResponse(json.dumps(res))


