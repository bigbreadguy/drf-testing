```
  cd drf_test
  django-admin
  python3
  python manage.py runserver
  python manage.py startapp api
  pip install djangrorestframework
  pip install djangorestframework
  python manage.py runserver
  pip install djangorestframework
  python manage.py runserver
  pip freeze > requirements.txt
  cat requirements.txt
  pip install gunicorn
  pip freeze > requirements.txt
  gunicorn drf.wsgi:application --forwarded-allow-ips="*" --bind 0.0.0.0:8000
  docker build -t drf-testing .
  ssh ubuntu@jenkins.deeping.kr
  docker-compose up -d
  docker-compose ps
  docker logs nginx
  docker-compose down
  docker-compose up -d
  docker ps
  docker-compose down
  chmod 400 Downloads/drf-testing.pem
  chmod 400 ~/Downloads/drf-testing.pem

  cd
  ls -al
  cat .zsh_history
```
