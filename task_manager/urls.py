from rest_framework.routers import DefaultRouter
from tasks.api import TaskViewSet
from users.api import UserViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'users', UserViewSet, basename='user')


urlpatterns = router.urls
