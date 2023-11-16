function togglePassword() {
    var passwordField = document.getElementById("user_password");
    var passwordField_c = document.getElementById("user_confirm_password");

    var showPasswordIcon = document.querySelector(".show-password-btn i");
    var showPasswordIcon_c = document.querySelector(".show-c-password-btn i");

    if (passwordField.type === "password") {
        passwordField_c.type = "text"
        passwordField.type = "text";
        showPasswordIcon.classList.remove("fa-eye");
        showPasswordIcon.classList.add("fa-eye-slash");
        showPasswordIcon_c.classList.remove("fa-eye");
        showPasswordIcon_c.classList.add("fa-eye-slash");
    } else {
        passwordField_c.type = "password"
        passwordField.type = "password";
        showPasswordIcon.classList.remove("fa-eye-slash");
        showPasswordIcon.classList.add("fa-eye");
        showPasswordIcon_c.classList.remove("fa-eye-slash");
        showPasswordIcon_c.classList.add("fa-eye");
    }
}