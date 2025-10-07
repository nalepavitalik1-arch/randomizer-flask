from flask import Flask, render_template_string
import random

app = Flask(__name__)

@app.route("/")
def home():
    number = random.randint(1, 6)
    return render_template_string("""
        <html>
            <head><title>Рандомайзер</title></head>
            <body style="font-family:sans-serif; text-align:center; margin-top:50px;">
                <h1>🎲 Випадкове число:</h1>
                <h2>{{ num }}</h2>
                <button onclick="window.location.reload()">Кинути ще раз</button>
            </body>
        </html>
    """, num=number)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
