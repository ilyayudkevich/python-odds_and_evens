from django.conf.urls import url, include
from rest_framework import routers
from game import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'actions', views.ActionViewSet)
router.register(r'results', views.ResultViewSet)
router.register(r'player1actions', views.Player1ActionViewSet)
router.register(r'player2actions', views.Player2ActionViewSet)
router.register(r'gameresultsdisplays', views.GameResultsDisplayViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
