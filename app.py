from flask import Flask
import main

app = Flask(__name__)

@app.route("/start")
def start():
    main.main()
    return "Voice assistant finished."

if __name__ == "__main__":
    app.run(debug=True)