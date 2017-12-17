# bundesLigueScrapApp

python3
  requests
  json
django
postgreSQL
celery
redis


Instalation:

  Django using pip:
  
    pip3 install django 
  
  postgreSQL:
    
    sudo apt-get install libpq-dev postgresql postgresql-contrib
    pip3 install django psycopg2
    

  celery and redis:
  
    pip3 install Celery
    brew install redis
    pip3 install -U "celery[redis]"
  
  
Decelopment setup:
  
    Setup postgreSQL database and user:
      psql
      CREATE DATABASE scrapinggames;
      CREATE USER scrapera WITH PASSWORD 'scraperDB';
      GRANT ALL PRIVILEGES ON DATABASE scrapinggames TO scrapera;
    
The project can be run either with celery and redis or running scraper.py from the terminal.
