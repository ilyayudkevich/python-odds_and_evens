from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from game.models import Action, Result, Player1Action, Player2Action, GameResultsDisplay
from game.serializers import UserSerializer, GroupSerializer, ActionSerializer, ResultSerializer, Player1ActionSerializer, Player2ActionSerializer, GameResultsDisplaySerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ActionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows actions to be viewed or edited.
    """
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

class ResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows results to be viewed or edited.
    """
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class Player1ActionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows player1actions to be viewed or edited.
    """
    queryset = Player1Action.objects.all()
    serializer_class = Player1ActionSerializer

class Player2ActionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows player2actions to be viewed or edited.
    """
    queryset = Player2Action.objects.all()
    serializer_class = Player2ActionSerializer

class GameResultsDisplayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows gameresults1display to be viewed or edited.
    """
    queryset = GameResultsDisplay.objects.all()
    serializer_class = GameResultsDisplaySerializer

