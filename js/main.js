function sendLogin() {
    var name = document.getElementById('username').value;
    var pd = document.getElementById('password').value;
    sendRequest("POST", "http://127.0.0.1:8000/login", { "username": name, "password": pd });
}

function sendRegister() {
    var name = document.getElementById('usernameReg');
    var pd = document.getElementById('passwordReg');
    var email = document.getElementById('email');
    sendRequest("POST", "http://127.0.0.1:8000/register", { "username": name, "password": pd, "email": email });
}

function sendHi() {
    sendRequest("GET", "http://127.0.0.1:8000/hi")
}

function sendRequest(method, url, jsonData = null) {
    var xhr = new XMLHttpRequest();
    xhr.open(method.toUpperCase(), url, true);
    xhr.setRequestHeader("content-type", "application/json");
    xhr.setRequestHeader("Access-Control-Allow-Origin", "*");

    access_token = localStorage.getItem("access_token");
    refresh_token = localStorage.getItem("refresh_token");
    xhr.setRequestHeader("access_token", access_token);
    xhr.setRequestHeader("refresh_token", refresh_token);

    xhr.onreadystatechange = function () {
        if (url.endsWith("login")) {
            if (xhr.readyState === 4) {
                console.log(xhr.response)
                saveJwt(xhr.response);
            }
        }
    };
    xhr.send(JSON.stringify(jsonData));
}

// 从请求中抽取jwt，保存到localStorage
function saveJwt(body) {
    body = JSON.parse(body);
    if (!("access_token" in body["data"]) || !("refresh_token" in body["data"])) {
        console.log("no token inside")
        return;
    }
    localStorage.setItem("access_token", body["data"]["access_token"]);
    localStorage.setItem("refresh_token", body["data"]["refresh_token"]);
}