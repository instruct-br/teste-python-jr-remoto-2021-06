# Template flask

Este é um template de uma aplicação [Flask](https://flask.palletsprojects.com/en/2.0.x/), utilizando o [SQLAlchemy](https://www.sqlalchemy.org/) como ORM, e o [Alembic](https://alembic.sqlalchemy.org/en/latest/front.html#project-homepage) como ferramenta de migração.

## Iniciando

Instale as dependências deste template utilizando o [Pipenv](https://pipenv.pypa.io/en/latest/), com o seguinte comando:

```sh
pipenv install
```

Para subir este app em ambiente de desenvolvimento, execute:

```sh
sh run.sh
```

Este template, está configurado para utilizar um banco sqlite em ambiente de dev, e o Postgres em ambiente de prod.

## Migrations

Caso você faça alguma alteração nas models, e queira executar uma migration, utilize o seguinte comando:

```sh
alembic revision --autogenerate -m "<nome da migration>"
```

Para aplicar manualmente as migrations geradas no passo anterior, utilize o comando:

```sh
alembic upgrade head
```