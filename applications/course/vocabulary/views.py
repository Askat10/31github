from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, SAFE_METHODS, AllowAny

from applications.course.vocabulary.models import WordsModel
from applications.course.vocabulary.serializers import WordsSerializer


class WordsViewSet(ModelViewSet):
    queryset = WordsModel.objects.all()
    serializer_class = WordsSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
