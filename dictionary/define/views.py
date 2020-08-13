from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Word
from .serializers import WordSerializer, WSerializer
from rest_framework import viewsets

class WordView(APIView):
    def get(self, request):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response({"words": serializer.data})

    def post(self, request):
        word = request.data.get('word')
        serializer = WordSerializer(data=word)
        if serializer.is_valid(raise_exception=True):
            word_saved = serializer.save()
        return Response({"success": "Word '{}' created successfully".format(word_saved.title)})


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WSerializer
    lookup_field = 'title'