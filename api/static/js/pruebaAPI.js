document.addEventListener("DOMContentLoaded", function () {
  // Obtener elementos del DOM
  var openModalButton = document.querySelector(".open-modal-button");
  var closeModalButton = document.querySelector(".close-modal-button");
  var modal = document.getElementById("myModal");
  var formulario = document.getElementById("miFormulario");
  var resultado = document.getElementById("resultado");

  // Función para abrir el modal
  function abrirModal() {
      modal.style.display = "block";
  }

  // Función para cerrar el modal
  function cerrarModal() {
      modal.style.display = "none";
  }

  // Función para enviar el formulario y mostrar la información
  function enviarFormulario(event) {
    event.preventDefault(); // Evita que se recargue la página

    // Obtener los valores del formulario
    var nombre = document.getElementById("nombre").value;
    var email = document.getElementById("email").value;

    // Crear un nuevo div para la información
    var infoDiv = document.createElement("div");
    infoDiv.classList.add("info-div");
    infoDiv.innerHTML = "<h3>Información enviada:</h3><p>Nombre: " + nombre + "</p><p>Email: " + email + "</p>";

    // Agregar el div al contenedor de información
    var informacionContainer = document.getElementById("informacion-container");
    informacionContainer.appendChild(infoDiv);

    // Cerrar el modal
    cerrarModal();
  }

  // Agregar eventos
  openModalButton.addEventListener("click", abrirModal);
  closeModalButton.addEventListener("click", cerrarModal);
  formulario.addEventListener("submit", enviarFormulario);
});
