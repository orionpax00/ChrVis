### Installation Instructions

#### Docker

```sh
git clone https:\\github.com\orionpax00\chrvis.git
```
```sh
cd chrvis
```
```sh
docker-compose build
```
```sh
docker exec -it chrvis bash
```

```sh
cd chrvis-server/
```
```sh
celery -A chrvis worker -l info
```
