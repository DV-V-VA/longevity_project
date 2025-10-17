from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    # Можно передавать контекст: статистика, секции и пр.
    stats = {
        "genes": "19,000+",
        "variants": "27,000,000+",
        "articles": "10,500,000+",
    }
    features = [
        {"title": "Clinical Diagnostics", "description": "Accelerate variant interpretation", "img": "diagnostics.png"},
        {"title": "Precision Therapeutics", "description": "Insights for drug development", "img": "therapeutics.png"},
        {"title": "Data Access", "description": "Comprehensive genomic data", "img": "data.png"},
    ]
    return render_template("index.html", stats=stats, features=features)

if __name__ == "__main__":
    app.run(debug=True)
