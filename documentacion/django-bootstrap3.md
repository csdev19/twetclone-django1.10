# Django y Bootstrap3

Vamos a ver como integrar **bootstrap3** a nustro proyecto.

Para esta seccion usaremos el siguiente [link](https://getbootstrap.com/docs/3.3/getting-started/)

## Para hacer esto tenemos dos caminos

**Un camino corto y otro largo** y vamos a ver los dos aqui.

- **La forma corta:** Usa el **CDN** de **Bootstrap** para esto usaremos el **Basic template** que podemos ver en la documentacion.
- **La forma larga:** Seria manejando archivos estaticos de Bootstrap en Django.


## Veamos la forma corta en profundidad

Para esto usaremos el **Basic Template** como ya dijimos antes, y lo copiaremos dentro de nuestro **home.html** de la siguiente manera:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>Bootstrap 101 Template</title>
    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <h1>Hello, world!</h1>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
```

Pero, faltaria un detalle. Cuando cargamos los archivos de **bootstrap3** estarian buscando las carpetas que contienen los archivos. Pero nosotros usaremos el **CDN** asi que debemos reemplazar esto por los links que nos dan en la seccion de **CDN**

Pero que hace un **CDN** o como funciona ?
Lo que hace es que los archivos estaticos que cargamos son guardados en el **browser** de la persona que accede al sitio web. Entonces cada vez que entre alguien aqui este fichero va a cargar increiblemente rapido.


## Ahora veremos la forma larga

Y para esto debemos usar **los archivos estaticos mediante Django**. 

Para esto debemos descargar **Bootstrap** la version 3 minificada. Y extraer sus tres carpetas (css, js y fonts) dentro de nuestro proyecto, especificamente en la carpeta **static-serve** porque desde ahi se cargaran nuestros archivos estaticos.


Luego de hacer esto tenemos que correr el comando **collecstatic** para cargar otra vez los archivos estativos y que reconozca ahora los nuevos que hemos agregado.

```console
$ python manage.py collecstatic
```

Aunque tambien podemos crear una carpeta llamada **bootstrap** y poner todos los archivos ahi dentro, en este caso me parece mas ordenado asi que eso hare.
Y volveremos a ejecutar **collecstatic**.


Ahora para trabajar con estos archivos estaticos en django, tenemos que agregar una linea de codigo a nuestro **html**, que es la siguiente:

```html
{% load static %}
....
```

Antiguamente se usaba el tag **{% load staticfiles %}** pero ahora podemos poner simplemente static.

Ahora para usar los archivos estaticos usaremos lo siguiente:

```html

```

Y asi quedaria

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap 101 Template</title>
    <!-- Bootstrap -->
    <!-- <link href="css/bootstrap.min.css" rel="stylesheet">
     --><!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <!-- <script src="js/bootstrap.min.js"></script> -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  </body>
</html>
```




















