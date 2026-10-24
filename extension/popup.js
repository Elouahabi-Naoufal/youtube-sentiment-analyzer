const API_URL = "http://localhost:8000/predict";

document.getElementById("analyze").addEventListener("click", async () => {
  const text = document.getElementById("text").value.trim();
  const result = document.getElementById("result");
  if (!text) { result.textContent = "Enter some text first."; return; }
  result.textContent = "Analyzing...";
  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    const data = await res.json();
    if (data.error) { result.textContent = "Error: " + data.error; return; }
    result.innerHTML = `<span class="${data.label === "positive" ? "pos" : "neg"}">${data.label}</span> (score ${data.score.toFixed(3)})`;
  } catch (e) {
    result.textContent = "Failed to reach API: " + e.message;
  }
});
