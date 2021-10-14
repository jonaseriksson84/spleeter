import os
from django.http.response import HttpResponse

from django.shortcuts import render
from django.core.files import File
from pathlib import Path

# Create your views here.
from spleeter.separator import Separator
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from rest_framework.decorators import api_view


@api_view()
def hello_world(request):
    separator = Separator("spleeter:2stems")
    separator.separate_to_file("./missli.mp3", "./output/")
    print("hej")
    return Response({"message": "Hello, worldz!"})


class UploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            uploaded_file = file_serializer.save()

            separator = Separator("spleeter:2stems")
            separator.separate_to_file(
                f"{os.getcwd()}/media/{uploaded_file.file}", "./media/output/"
            )
            resp = file_serializer.data
            resp[
                "vocals"
            ] = f"http://localhost:8000/download/{uploaded_file.file}/vocals.wav"
            resp[
                "accompaniment"
            ] = f"http://localhost:8000/download/{uploaded_file.file}/accompaniment.wav"
            return Response(resp, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DownloadView(APIView):
    def get(self, request, *args, **kwargs):
        file_path = f"{os.getcwd()}/media/output/{kwargs.get('song').split('.')[0]}/{kwargs.get('filename')}"
        print(file_path)
        f = open(file_path, "rb")
        response = HttpResponse(f, content_type="audio/x-wav")
        response[
            "Content-Disposition"
        ] = f"attachment; filename={kwargs.get('filename')}"
        return response


#     file_path = file_url
#     FilePointer = open(file_path,"r")
#     response = HttpResponse(FilePointer,content_type='application/msword')
#     response['Content-Disposition'] = 'attachment; filename=NameOfFile'

#     return response.
