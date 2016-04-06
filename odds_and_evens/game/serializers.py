from django.contrib.auth.models import User, Group
from rest_framework import serializers
from game.models import Action, Result, Player1Action, Player2Action, GameResultsDisplay


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ActionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Action
    fields = ('name', 'iname')

class ResultSerializer(serializers.ModelSerializer):
  class Meta:
    model = Result
    fields = ('name', 'iname')

class Player1ActionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Player1Action
    fields = ('actionid', 'iname')

class Player2ActionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Player2Action
    fields = ('actionid', 'iname')

class GameResultsDisplaySerializer(serializers.ModelSerializer):
  class Meta:
    model = GameResultsDisplay
    fields = ('action1', 'result1', 'action2', 'result2')


