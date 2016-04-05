# python-odds_and_evens
This project is realization of on-line game (
http://www.neos-guide.org/content/game-theory-basics) known as 'odds_and_evens' with two players.
Both take actions not being aware of action other player. They select either '1'(odd) or '2'(even).
If their selections match, then Second Player won, otherwise First Player won and Second lost accordingly.
The game was implemeted using Python, Django, Django REST Framework, SQLite and, for synchronization purpose,
RabbitMQ and Python Client to it, Pika. There is assumption that RabbitMQ already installed. Project was
developed and tested on laptop running Ubuntu 15.04. Every Player uses command line interface. 
