"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Start Here</title>
      </head>
      <body>
        <a href="/hello">Take me to the start</a>
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <p>
          <label for="compliment-options"> Choose a compliment:</label>
          <select name="compliment" id="compliment-options">
            <option value="awesome">Awesome</option>
            <option value="terrific">Terriric</option>
            <option value="fantastic">Fantastic/option>
            <option value="wonderful">Wonderful</option>
            <option value="lovely">Lovely</option>
          </select>
          </p>
          <input type="submit" value="Submit">
        </form>
        <form action="/diss">   
          What's your name? <input type="text" name="person">     
            <p>
            <label for="diss-options"> Choose a diss:</label>
            <select name="diss" id="diss-options">
              <option value="annoying">Annoying</option>
              <option value="ugly">Ugly</option>
              <option value="loud">Loud</option>        
            </select>
            </p>
            <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person").title()

    compliment = request.args.get("compliment").lower()

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route('/diss')
def diss_user():
    """Diss the user"""

    player = request.args.get("person").title()

    diss = request.args.get("diss").lower()

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
