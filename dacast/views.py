from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from dacast.serializers import VideoSerializer


@api_view(['GET', 'POST'])
def uploadVideo(request):
    if request.method == "POST":
        serializer = VideoSerializer(data=request.data)
        token = "1641301942hzIX4LKsvBFgHn32Ms0TuAPk1JeWBAxv"
        if serializer.is_valid():
            file = serializer.validated_data['file']
            serializer.save()
            url = ('https://upload.dacast.com')
            res = requests.post(url, data={
                'source': 'test.mp4',
                'upload_type': 'ajax',
                
                'token': token,
            })
            # print(res.json())
        else:
            return Response(serializer.errors.json())
    
    return Response("dnoe")
        
