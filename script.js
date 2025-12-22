// static/script.js

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("newsForm");
    const inputField = document.getElementById("newsInput");
    const resultDiv = document.getElementById("result");
    const toggleBtn = document.getElementById("toggleTheme"); 

    // --- Form submission handler ---
    form.addEventListener("submit", async function (e) {
        e.preventDefault(); // prevent page reload

        const newsText = inputField.value.trim();
        if (!newsText) {
            resultDiv.innerHTML = "<p style='color:red;'>⚠️ Please enter some text.</p>";
            return;
        }

        resultDiv.innerHTML = "<p>⏳ Analyzing...</p>";

        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ text: newsText })
            });

            const data = await response.json();

            if (data.prediction === "FAKE") {
                resultDiv.innerHTML = "<p style='color:red; font-weight:bold;'>❌ Fake News Detected!</p>";
            } else if (data.prediction === "REAL") {
                resultDiv.innerHTML = "<p style='color:green; font-weight:bold;'>✅ This news seems Real.</p>";
            } else {
                resultDiv.innerHTML = "<p style='color:gray;'>🤔 Unable to classify.</p>";
            }
        } catch (error) {
            resultDiv.innerHTML = "<p style='color:red;'>⚠️ Error: Could not connect to server.</p>";
            console.error("Error:", error);
        }
    });

    // --- Dark mode toggle handler ---
    if (toggleBtn) {
        toggleBtn.addEventListener("click", () => {
            document.body.classList.toggle("dark-mode");
        });
    }
});