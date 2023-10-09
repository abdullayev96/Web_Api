from rest_framework import serializers
from .models import Childern


class ChildernListSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Childern
        fields = ('id', 'name', 'title', 'description', 'image', 'parent', 'children', 'husband')

    def get_children(self, obj):
        instance = obj.children.all()
        return ChildernListSerializer(instance, many=True).data


class ChildernDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Childern
        fields = '__all__'


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Childern
        fields = '__all__'
