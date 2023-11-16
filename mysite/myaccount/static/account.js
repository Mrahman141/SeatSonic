function addspaceondiv() {
    var element = document.getElementById("main-information");
    if (!element.classList.contains("space")) {
        element.classList.add("space");
    }
    else {
        element.classList.remove("space");
    }
}

function removespaceondiv() {
    var element = document.getElementById("main-information");
    element.classList.remove("space");
}
