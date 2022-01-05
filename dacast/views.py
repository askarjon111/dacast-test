from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from dacast.serializers import VideoSerializer


# @api_view(['GET', 'POST'])
# def uploadVideo(request):
#     if request.method == "POST":
#         serializer = VideoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             url = ('https://upload.dacast.com/v2/vod')
#             headers = {'X-Api-Key': "to1641301942hzIX4LKsvBFgHn32Ms0TuAPk1JeWBAxvken"}
#             res = requests.post(url, data={
#                 'source': 'test.mp4',
#                 'upload_type': 'ajax',
#             },
#             headers=headers)
#             print(res)
#         else:
#             return Response(serializer.errors.json())
    
#     return Response("dnoe")
        

@api_view(['GET', 'POST'])
def getToken(request):
    apikey = "to1641301942hzIX4LKsvBFgHn32Ms0TuAPk1JeWBAxvken"
    tokenUrl = "https://developer.dacast.com/?apikey=" + apikey
    callbackUrl = 'https://127.0.0.1:8000'
    uploadUrl = "https://upload.dacast.com"
    if request.method == "POST":
        print("getting token")
        
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            FormData = {
                'apikey'
                'source': serializer.data['file'],
                'callbackUrl': callbackUrl,
                'upload_type': 'ajax',
            }
            resTok = requests.post(tokenUrl)
            res = requests.post(uploadUrl, FormData, headers=resTok)
            print(res)
        else:
            return Response(serializer.errors.json())

    return Response("dnoe")
