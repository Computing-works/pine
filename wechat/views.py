from django.http import HttpRequest,HttpResponse
from django.shortcuts import render

import hashlib

WECHAT_TOKEN = ''

def index(request):
    token = WECHAT_TOKEN
    
    if request.method == 'GET':
        signature = request.GET.get('signature','')
        timestamp = request.GET.get('timestamp','')
        nonce = request.GET.get('nonce','')
        echostr = request.GET.get('echostr','')
        tmpArr = [token,timestamp,nonce]
        tmpArr.sort();
        tmpStr = ''.join(tmpArr);
        sha1 = hashlib.sha1();
        sha1.update(tmpStr);
        
        if sha1.hexdigest() == signature:
            return HttpResponse(echostr)
        
    return HttpResponse(', '.join(['hello','there','!']))
