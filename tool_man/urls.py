from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from toolmanapi.views.auth import login_user, register_user
from toolmanapi.views.customer import CustomerView
from toolmanapi.views.message import MessageView
from toolmanapi.views.request import RequestView
from toolmanapi.views.request_photo import RequestPhotoView
from toolmanapi.views.status import StatusView
from toolmanapi.views.topic import TopicView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'topics', TopicView, 'topic')
router.register(r'statuses', StatusView, 'status')
router.register(r'requests', RequestView, 'request')
router.register(r'messages', MessageView, 'message')
router.register(r'customers', CustomerView, 'customer')
router.register(r'requestphotos', RequestPhotoView, 'requestphoto')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
