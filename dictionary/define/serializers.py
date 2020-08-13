from rest_framework import serializers
from .models import Word
class WordSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    define = serializers.CharField()
    example = serializers.CharField()
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Word.objects.create(**validated_data)

class WSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ('url', 'title', 'define', 'example','date')
        lookup_field = 'title'

