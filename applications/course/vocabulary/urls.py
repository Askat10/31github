from rest_framework import routers

from applications.course.vocabulary.views import WordsViewSet

router = routers.DefaultRouter()
router.register('words', WordsViewSet, 'words')
urlpatterns = router.urls
