document.addEventListener("click", function (e){
    if(e.target.classList.contains("gallery-item")) {
        const src = e.target.getAttribute("src");
        document.querySelector(".modal-img").src = src;
        const myModal = new bootstrap.Modal(document.getElementById('gallery-modal'));
        myModal.show();
    }
})
const signInBtn = document.querySelector(".signin-button")
const signUpBtn = document.querySelector(".signup-button")
const formBox = document.querySelector(".form-box")
const loginBody = document.querySelector(".login-body")

signUpBtn.addEventListener('click', function () {
    formBox.classList.add('active');
    loginBody.classList.add('active');
});

signInBtn.addEventListener('click', function () {
    formBox.classList.remove('active');
    loginBody.classList.remove('active');

});