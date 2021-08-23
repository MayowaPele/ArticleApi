from django.urls import path
from django.urls.conf import include
from .views import article_each, article_list, ArticleAPIView, ArticleViewSet, Article_each, GenericAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('article/', article_list),
    path('articleclass/', ArticleAPIView.as_view()),
    path('eacharticle/<int:id>/', article_each),
    path('eacharticleclass/<int:id>/', Article_each.as_view()),
    path('articlegeneric/<int:id>/', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls))
]
