# Calculatrice

Pour lancer le serveur je peux uitiliser la commande ci-dessous:

docker compose up --build   

```
version: '3.1'

services:
  server:
    image: woof
    build: .
    environment:
      CHAT_PORT : 4444
    ports: 
      - "8080:4444"


# 8080 = le port de ma machine
# 4444 = le port sur lequel le programme écoute
```


Si je veux lancer le serveur sur un port en particulier, j'utilise ce code en définissant le port souhaité(ici en gras):
```
docker run -p  8080:**1111** -e CHAT_PORT=**1111** woof
```