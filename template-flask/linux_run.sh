export FLASK_ENV=development
export FLASK_APP=magpy
alembic upgrade head
flask run
