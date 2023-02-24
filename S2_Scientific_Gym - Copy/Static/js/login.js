const login_btn = document.getElementById('login')
const register_btn = document.getElementById('register')
const toggle_btn = document.getElementById('btn')

function register() {
    login_btn.style.left = "-400px"
    register_btn.style.left = "50px";
    toggle_btn.style.left = "110px";
}


function login() {
    login_btn.style.left = "50px"
    register_btn.style.left = "450px";
    toggle_btn.style.left = "0px";
}