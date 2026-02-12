from rest_framework import serializers
from .models import Resources , Tag

class ResourceSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Resources
        fields = '__all__'
        files = serializers.CharField(required=False)
        read_only_fields = ['owner']
        tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        required=False
)
# serializers.PrimaryKeyRelatedField() it only supports the existing tag means the existing id of tags , 
# if different given then error occurs

class TagSerializer(serializers.ModelSerializer):
    class Meta :
        model = Tag
        fields = ['id','name']