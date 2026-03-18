// Wait for page to load
document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const input = document.querySelector("input[name='user_input']");
    
    form.addEventListener("submit", function () {
        if (input.value.trim() === "") {
            alert("Please enter something!");
        }
    });

});
