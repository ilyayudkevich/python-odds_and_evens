from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from game.models import Action, Result, Player1Action, Player2Action, GameResultsDisplay

@receiver(post_save, sender=Player2Action)
def populate_results(sender, **kwargs):
    if kwargs.get('created', True):
        results = Result.objects.all()
        actions = Action.objects.all()
        player2actions = Player2Action.objects.all()
        player1actions = Player1Action.objects.all()
        ltbp1a = len(player1actions)
        ltbp2a = len(player2actions)
        insert_GameResults(ltbp1a, ltbp2a, player1actions, player2actions, results)

def insert_GameResults(n1, n2, player1actions, player2actions, results):
  res1 = results[0].name
  res2 = results[1].name
  act1 = player1actions[n1 - 1].actionid
  act2 = player2actions[n2 - 1].actionid
  print(res1, res2, act1, act2)
  if(player1actions[n1 - 1].actionid == player2actions[n2 - 1].actionid):
    grs = GameResultsDisplay(action1 = act1, result1 = res2, \
                             action2 = act2, result2 = res1)
#    print ('Second Player won')
  else:
    grs = GameResultsDisplay(action1 = act1, result1 = res1, \
                             action2 = act2, result2 = res2)
#    print ('First PLayer Won')

  grs.save()




