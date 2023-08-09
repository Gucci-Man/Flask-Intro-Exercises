from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/welcome")
def welcome():
    """View that responds with 'Welcome'"""
    html = """
    <html>
        <body>
            <h1>welcome</h1>
        </body>
    </html>
    """
    return html


@app.route("/welcome/home")
def welcome_home():
    """View that responds with 'Welcome bome"""
    html = """
    <html>
        <body>
            <h1>welcome home</h1>
        </body>
    </html>
    """
    return html


@app.route("/welcome/back")
def welcome_back():
    """View that responds with 'Welcome back"""
    html = """
    <html>
        <body>
            <h1>welcome back</h1>
        </body>
    </html>
    """
    return html
