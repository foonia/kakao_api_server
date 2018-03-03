from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .decorators import bot
from .models import Post
import json, requests

#def keyboard(request):
#    if request.method == 'GET':
#        ret = { "type" : "buttons",
#                "buttons" : ["불 켜기", "불 끄기", "리셋"]
#                }
#        return HttpResponse(json.dumps(ret, ensure_ascii=False))


#@csrf_exempt
#def message(request):
#    ret  = {
#            'message':{
#                'text':'*{}* 정상적으로 작동 하였습니다!'.format(data['content']),
#                },
#            'keyboard':{
#                'type':'buttons',
#                'buttons':["불 켜기", "불 끄기", "리셋"]
#                }
#            }
#
#    return HttpResponse(json.dumps(ret))

@bot
def keyboard(request):
    return {'type':'text'} 


@bot
def message(request):
    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content']

    if type == 'photo':
        pass
    else:
        post = Post.objects.create(user=request.user, message=content)
        ret  = {
                'message':{
                    'text':'-{}-\n저장되었습니다.'.format(content)
                    }
                }
        return ret 
    
