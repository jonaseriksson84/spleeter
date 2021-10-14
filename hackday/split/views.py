from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView
from spleeter.separator import Separator


@api_view()
def hello_world(request):
    separator = Separator("spleeter:2stems")
    separator.separate_to_file("./missli.mp3", "./output/")
    print("hej")
    return Response({"message": "Hello, worldz!"})


class UploadView(APIView):
    # parser_class = (FileUploadParser,)
    parser_classes = (FormParser, MultiPartParser)

    def put(self, request, format=None):
        if "file" not in request.data:
            raise ParseError("Empty content")

        f = request.data["file"]

        # mymodel.my_file_field.save(f.name, f, save=True)
        print(f)
        return Response(status=HTTP_201_CREATED)