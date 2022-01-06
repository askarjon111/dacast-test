import base64
from urllib.request import urlopen
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json
from dacast.serializers import VideoSerializer
        

@api_view(['POST'])
def getToken(request):
    apikey = "1641301942hzIX4LKsvBFgHn32Ms0TuAPk1JeWBAxv"
    tokenUrl = f"https://developer.dacast.com/v2/vod/"
    uploadUrl = "https://upload.dacast.com/v2/vod"
    if request.method == "POST":
        print("getting token")
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            data = {
                "source": base64.b64encode(serializer.validated_data['file']).read(),
                "upload_type": "ajax",
            }
            headers = {
                "X-Api-Key": apikey,
            }
            resTok = requests.post(tokenUrl, headers=headers, json=json.dumps(data))
            print(data)
            print("token: ", resTok.status_code)
            res = requests.post(
                uploadUrl, data, headers=resTok)
            print("upload: ", res)
        else:
            return Response(serializer.errors.json())

    return Response("dnoe")
