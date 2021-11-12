from django.contrib.auth import get_user_model
from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthororReadOnly

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthororReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

