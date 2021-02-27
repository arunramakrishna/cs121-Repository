# % PYTHON_BIN_PATH="$(python3 -m site --user-base)/bin"

# % PATH="$PATH:$PYTHON_BIN_PATH"

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, cs121 World"