# python-odds_and_evens
#This project is realization of on-line game (
#http://www.neos-guide.org/content/game-theory-basics)
#known as 'odds_and_evens' with two players.
#Both take actions not being aware of action other player.
#They select either '1'(odd) or '2'(even).
#If their selections match, then Second Player won, 
#otherwise First Player won and Second lost accordingly.
#The game was implemeted using 
#Python3, Nginx, WSGI, Django, Django REST Framework, SQLite and, 
#for synchronization purpose,
#RabbitMQ and, Python Client to it, Pika. 
#There is assumption that RabbitMQ, Nginx are already installed and running. 
#Also there should be installed Git and virtualenv
#Project was developed and tested on laptop running Ubuntu 15.04. 
#Every Player uses command line interface by launching 
#(env)...$python first_player.py
#(env)...$python second_player.py

STEPS TO GET GAME WORKING:

1. cd /path_to_your_folder/
2. virtualenv -p /usr/bin/python3 env
3. source env/bin/activate
4. pip install --upgrade pip
5. pip install pika
6. pip install httpie
7. pip install django
8. pip install djangorestframework

9. django-admin.py startproject odds_and_evens
10. cd odds_and_evens
11. django-admin.py startapp game
12. python manage.py migrate

13. copy all files and folders: 
    git clone https://github.com/ilyayudkevich/python-odds_and_evens.git 
    from: python-odds_and_evens/odds_and_evens/odds_and_evens
    to:   odds_and_evens/odds_and_evens
          settings.py, urls.py
    
    from: python-odds_and_evens/odds_and_evens/game
    to:   odds_and_evens/game
          folders: fixtures, migrations
          files:  apps.py, __init__.py, models.py, serializers.py, signals.py, views.py

    from python-odds_and_evens:
    to: /path_to_ypur_folder/
        first_player.py
        second_player.py
        README.md
    
14. python manage.py migrate
15. python manage.py createsuperuser
#    providing username:  admin
#              email:     admin@email.com
#              password:  password123
16. python manage.py loaddata `pwd` game/fixtures/users.json
17. python manage.py loaddata `pwd` game/fixtures/actions.json
18. python manage.py loaddata `pwd` game/fixtures/results.json
19. cd ..
20. open second terminal window, activate virtualenv environment
21. open third terminal window, activate virtualenv, cd odds_and_evens, run: python manage.py runserver 
22. Optional. Open forth terminal window, activate virtualenv and issue command:
    http -a admin:password123 http://127.0.0.1:8000/users/

    Verify that three users in the database, if yes, you are good to start a game.

23. from second terminal window enter command:  python second_plaer.py  # second player always awaiting an action from first player
    from first terminal window enter command:   python first_player.py  # follow instructions from both screens, enjoy!




