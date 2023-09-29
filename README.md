
# 🚀 Acerca del Proyecto: Aplicación Web similar a Discord

En este proyecto se desarrolló una Aplicación Web con un sistema de mensajería similar a Discord.
La aplicación permite registrar usuarios, los cuales pueden crear o unirse a uno o más servidores. Un servidor es un espacio que puede contener usuarios y a su vez canales.


## Tecnológicas utilizadas
**HTML**, **CSS** , **Javascript**, **Flask**, **MySQL**, **Python**.


Para el desarrollo de la aplicación web fue necesario:
● Una interfaz con la que los usuarios de la aplicación interactúen, implementada con HTML, CSS y Javascript.
● Una REST API que pueda consumir la interfaz mediante fetching.
La cual fue implementada usando Flask, haciendo uso del patrón de diseño MVC.
● Una base de datos en MySQL, para manejar toda la información de la app.

## Funcionalidades
La aplicación permite las siguientes funcionalidades:
1. **Crear usuarios**: se solicitará el nombre del usuario,contraseña. La imagen de perfil sólo podrá elegirse posteriormente a la creación del usuario.

2. **Iniciar la sesión de un usuario**. En caso de que este no exista, deberá indicarse dicho hecho y sugerir que se registre en la aplicación.

3. Una vez iniciada una sesión, se deben mostrar tres columnas en la pantalla principal: a) Una primera columna debe mostrar un **listado con los servidores a los que el usuario pertenece**. Si no pertenece a ningún servidor, entonces mostrará un mensaje indicando esto. Por defecto ningún servidor estará seleccionado. Sin embargo al seleccionar uno, se deberá cargar una segunda columna con los **canales** que posea ese servidor. Además, esta columna debe tener un botón para **crear un servidor nuevo**. b) La segunda columna debe mostrar un **listado de los canales del servidor seleccionado**, si no tiene ningún canal creado muestra un mensaje indicándolo. Por defecto , ningún canal estará seleccionado. Sin embargo, al seleccionar uno, se deberá cargar una tercera columna con los **mensajes del chat de ese canal**. Además, esta columna debe tener un botón para **crear un canal nuevo**. c) La tercera columna mostrará los **mensajes ordenados cronológicamente**, con el más reciente en la parte inferior del chat. Si no hay ningún mensaje en el chat mostrará un mensaje indicando este hecho. Por supuesto, esta columna debe contar con un cuadro de texto para escribir un nuevo mensaje.

4. Los mensajes de un chat sólo pueden ser modificados o eliminados por el usuario que los ha creado.

5. Debe contar con un componente que permita mostrar el **perfil del usuario logueado**. En el perfil del usuario se podrán actualizar los datos personales del usuario, incluyendo la imagen del mismo.

6. La aplicación deberá implementar manejadores de errores personalizados para los siguientes casos:

a) 400, Bad Request. b) 404, Not Found.
c) 403, Forbidden. Para aquellas peticiones donde no se tenga permisos de acceso o modificación. Por ejemplo, al intentar eliminar un mensaje del chat de otro usuario. d) 500, Server Error.

7. **Buscador de servidores**: Se buscará por el nombre del servidor. En este componente se mostrarán todos los servidores que coincidan con la búsqueda realizada, para cada resultado se debe mostrar el nombre del servidor, la descripción del servidor (si la tuviera) y la cantidad de usuarios registrados en él (siempre tiene al menos un usuario registrado, quien lo creó).
8. Se deberá administrar la sesión de un usuario, es decir, registramos la información de un usuario inicie una sesión, y el acceso a los *endpoints* de la API REST diseñada deberá estar restringida sólo a usuarios logueados.

9. Notificaciones e invitaciones a un servidor.







## ¿Cómo ejecutar el proyecto?
Es importante activar el entorno virtual.
## Sobre el Equipo 💪
### Hola👋, Bienvenidos al Grupo 10. Somos **For()Innovators**! 
👩‍💻 Somos alumnos de primer año de la *Tecnicatura Universitaria en Desarrollo de Software* de la Universidad Provincial de Administración, Tecnología y Oficios UPATecO.

🧠 Actualmente estamos en nuestra etapa de formación académica. Somos alumnos comprometidos y entusiastas a la hora de desarrollar nuestros proyectos.


😄 Gracias por visitarnos!



## 🔗 Contactos

### LinkedIn
Kevin Serrano [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kevin-serrano-86711a231/)
Benjamin Assennato
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/benjamin-assennato-00ab80240/)
Jésica Llanos
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)

### Github
- [@Kevin](https://github.com/kevinserrano01)
- [@Benjamín](https://github.com/BenjaminAss)
- [@Jésica](https://github.com/Jesi10)

### 📫E-mails
Kevin Serrano: kevinserrano010@gmail.com
Benjamin Assennato: benjaassennato@hotmail.com
Jésica Llanos: teoricas461@gmail.com
