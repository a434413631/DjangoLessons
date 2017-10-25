from rest_framework import models


class RSBase:
    def __init__(self, data, success, message, token):
        self.data = data
        self.success = success
        self.message = message
        self.token = token

    def __init__(self, data, token):
        self.data = data
        self.success = True
        self.message = "数据请求成功"
        self.token = token
