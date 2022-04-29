from django.contrib.auth.models import AnonymousUser
from articles.serializers import ArticleSerializer
from articles.models import Article
from articles.permissions import IsAuthorOrReadOnly
from rest_framework import viewsets


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(is_public=True)
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        username = self.request.user
        if str(username) == 'AnonymousUser':
            return Article.objects.filter(is_public=True)
        return Article.objects.all()
