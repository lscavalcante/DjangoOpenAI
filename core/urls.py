from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.openAI.api.viewsets import OpenIaAPI
from apps.openAI.views import gerente_image_from_txt

router = routers.DefaultRouter()
router.register(r'api/openAI', OpenIaAPI, basename='openai')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('web/openAI/', gerente_image_from_txt, name='generete_image_from_txt'),
    path('', include(router.urls)),
]
