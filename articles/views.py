from articles.serializers import ArticleSerializer
from articles.models import Article
from articles.permissions import IsAuthorOrReadOnly
from rest_framework import viewsets


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        username = self.request.user
        if username.is_active:
            return Article.objects.all()
        return Article.objects.filter(is_public=True)

    def get_permissions(self):
        return IsAuthorOrReadOnly(),

