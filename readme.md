# Como deployar esto?

## 1. Solicitas las envs

Vas a necesitar estas 

DB_HOST=
DB_USER=
DB_PASS=
AWS_ACCESS_ID=
AWS_SECRET_ID=

## 2. Instala el CLI de Elastic Beanstalk
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html
## 3. Crear una app de elastic beanstalk
1. Inicializa el CLI - Sigue los pasos para logearte con tus credenciales de AWS y crear la aplicacion de EB para el deploy
```
eb init
```
2. Deploy tu app con el comando
```
eb deploy
```
3. Abre tu app con

```
eb open
```
# Listo
