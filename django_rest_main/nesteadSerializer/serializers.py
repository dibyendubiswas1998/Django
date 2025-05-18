from rest_framework import serializers
from .models import *



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
        
        
# Make Nestead Serializer
class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True) # it help to make nestead serializer. It bring entier comments into BlogSerializer
    class Meta:
        model = Blog
        fields = "__all__"
        
