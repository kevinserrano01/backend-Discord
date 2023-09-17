window.addEventListener('load', function () {
    getUsername();
});

// TOMAR BOTONES PARA FUNFIONALIDADES DE UNIRSE A UN SERVIDOR O BUSCAR UNO.
// document.getElementById("addServer").addEventListener("click", addServer);
// document.getElementById("searchServer").addEventListener("click", searchServer);

function getUsername() {
    const url = "http://127.0.0.1:5000/auth/profile";
    
    fetch(url, {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            return response.json().then(data => {
                document.getElementById("username").innerText = data.username;
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