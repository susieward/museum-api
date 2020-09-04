
from flask import Flask

app = Flask(__name__)

from main import main_bp as main_bp
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug = True)
