from rest_framework import models


class RQBase:
    def __init__(self, json_str):
        self.data = json_str.get('data')
        self.clientID = json_str.get('clientID')
        self.currentVersion = json_str.get('currentVersion')
        self.deviceID = json_str.get('deviceID')
