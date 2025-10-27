from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load a simple grammar model
generator = pipeline("text-generation", model="gpt2")

@app.route("/", methods=["GET", "POST"])
def home():
    output = ""
    if request.method == "POST":
        text = request.form.get("inputText")
        if text:
            # Generate corrected text (simple example)
            result = generator(text, max_length=50, do_sample=False)
            output = result[0]['generated_text']
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)

