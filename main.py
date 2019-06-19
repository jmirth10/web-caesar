from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
        <label for="rot">Rotate by:<input type="text name="rot" value="0"></label>    
        <textarea name="text"></textarea>
        <input type="submit" value="Submit">
        
    </body>
</html>
"""

@app.route('/', methods=["POST"])
def encrypt():
    text = request.form["text"]
    rot = int(request.form["rot"])
    encrpyted_text = rotate_string(text, rot)
    return form.format(encrpyted_text)

@app.route("/")
def index():
    content = form
    return form.format(content)

app.run()