from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True   

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Caesar: Not Code for Salad</title>
    </head>
    <body>
        <h1>Caesar: Not Code for Salad</h1>
"""

page_footer = """
    </body>
</html>
"""

input_form = """
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
        <form action="/input" method="POST">
        <label>
            I want to rotate by
            <input type="text" name ="rot" value="0"/>
            <br><br><br>
            My message is
            <textarea input type="text" name="text"/>{0}</textarea>
        </label>
        <br><br>
        <input type="submit" value="Encode"/>
    </body>
</html>
"""




@app.route("/input", methods=["POST"])
def encrypt():
    rotation = int(request.form['rot'])
    message = request.form['text']
    code = rotate_string(message, rotation)
    display = page_header + "<p>" + input_form.format(code) + "</p>" + page_footer
    return display


@app.route("/")
def index():
    start = ""
    summary = page_header + input_form.format(start) + page_footer
    return summary 



app.run() 



