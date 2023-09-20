window.addEventListener('load', function () {
    getservers();
});

// TOMAR BOTONES PARA FUNFIONALIDADES DE UNIRSE A UN SERVIDOR O BUSCAR UNO.
// document.getElementById("addServer").addEventListener("click", addServer);
// document.getElementById("searchServer").addEventListener("click", searchServer);

function getservers() {
    const url = "http://127.0.0.1:5000/auth/profile";
    
    fetch(url, {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            return response.json().then(data => {
                document.getElementById("username").innerText = data.username;
                document.getElementById("username1").innerText = data.username;
                document.getElementById("username2").innerText = data.username;
                document.getElementById("username3").innerText = data.username;

                const materiasContainer = document.getElementById('materias-container');
                servidores = data.servers
                servidores.forEach(server => {
                    console.log(server)
                    const div = document.createElement('div');
                    div.innerHTML = `<div class="pf2" style="border-radius: 15px; background: #5865f2">
                                        <p style="color: #fff; font-weight: bold; font-size: 15px">${server[0]}</p>
                                        <div class="left-line" style="opacity: 1; height:40px; top: -2px"></div>
                                        <div id="servers" class="tooltip">${server}</div>    
                                    </div>`;
                    materiasContainer.appendChild(div);
                });
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