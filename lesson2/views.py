import pdb
import urllib

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from flask import json
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import exceptions

from lesson1.models import Student
from lesson1.serializers import StudentSerializer
from lesson2.rqbase import RQBase
from lesson2.rsbase import RSBase
from rest_framework.authtoken import views


@api_view(['POST'])
def test(request):
    queryset = Student.objects.all().order_by('-created')
    # serializer_class = StudentSerializer(queryset)
    # serializer = StudentSerializer2(student)
    serializer = StudentSerializer(queryset, many=True)
    data = {'list':serializer.data}
    response = RSBase(data,"")
    # return JsonResponse(serializer.data, safe=False)
    json_str = json.dumps(response, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    return HttpResponse(json_str)


# 用户登录
@csrf_exempt
def user_login(request):
    json_str = json.loads(request.body)
    rqbase = RQBase(json_str)
    username = rqbase.data.get('phoneNum')
    if not username:
        return None

    user = User.objects.get(username=username)
    if not user:
        user = User.objects.create_user(username)
    token = Token.objects.get(user=user)
    if not token:
        token = Token.objects.get(user=user)

    # user = User.objects.get(username='admin')
    # new_token = Token.objects.create(user=user)
    # user_agent = "Mozilla/5.0 (Windows NT 6.1)"
    # headers = {
    #     'username': username,
    #     'password': password,
    #     'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    #     'User-Agent': user_agent,
    # }
    # data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
    # data = data.encode('utf-8')
    # # token = views.obtain_auth_token(request)
    # res = urllib.request.Request(url='http://127.0.0.1:8000/api-token-auth/', headers=headers)
    # response = urllib.request.urlopen(res,data)
    # print(token)
    # print(token)
    response = RSBase({}, token.key)
    # return JsonResponse(serializer.data, safe=False)
    json_str = json.dumps(response, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    print(json_str)
    return HttpResponse(json_str)
