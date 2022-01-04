from django.http.response import HttpResponse
from rest_framework.decorators import api_view
import requests
from dacast.models import Video
from dacast.serializers import VideoSerializer


@api_view(['GET', 'POST'])
def uploadVideo(request):
    if request.method == "POST":
        serializer = VideoSerializer(data=request.data)
        token = "1641301942hzIX4LKsvBFgHn32Ms0TuAPk1JeWBAxv"
        if serializer.is_valid():
            serializer.save()
            url = ('https://upload.dacast.com')
            requests.post(url, token, serializer.data)
    
    return HttpResponse(request, url, {'form': serializer.data})
        
