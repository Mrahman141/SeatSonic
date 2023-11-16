function addspaceondiv() {
    var element = document.getElementById("main-information");
    if (!element.classList.contains("space")) {
        element.classList.add("space");
    } else {
        element.classList.remove("space");
    }
}

function submitForm() {
			document.getElementById("del_acc").submit();
		}
function removespaceondiv() {
    var element = document.getElementById("main-information");
    element.classList.remove("space");
}

function togglePassword() {
    let password = document.getElementById("password");
    let button = document.querySelector(".show-password");
    if (password.type === "password") {
        password.type = "text";
        button.classList.add("active");
    } else {
        password.type = "password";
        button.classList.remove("active");
    }
}