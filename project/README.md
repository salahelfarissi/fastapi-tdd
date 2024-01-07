# FastAPI TDD Docker

## Setup

Run application in a containerized environment.

```shell
docker compose up -d --build
```

To access the database.

```shell
docker compose exec web-db psql -U postgres
```
