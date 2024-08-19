from django.urls import path,include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import ServiceViewsetWeb,BusinesViewsetWeb,UserViewsetWeb,ClientViewsetWeb,CommentViewsetWeb,FaqViewsetWeb





router = routers.DefaultRouter()
router.register(r"service-web", ServiceViewsetWeb, basename='service-web')
router.register(r"busines-web", BusinesViewsetWeb, basename='busines-web')
router.register(r"users-web", UserViewsetWeb, basename='users-web')
router.register(r"client-web", ClientViewsetWeb, basename='client-web')
router.register(r"comment-web", CommentViewsetWeb, basename='comment-web')
router.register(r"faqs-web", FaqViewsetWeb, basename='faqs-web')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth-token/', obtain_auth_token),
]