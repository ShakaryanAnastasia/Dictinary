from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import WordView, WordViewSet

app_name = "define"
router = routers.DefaultRouter()
router.register(r'define', WordViewSet)

urlpatterns = [
    # url(r'^$', ListView.as_view(queryset=Word.objects.all().order_by("-date")[:20],
    # template_name="define/words.html")),
    # url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Word, template_name = "define/word.html"))
    url(r'^', include(router.urls)),
]