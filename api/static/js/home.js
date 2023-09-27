window.addEventListener('DOMContentLoaded', function () {
    getServers();
});

// var server_name = sessionStorage.getItem('server_name')
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
                                                <div id="btnEditChannel" class="tooltip2" style="left: -280%; top: -35px">Edit channel</div>
                                            </div>
                                            <div class="holder">
                                                <img src="../static/icons/edit-channel.png" style="margin-left: 5px;" class="show-img">
                                                <div id="btnEditChannel" class="tooltip2" style="left: -210%; top: -35px">Delete channel</div>
                                            </div>
                                        </div>
                                    </div>`;
                    canales_container.appendChild(div);

                    // Obtengo una referencia al botón por su ID
                    const btn_channel = document.getElementById(`${item.channel_name}`);
                    btn_channel.addEventListener('click', function() {
                        const messages_container = document.getElementById('messages-container');
                        messages_container.innerHTML = ""
                        sessionStorage.setItem('channel_name', item.channel_name) // Guardo el nombre del canal en la sessionStorage
                        sessionStorage.setItem('channel_id', item.channel_id) // Guardo el id del canal en la sessionStorage
                        let nombre_canal = sessionStorage.getItem('channel_name')
                        get_messages(nombre_canal);
                        // Verificar si hay mensajes, en caso que no hayan mensajes mostrar un mensaje.
                        // if (messages_container.innerHTML.trim() === "") {
                        //     messages_container.innerHTML = "No hay mensajes.";
                        // }
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
                                        <div style="margin-right: 10px;">
                                            <div style="display: flex; align-items: center;">
                                                <button id="${element.message_id}" class="btnEditMessage">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil" viewBox="0 0 16 16">
                                                    <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z"/>
                                                    </svg>
                                                </button>
                                                <button id="${element.message_id}" class="btnDeleteMessage">
                                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3" viewBox="0 0 16 16">
                                                    <path d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5ZM11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H2.506a.58.58 0 0 0-.01 0H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1h-.995a.59.59 0 0 0-.01 0H11Zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5h9.916Zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47ZM8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5Z"/>
                                                    </svg>
                                                </button>
                                            </div>                                            
                                        </div>
                                    </div>`;
                    messages_container.appendChild(div);
                    // Desplazar automáticamente el contenedor hacia abajo para mostrar el mensaje más reciente
                    messages_container.scrollTop = messages_container.scrollHeight;

                    // Asignale un evento a todos los botones con la clase: btnDeleteMessage
                    var btnsDelete = document.querySelectorAll(".btnDeleteMessage");
                    btnsDelete.forEach(function(boton) {
                        boton.addEventListener("click", function () {
                            let message_id = boton.id // Tomamos el Id de la clase de cada boton.
                            sessionStorage.setItem('message_id', message_id) // Guardamos el id del mensaje en sessionStorage
                            deleteMessage()
                        })
                    });

                    // Asignale un evento a todos los botones con la clase: btnEditMessage
                    var btnsEdit = document.querySelectorAll(".btnEditMessage");
                    var ejecutado = false;
                    btnsEdit.forEach(function(boton) {
                        boton.addEventListener("click", function () {
                            message_id = boton.id // Tomamos el Id de la clase de cada boton.
                            sessionStorage.setItem('message_id_edit', message_id) // Guardamos el id del mensaje en sessionStorage
                            editMessage()
                        })
                    });
                });
            });
        } else {
            return response.json().then(data => {
                console.log(data.message)
            });
        }
    })
    .catch(error => {
        document.getElementById("message").innerHTML = "An error occurred.";
    });
}


const cajaMensajes = document.getElementById('messages-container')
const btnEnviar = document.getElementById('btnEnviar')
const inputMensaje = document.getElementById('messageContent')

btnEnviar.addEventListener('click', sendMessage);

function sendMessage() {
    const data = {
        content: document.getElementById("messageContent").value,
        user_id: sessionStorage.getItem('user_id'),
        channel_id: sessionStorage.getItem('channel_id')
    };
    // console.log(data)

    let message = inputMensaje.value.trim()
    let username = sessionStorage.getItem('user')
    let fechaYHora = new Date();
    if (message !== ''){
        let nuevoMensaje = document.createElement('div');
        nuevoMensaje.classList.add('message');
        nuevoMensaje.innerHTML = `<img src="../static/images/Discord_Logo.jpg" width="46px">
                                    <div style="margin-left: 10px;">
                                        <div style="display: flex; align-items: center;">
                                            <p style="color: white; margin-right: 5px; font-size: 14px; font-weight: bold;">${username}</p>
                                            <div class="date" style="position: static; font-size: 11px;">${fechaYHora.toTimeString().split(' ')[0]}</div>
                                        </div>
                                        <p style="margin-top: 5px; color: #D6D7CA; font-size: 14px">${message}</p>
                                    </div>`;
        cajaMensajes.appendChild(nuevoMensaje);
        inputMensaje.value = '';
        inputMensaje.focus();

        fetch("http://127.0.0.1:5000/message/add", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        credentials: 'include'
        })
        .then(response => {
            if (response.status === 201) {
                // Redirect to profile page if login is successful
                return response.json().then(data => {
                    // console.log(data)
                    // window.location.href = "homeDiscord.html";
                });
            } else {
                return response.json().then(data => {
                    console.log(data)
                });
            }
        })
        .catch(error => {
            document.getElementById("message").innerHTML = "An error occurred.";
        });

    } else {
        console.log('Llena el mensaje con contenido porfavor...')
    }
}


function deleteMessage() {
    const data = {
        message_id: sessionStorage.getItem('message_id'),
        user_id: sessionStorage.getItem('user_id')
    };
    // console.log(data)

    fetch("http://127.0.0.1:5000/message/delete", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        credentials: 'include'
        })
        .then(response => {
            if (response.status === 200) {
                // Redirect to profile page if login is successful
                return response.json().then(data => {
                    console.log(data.message)
                    window.location.href = "homeDiscord.html";
                });
            } else {
                return response.json().then(data => {
                    console.log(data.message)
                });
            }
        })
        .catch(error => {
            document.getElementById("message").innerHTML = "An error occurred.";
        });

}

function editMessage() {
    const data = {
        message_id: sessionStorage.getItem('message_id_edit'),
        user_id: sessionStorage.getItem('user_id')
    };
    console.log(data)
}



const btnExitServer = document.getElementById('btn-Exit-Server');
btnExitServer.addEventListener('click', exitServer);

function exitServer() {
    const data = {
        user_id: sessionStorage.getItem('user_id'),
        server_id: sessionStorage.getItem('id_server')
    }
    console.log('Saliendo del servidor...')
    console.log(data)

    fetch("http://127.0.0.1:5000/suscription/exit", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
        credentials: 'include'
    })
    .then(response => {
        if (response.status === 201) {
            // Redirect to profile page if login is successful
            return response.json().then(data => {
                window.location.href = "homeDiscord.html";
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