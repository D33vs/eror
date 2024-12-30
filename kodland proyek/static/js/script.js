async function fetchBotReply(userMessage) {
    try {
        console.log("Sending message to backend:", userMessage);
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage }),
        });
        const data = await response.json();
        console.log("Received reply from backend:", data);
        return data.reply || "No reply received.";
    } catch (error) {
        console.error("Error fetching bot reply:", error);
        return "Something went wrong. Please try again.";
    }
}



// Toggle navigation background color on scroll
window.addEventListener("scroll", () => {
    const header = document.querySelector("header");
    if (window.scrollY > 50) {
        header.style.backgroundColor = "#0056b3";
    } else {
        header.style.backgroundColor = "#007BFF";
    }
});

// Show alert for solutions section
const solutionsButton = document.getElementById("learnMore");
solutionsButton.addEventListener("click", () => {
    alert("Learn more about how you can contribute to solutions for climate change!");
});

