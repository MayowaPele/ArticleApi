from django.db.models import fields
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        #fields = ['id', 'title', 'Author', "email"]

        # To get all fields:
        fields = "__all__"