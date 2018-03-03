from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json, requests

def keyboard(request):

    if request.method == 'GET':
        ret = { "type" : "buttons",
                "buttons" : ["불 켜기", "불 끄기", "리셋"]
                }
        return HttpResponse(json.dumps(ret, ensure_ascii=False))

@csrf_exempt
def message(request):
    data = json.loads(request.body.decode('utf-8'))

    ret  = {
            'message':{
                'text':'*{}* 정상적으로 작동 하였습니다!'.format(data['content']),
                },
            'keyboard':{
                'type':'buttons',
                'buttons':["불 켜기", "불 끄기", "리셋"]
                }
            }

    return HttpResponse(json.dumps(ret))

