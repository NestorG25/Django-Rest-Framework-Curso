from rest_framework import routers
from .api import ProjectViewSet

router= routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls

#urlpatterns = [
  ##  path('projects/', views.projects, name="projects"),
  ##  path('project/<str:pk>/', views.project, name="project"),
#]

