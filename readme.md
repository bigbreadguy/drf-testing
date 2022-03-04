: 1646360223:0;cd drf_test
: 1646360241:0;django-admin
: 1646360244:0;python3
: 1646360323:0;python manage.py runserver
: 1646360470:0;python manage.py startapp api
: 1646360499:0;pip install djangrorestframework
: 1646360507:0;pip install djangorestframework
: 1646360688:0;python manage.py runserver
: 1646360723:0;pip install djangorestframework
: 1646360725:0;python manage.py runserver
: 1646360849:0;pip freeze > requirements.txt
: 1646360851:0;cat requirements.txt
: 1646360872:0;pip install gunicorn
: 1646360876:0;pip freeze > requirements.txt
: 1646360893:0;gunicorn drf.wsgi:application --forwarded-allow-ips="*" --bind 0.0.0.0:8000
: 1646360922:0;docker build -t drf-testing .
: 1646361111:0;ssh ubuntu@jenkins.deeping.kr
: 1646361365:0;docker-compose up -d
: 1646361384:0;docker-compose ps
: 1646361390:0;docker logs nginx
: 1646361401:0;docker-compose down
: 1646361416:0;docker-compose up -d
: 1646361424:0;docker ps
: 1646361484:0;docker-compose down
: 1646361763:0;chmod 400 Downloads/drf-testing.pem
: 1646361767:0;chmod 400 ~/Downloads/drf-testing.pem

: 1646362655:0;cd
: 1646362657:0;ls -al
: 1646362664:0;cat .zsh_history
