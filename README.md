# python-odds_and_evens
#This project is realization of on-line game (
#http://www.neos-guide.org/content/game-theory-basics)
#known as 'odds_and_evens' with two players.
#Both take actions not being aware of action other player.
#They select either '1'(odd) or '2'(even).
#If their selections match, then Second Player won, 
#otherwise First Player won and Second lost accordingly.
#The game was implemeted using 
#Python3, Django, Django REST Framework, SQLite and, 
#for synchronization purpose,
#RabbitMQ and, Python Client to it, Pika. 
#There is assumption that RabbitMQ already installed and running. 
#Project was developed and tested on laptop running Ubuntu 15.04. 
#Every Player uses command line interface. 

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

13. copy all files and folders
14. python manage.py migrate
15. python manage.py createsuperuser
#    providing username:  admin
#              email:     admin@email.com
#              password:  password123
16. python manage.py loaddata `pwd` game/fixtures/users.json
17. python manage.py loaddata `pwd` game/fixtures/actions.json
18. python manage.py loaddata `pwd` game/fixtures/results.json
19. cd ..





