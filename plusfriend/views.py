from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def keyboard(request):

    if request.method == 'GET':
        ret = { "type" : "buttons",
                "buttons" : ["불 켜기", "불 끄기", "리셋"]
                }
        return HttpResponse(json.dumps(ret))

@csrf_exempt
def message(request):
    #print(request.body)
    ret  = {
            'message':{
                'text':'정상적으로 작동 하였습니다!',
                },
            'keyboard':{
                'type':'buttons',
                'buttons':["불 켜기", "불 끄기", "리셋"]
                }
            }

    return HttpResponse(json.dumps(ret))

