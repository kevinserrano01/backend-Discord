window.addEventListener('DOMContentLoaded', function () {
    getServers();
});

var server_name = sessionStorage.getItem('server_name')
let idBotonGlobal = null // id del boton del servidor seleccionado -> Global

function getServers() {    
    fetch("http://127.0.0.1:5000/auth/profile", {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            return response.json().then(data => {
                document.getElementById("username").innerText = sessionStorage.getItem('user');

                const servidoresContainer = document.getElementById('servidores-container');
                servidores = data.servers
                servidores.forEach(server => {
                    const div = document.createElement('div');
                    div.innerHTML = `<button id="${server}" class="pf2" style="border-radius: 15px; background: #5865f2">
                                        <p style="color: #fff; font-weight: bold; font-size: 15px">${server[0]}</p>
                                        <div class="left-line" style="opacity: 1; height:40px; top: -2px"></div>
                                        <div id="servers" class="tooltip">${server}</div>    
                                    </button>`;
                    servidoresContainer.appendChild(div);

                    // Obtengo una referencia al botón por su ID
                    const boton = document.getElementById(`${server}`);
                    boton.addEventListener('click', function() {
                        get_server(`${server}`) // Guardo los Id en sessionStorage de cada uno.
                        const container_canales = document.getElementById('channels-container') // Limpiar el container de los canales
                        container_canales.innerHTML = "";
                        idBotonGlobal = this.id;
                        // Guardar una variable en sessionStorage
                        sessionStorage.setItem('server_name', idBotonGlobal);
                        listar_canales(idBotonGlobal);
                    });

                    
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

function listar_canales(server_name) {
    // OTRO FETCH ------------------------------------------------------------------------------------
    fetch(`http://127.0.0.1:5000/channel/get/${server_name}`, {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            return response.json().then(data => {
                const canales_container = document.getElementById('channels-container');
                data.forEach(item => {
                    const div = document.createElement('div');
                    div.id = `${item.channel_name}`;
                    div.innerHTML = `<div id=${item.channel_name} class="contents2">
                                        <div>
                                            <img src="../static/icons/hashtag.png" style="width: 20px">
                                            <p class="channel-p">${item.channel_name}</p>
                                        </div>
                                        <div style="margin-right: 7px;">
                                            <div class="holder">
                                                <img src="../static/icons/add-friend.png" class="show-img">
                                                <div class="tooltip2" style="left: -280%; top: -35px">Create Invite</div>
                                            </div>
                                            <div class="holder">
                                                <img src="../static/icons/edit-channel.png" style="margin-left: 5px;" class="show-img">
                                                <div class="tooltip2" style="left: -210%; top: -35px">Edit Channel</div>
                                            </div>
                                        </div>
                                    </div>`;
                    canales_container.appendChild(div);

                    // Obtengo una referencia al botón por su ID
                    const btn_channel = document.getElementById(`${item.channel_name}`);
                    btn_channel.addEventListener('click', function() {
                        const messages_container = document.getElementById('messages-container');
                        messages_container.innerHTML = ""
                        sessionStorage.setItem('channel_name', item.channel_name)
                        let nombre_canal = sessionStorage.getItem('channel_name')
                        get_messages(nombre_canal);
                    });
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

function get_server(server_name) {
    fetch(`http://127.0.0.1:5000/server/get/${server_name}`, {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            return response.json().then(data => {
                var idServerActual = data.server_id;
                sessionStorage.setItem('id_server', idServerActual); // Guardamos el id del servidor actual en sessionStorage
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

function get_messages(channel_name) {
    fetch(`http://127.0.0.1:5000/message/get/${channel_name}`, {
        method: 'GET',
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 200) {
            return response.json().then(data => {
                data.forEach(element => {
                    // console.log(element)
                    const messages_container = document.getElementById('messages-container');
                    const div = document.createElement('div');
                    div.id = `${element.message_id}`;
                    div.innerHTML = `<div class="message">
                                        <img src="../static/images/Discord_Logo.jpg" width="46px">
                                        <div style="margin-left: 10px;">
                                            <div style="display: flex; align-items: center;">
                                                <p style="color: white; margin-right: 5px; font-size: 14px; font-weight: bold;">${element.username}</p>
                                                <div class="date" style="position: static; font-size: 11px;">${element.creation_date}</div>
                                            </div>
                                            <p style="margin-top: 5px; color: #D6D7CA; font-size: 14px">${element.content}</p>
                                        </div>
                                    </div>`;
                    messages_container.appendChild(div);
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