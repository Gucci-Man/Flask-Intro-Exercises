from operations import *
from flask import Flask, request

app = Flask(__name__)


@app.route("/add")
def add_route():
    """View that returns the addition of a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(add(a, b))


@app.route("/sub")
def sub_route():
    """View that returns the difference of a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(sub(a, b))


@app.route("/mult")
def mult_route():
    """View that returns the product of a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(mult(a, b))


@app.route("/div")
def div_route():
    """View that returns the quotient of a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(div(a, b))


@app.route("/math/<oper>")
def all_route(oper):
    """View that returns the answer dependent on the operation requested"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    if oper == "add":
        return str(add(a, b))

    elif oper == "sub":
        return str(sub(a, b))

    elif oper == "mult":
        return str(mult(a, b))

    elif oper == "div":
        return str(div(a, b))
