// Cargar la informacion del usuario en los inputs apenas ingrese al formulario...
window.addEventListener('DOMContentLoaded', function () {
    cargarDatosUsuario();
});

function cargarDatosUsuario() {
    fetch("http://127.0.0.1:5000/auth/profile", {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            return response.json().then(data => {
                console.log(data)
                console.log(data.username)
                console.log(data.email)
                console.log(data.first_name)
                console.log(data.last_name)

                document.getElementById("username").value = data.username;
                document.getElementById("email").value = data.email;
                document.getElementById("first_name").value = data.first_name;
                document.getElementById("last_name").value = data.last_name;
            });
        } else {
            return response.json().then(data => {
                document.getElementById("message").innerHTML = data.message;
            });
        }
    })
    .catch(error => {
        document.getElementById("message").innerHTML = "An error occurred.";
    });
}

// FORMULARIO DE ACTUALIZACION DEL USUARIO
document.getElementById("editUSerForm").addEventListener("submit", function (event) {
    event.preventDefault();
    updateUser();
});

function updateUser() {
    // Actualizamos el username de la sessionStorage
    let newUsername = document.getElementById("username").value;
    sessionStorage.setItem('user', newUsername)

    const data = {
        user_id: sessionStorage.getItem('user_id'),
        username: document.getElementById("username").value,
        email: document.getElementById("email").value,
        first_name: document.getElementById("first_name").value,
        last_name: document.getElementById("last_name").value
    };

    console.log(data)

    fetch("http://127.0.0.1:5000/auth/edit", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            // Redirect to login page if register is successful
            return response.json().then(data => {
                console.log(data)
                window.location.href = "profile.html";
            });
        } else {
            return response.json().then(data => {
                document.getElementById("message").innerHTML = `<div class="notifications-container">
                <div class="error-alert">
                  <div class="flex">
                    <div class="flex-shrink-0">
                      <svg aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" class="error-svg">
                        <path clip-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" fill-rule="evenodd"></path>
                      </svg>
                    </div>
                    <div class="error-prompt-container">
                      <p class="error-prompt-heading">${data.message}</p>
                    </div>
                  </div>
                </div>
              </div>`;
            });
        }
    })
    .catch(error => {
        document.getElementById("message").innerHTML = "An error occurred.";
    });
}