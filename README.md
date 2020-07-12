# EnergyConsumptionAPI

Este proyecto consiste en una API Rest, desarrollada en Django REST framework, que cuenta con los endpoints necesarios para que el siguiente dashboard pueda mostrar los datos que en el se pueden apreciar:

![Dashboard](https://github.com/jesuschm/EnergyConsumptionAPI/blob/master/resources/dashboard.png?raw=true)

Para almacenar los datos se ha utilizado el sistema por defecto de base de datos que Django REST framework nos proporciona (Sqlite3) y para la autenticación, la propia autenticación basada en tokens de Django REST framework.

## Getting Started

### Prerequisitos

El proyecto ha sido desarrollado con la siguiente configuración:
- python 3.8
- pip 20.1.1
- django 3.0.8

### Instalación

Para probar el proyecto en tu equipo, debes tener primero instalado python (el siguiente enlace cuenta con una guía muy sencilla: https://tutorial.djangogirls.org/es/python_installation/) para luego continuar con los siguientes pasos:

1. Crearte un entorno virtual utilizando el comando 
```
python -m venv myvenv
```
2. Activar el entorno, introduciendo el siguiente comando
```
myvenv\Scripts\activate
```
3. Instalar Django
```
pip3 install django
```
4. E instalar Django Rest framework
```
pip3 install djangorestframework
```
5. Clonación del proyecto en el directorio deseado

## Modelo de datos

La principal entidad implementada en esta aplicación es la llamada CONSUMPTION y representa cada una de las mediciones del consumo energético que el cliente solicita. Estas mediciones pueden verse dentro del directorio /resources/. Cada uno de las columnas ha sido utilizada para dar vida a cada uno de los atributos de la entidad. 

Esta entidad tiene el siguiente aspecto:

![Consumption model](https://github.com/jesuschm/EnergyConsumptionAPI/blob/master/resources/Consumption_entity.png?raw=true)

## Despliegue

Para lenvantar nuestra API, debemos dirigirnos al directorio principal (donde se encuentra el archivo manage.py) e introducir el siguiente comando para levantar nuestro servidor:
```
manage.py runserver
```

## Uso

Aunque existía la posibilidad de hacer que esta API fuese explotable mediante la clase ListCreateAPIView que nos proporciona Django REST framework, la cual nos permite visualizar tanto la información de la base de datos como crear nuevos elementos. He preferido desarrollarla para su uso canónico: a traves de peticiones GET y POST.

Por ello, la forma más fácil de probar las diferentes funcionalidades es haciendo uso de Postman, el famoso software de peticiones HTTP. Por tanto, y para facilitar este trabajo, se puede hacer uso del fichero EnergyReportApp.postman_collection.json, localizado en el directorio raiz del proyecto. En este fichero tenemos las sigueintes peticiones ya configuradas:

1. [POST] Get-token, endpoint para autenticarnos en el servicio y conseguir el token que necesitaremos usar para el resto de peticiones.
2. [GET] Logout, endpoint para desidentificarnos como usuario.
3. [GET] User list, endpoint para visualizar todos los usuarios existentes en el sistema. Ideado para realizar un sistema de registro y login de usuarios aparte del superuser utilizado en el primero de los endpoints presentados.
4. [GET] Import consumption from CSV, este endpoint indicará al servicio el deseo de limpiar la tabla CONSUMPTION de la base de datos y la vuelve a poblar con toda la información dentro del CSV dentro de la carpeta /resources/.
5. [POST] El endpoint Filtered historial consumption está ideado para llevar al front todos los datos necesarios para pintar las gráficas. Esta gráfica representa cada uno de los atributos en el eje vertical, mientras que en el eje horizontal se encuentra el tiempo. Como la interfaz está diseñada para trabajar con pestañas, he pensado que lo mejor es devolver toda la información y no solo la pareja atributo-tiempo correspondiente en función de la pestaña seleccionada, gracias a esta forma de implementar la API, nos podremos ahorrar problemas de saturación del servicio (por ejemplo, si muchos usuarios cambian de pestañas de manera muy seguida).

Este método recibe dos fechas para filtrar los objetos dentro de ese periodo de tiempo.
6. [POST] Filtered energy consumption sum, endpoint que devuelve el consumo de energía activa, definido como la suma de todos los valores del campo energy.
Este método también recibe dos fechas para realizar su filtrado.
7. [POST] Filtered installed power avg, endpoint que devuelve la potencia instalada por el cliente, definida como la media de todos los valores del campo maximeter.
Al igual que los dos anteriores, este método también recibe dos fechas para realizar su filtrado.
8. [POST] Filtered reactive energy sum, endpoint que devuelve el consumo de energía reactiva, definida como la suma de todos los valores del campo reactive_energy.
Al igual que los tres anteriores, este método también recibe dos fechas para realizar su filtrado.

Las fechas pueden modificarse manualmente desde el menú body de Postman, pues todos los endpoints esperan recibir un tipo JSON con dicha información. Si alguno de las dos fechas no viene dentro del JSON, la fecha de hoy será la que se usará.

Adicionalmente, para poder realizar todas las peticiones de la API (excepto la primera), es necesario copiar el token a la cabecera del resto de las peticiones como se puede apreciar en la siguiente imagen (en la sección Authorization de la lista de parametros):

![Consumption model](https://github.com/jesuschm/EnergyConsumptionAPI/blob/master/resources/Authentication_Postman.png?raw=true)

## Test unitario
Para ejemplificar el uso de test unitarios en django. 

Este test prueba la función GetEnergyConsumptiom, función que devuelve uno de los datos del dashboard. Para ejecutarlo hay que introducir el siguiente comando:
```
manage.py tests test
```

## Mejoras
TODO_1. Parametrizar nombre del CSV. 
TODO_2. Securizar django secret key. 
1. Estudiaría el rendimiento de juntar los tres endpoints (6), (7), (8) en uno solo para reducir las llamadas a la API en una sola en vez de en tres, aunque el servicio perdiese flexibilidad. Quizás añadiría ambas posibilidades (petición de toda la información que no vaya a la gráfica a la vez que dar la posibilidad de poder extraer solo uno de los datos por separado).
2. Las fórmulas usadas para los endpoints (6), (7), (8) han sido implementadas en función de una rápida investigación. Sería necesario hablar con el cliente para conocer el cálculo exacto.
3. Implementar algún tipo de token sería interesante, como el tipo Bearer, más ampliamente usado, sería otras de mis mejoras.
4. La integración con Swagger para hacer la documentación de la API sencilla de entender y usar sería una de las mejoras más importantes.

## Autor

* **Jesús Chacón** - *Initial work* - [Jesús Chacón](https://github.com/jesushcm)
