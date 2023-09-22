window.addEventListener('load', function () {
    getServers();
});

// window.addEventListener('load', function () {
//     getChannels();
// });

// TOMAR BOTONES PARA FUNFIONALIDADES DE UNIRSE A UN SERVIDOR O BUSCAR UNO.
// document.getElementById("addServer").addEventListener("click", addServer);
// document.getElementById("searchServer").addEventListener("click", searchServer);

function getServers() {    
    fetch("http://127.0.0.1:5000/auth/profile", {
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

    // OTRO FETCH ------------------------------------------------------------------------------------
    fetch("http://127.0.0.1:5000/channel/all", {
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
                    div.innerHTML = `<div class="contents2">
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

// function getChannels() {
//     fetch("http://127.0.0.1:5000/channel/all", {
//         method: 'GET',
//         credentials: 'include'
//     })
//     .then(response => {
//         if (response.status === 200) {
//             return response.json().then(data => {
//                 channels = data.channel_name
//                 channels.forEach(channel => {
//                     console.log(channel)
//                 });
//             });
//         } else {
//             return response.json().then(data => {
//                 document.getElementById("message").innerHTML = data.message;
//             });
//         }
//     })
//     .catch(error => {
//         document.getElementById("message").innerHTML = "An error occurred.";
//     });
// }







// btn_server.addEventListener('click', saludar)

// function saludar() {
//     console.log('click en primer btn_server')
// }

// function mostrarDiv(divId) {
//     // Ocultar todos los divs
//     document.getElementById('div1').classList.add('hidden');
//     document.getElementById('div2').classList.add('hidden');
//     document.getElementById('div3').classList.add('hidden');

//     // Mostrar el div deseado
//     document.getElementById(divId).classList.remove('hidden');
// }

// // Asignar eventos de clic a los botones
// document.getElementById('Ingles').addEventListener('click', function () {
//     saludar();
// });
// document.getElementById('Programacion Web').addEventListener('click', function () {
//     mostrarDiv('div2');
// });
// document.getElementById('Algoritmica').addEventListener('click', function () {
//     mostrarDiv('div3');
// });