from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp import views

router = DefaultRouter()
router.register('singer', views.singerviewset, basename='singer')
router.register('song', views.Songviewset, basename='song')

urlpatterns = [
    path('', include(router.urls)),
    

]
