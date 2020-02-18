from rest_framework import serializers
from .models import Snippet


# Post
#   List        PostSerializer
#   Retrieve    PostDetaukSerializer
#   Update      PostUpdateSerializer
#   Create      PostCreateSerializer
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            'pk',
            'author',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'created',
        )


class SnippetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            'pk',
            'author',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'created',
        )

        def to_representation(self, instance):
            return SnippetSerializer(instance).date
