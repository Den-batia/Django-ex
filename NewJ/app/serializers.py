from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import News


class MyUserSerializer(serializers.ModelSerializer):
    news = serializers.PrimaryKeyRelatedField(many=True, queryset=News.objects.all())
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'news']


class MyUserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email']



class NewsSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')
    author = MyUserSerializer1()

    class Meta:
        model = News
        fields = '__all__'

