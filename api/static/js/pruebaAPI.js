// URL de la API
const apiUrl = 'http://127.0.0.1:5000/auth/usuarios';

// Solicitud GET a la API
fetch(apiUrl, {
    method: 'GET',
    credentials: 'include'
})
  .then(response => {
    // Verifico si la solicitud fue exitosa (código de estado 200)
    if (!response.ok) {
      throw new Error(`La solicitud falló con el código de estado ${response.status}`);
    }
    // Parsea la respuesta JSON
    return response.json();
  })
  .then(data => {
    // Acceder a los datos en formato JSON
    console.log(data);
    // Manipular los datos y mostrarlos en tu página web...
  })
  .catch(error => {
    // Manejo los errores de la solicitud
    console.error('Error al consumir la API:', error);
  });
