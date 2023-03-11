from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from tasks import views

router = routers.DefaultRouter()
router.register(r"tasks", views.TaskView, "tasks")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='Tasks API')),
]