from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/welcome")
def welcome():
    html = """
    <html>
        <body>
            <h1>Welcome</h1>
        </body>
    </html>
    """
    return html
