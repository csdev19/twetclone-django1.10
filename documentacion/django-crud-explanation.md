# Django CRUD

Vamos a ver acerca del concepto de **CRUD** en Django y haremos nuestra primeras vistas relacionadas a esto.

## Que es un CRUD ?

**CRUD** son las siglas de:

- **C**reate: Crear
- **R**ead: Leer
- **U**pdate: Actualizar
- **D**elete: Eliminar.

## Y como asociamos esto con Django ?

En que estas siglas van a representar diferentes metodos que podemos usar dentro de nuestra **aplicacion web**. En este caso podriamos usar:

- El metodo Create: Para crear un Tweet.
- El metodo Read: Para ver los Tweets disponibles.
- El metodo Update: Para actualizar o modificar un tweet ya existente.
- El metodo Delete: Para eliminar un Tweet.

Ahora, podemos notar que todas estas acciones pueden ser realizadas dentro del **admin de django** pero esto no es muy practico para los usuarios finales. Asi que tendremos que crear vistas para permitir a los usuarios tener una forma interactiva y **restringidia** de realizar estas acciones.

