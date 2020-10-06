from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import RetrieveAPIView

import kss
from konlpy.tag import Hannanum

hannanum = Hannanum() 

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def stt(request):
    print(request.data)
    a=[]
    for sent in kss.split_sentences(request.data['text']):
        a.append(hannanum.nouns(sent))
    return Response(a)