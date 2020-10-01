from rest_framework import serializers
from django.contrib.auth.models import User
from cms.models import Page
from .models import Post

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# Serializers define the API representation.
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('__all__')


# Serializers define the API representation.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')