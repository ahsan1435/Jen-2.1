function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") return;

    let chatBox = document.getElementById("chat-box");

    // Add user message to chat
    let userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.textContent = userInput;
    chatBox.appendChild(userMessage);

    // Simulate bot response
    setTimeout(() => {
        let botMessage = document.createElement("div");
        botMessage.className = "bot-message";
        botMessage.textContent = getBotResponse(userInput);
        chatBox.appendChild(botMessage);

        chatBox.scrollTop = chatBox.scrollHeight;
    }, 500);

    document.getElementById("user-input").value = "";
}

// Simple bot response function (replace with AI later)
function getBotResponse(input) {
    let responses = {
        "hello": "Hi there!",
        "how are you?": "I'm just a bot, but I'm doing great!",
        "bye": "Goodbye! Have a great day!"
    };
    return responses[input.toLowerCase()] || "I'm still learning. Can you rephrase that?";
            }
