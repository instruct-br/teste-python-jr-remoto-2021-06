$env:FLASK_ENV="development"
$env:FLASK_APP="magpy"
alembic upgrade head
flask run
