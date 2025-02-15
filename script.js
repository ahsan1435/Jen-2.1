function sendMessage() {
    let inputField = document.getElementById("userInput");
    let userText = inputField.value.trim();

    if (userText === "") return;

    // Add User Message
    addMessage(userText, "user-message");

    // Simulate AI typing effect
    setTimeout(() => {
        addMessage("I'm still learning, Sir. Can you rephrase that?", "bot-message");
    }, 1000);

    inputField.value = "";
}

function addMessage(text, className) {
    let messageContainer = document.getElementById("messages");
    let messageDiv = document.createElement("div");
    messageDiv.className = className;
    messageDiv.textContent = text;
    messageContainer.appendChild(messageDiv);

    // Scroll to the bottom
    messageContainer.scrollTop = messageContainer.scrollHeight;
}
