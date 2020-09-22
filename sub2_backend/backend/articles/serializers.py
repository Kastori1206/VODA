from rest_framework import serializers
from .models import Article
from accounts.serializers import UserSerializer

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'created_at']


class ArticleSerializer(serializers.ModelSerializer):
    #user와 엮어서 이해하기
    # required=False => 
    #views.py에서의 is_valid() 에서 유무검증 pass 
    user = UserSerializer(required=False)  
    class Meta: 
        model = Article
        fields = '__all__'
