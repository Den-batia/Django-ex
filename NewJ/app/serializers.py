from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import News


class UserSerializer(serializers.ModelSerializer):
    news = serializers.PrimaryKeyRelatedField(many=True, queryset=News.objects.all())
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'news']


class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email']



class NewsSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')
    author = UserSerializer1()

    class Meta:
        model = News
        fields = '__all__'

