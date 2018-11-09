# Django creando una aplicacion: tweet

Ahora hemos visto algunas funcionalidades que podemos hacer con django, pero para crear una aplicacion como **tweeter** necesitamos mas cosas. Por ejemplo, una manera de crear usuarios para que posteen cosas. Esto lo haremos mediantes **apps** de la siguiente manera que veremos a continuacion.

## Como crear una aplicacion en Django

Lo haremos de la siguiente manera, ejecutando la siguiente sentencia en la consola:

```console
$ python manage.py startapp <nombre-de-la-aplicacion>

# en este caso la aplicacion se llamara "tweets" asi que se veria de la siguiente manera:
$ python manage.py startapp tweets
```

Una vez creada la **"app"** vamos a ver como django crea una carpeta dentro de la cual vamos a trabajar nuestra app (una buena practica es hacer varias aplicaciones pequeñas que se encargue nde tareas particulares en vez de tener una app grande). Asi que haremos que esta app solo se encargue de manejar los tweets.

Ahora, vamos a ver que se creo dentro de la carpeta **"tweets"**:

```console
$ tree tweets

tweets
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

Pero antes de seguir vamos a hacer una pausa y veremos algo de django.

## Inspeccionando el ADMIN de Django

En especifico la secciond de **users**:

![admin1](../imgs/admin1.png)


![admin2](../imgs/admin2.png)


Aqui podemos ver los campos que existen y que podemos usar para configurar un usuario ya existente, o podriamos tambien crear uno.


