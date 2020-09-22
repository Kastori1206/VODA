from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
#인증됨? 
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article


@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


@api_view(['POST'])
#AnonymousUser 방지 (Token없는 경우)
#인증된 사용자인지 확인
@permission_classes([IsAuthenticated])
def create_article(request):
    # print('POST: ', request.POST)
    # print('data: ', request.data)
    # POST:  <QueryDict: {}>
    # data:  {'content': 'bye', 'title': 'HI'}
    # row형식으로 데이터 보냈을 때 request.POSt는 값을 아예 받지 못하기 때문에
    # request.data를 사용하는게 좋음
    serializer = ArticleSerializer(data=request.data)
    # if serializer.is_valid(raise_exception=True):
    #     serializer.save(user=request.user)  # NOT NULL CONSTRAINT FAILED
    #     return Response(serializer.data)
    # raise_exception=True : 에러 메세지 보여줌 
    if serializer.is_valid(raise_exception=True):
        # print(request.user) //요청된 user값이 나오는거 확인 가능
        #print("==============",request.user) => token값이 없을 때 AnonymousUser
        serializer.save(user=request.user) #요청보낸 사용자를 저장  
        # 예전에는 밑의 방식으로 했음
        # serializer.save(user_id=1)

        # 비어있으면 NOT NULL CONSTRAINT FAILED
        #serializer.save()
        return Response(serializer.data)

    