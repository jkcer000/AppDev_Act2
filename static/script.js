function addMessage(text, sender) {
    const chat = document.getElementById("chat");

    let msg = document.createElement("p");
    msg.innerText = text;

    if (sender === "user") {
        msg.style.textAlign = "right";
    }

    chat.appendChild(msg);
}
