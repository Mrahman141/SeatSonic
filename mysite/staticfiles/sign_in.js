function togglePassword() {
    var passwordField = document.getElementById("login_password");
    var showPasswordIcon = document.querySelector(".show-password i");
    if (passwordField.type === "password") {
        passwordField.type = "text";
        showPasswordIcon.classList.remove("fa-eye");
        showPasswordIcon.classList.add("fa-eye-slash");
    } else {
        passwordField.type = "password";
        showPasswordIcon.classList.remove("fa-eye-slash");
        showPasswordIcon.classList.add("fa-eye");
    }
}