document.addEventListener("DOMContentLoaded", function () {
    const inputField = document.getElementById("newsInput");
    const resultDiv = document.getElementById("result");

    // Classify text
    document.getElementById("classifyBtn").addEventListener("click", async () => {
        const newsText = inputField.value.trim();
        if (!newsText) {
            resultDiv.innerHTML = "<p style='color:red;'>⚠️ Please enter some text.</p>";
            return;
        }
        resultDiv.innerHTML = "<p>⏳ Analyzing...</p>";

        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
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

    // Fetch live news
    document.getElementById("fetchBtn").addEventListener("click", async () => {
        const query = inputField.value.trim();
        if (!query) {
            resultDiv.innerHTML = "<p style='color:red;'>⚠️ Please enter a keyword.</p>";
            return;
        }
        resultDiv.innerHTML = "<p>⏳ Fetching news...</p>";

        try {
            const res = await fetch(`/get_news?q=${encodeURIComponent(query)}`);
            const articles = await res.json();
            resultDiv.innerHTML = "";
            articles.forEach(a => {
                resultDiv.innerHTML += `<p><a href="${a.url}" target="_blank">${a.title}</a> → ${a.prediction}</p>`;
            });
        } catch (error) {
            resultDiv.innerHTML = "<p style='color:red;'>⚠️ Error: Could not fetch news.</p>";
            console.error("Error:", error);
        }
    });
    const toggleBtn = document.getElementById("toggleTheme");
    toggleBtn.addEventListener("click", () => {
     document.body.classList.toggle("dark-mode");
});

resultDiv.innerHTML += `<p><a href="${a.url}" target="_blank">${a.title}</a> → ${a.prediction}</p>`;
articles.forEach(a => {
    const cls = a.prediction === "FAKE" ? "fake-link" : "real-link";
    resultDiv.innerHTML += `<p><a href="${a.url}" target="_blank" class="${cls}">${a.title}</a> → ${a.prediction}</p>`;
});
});