
from flask import Flask, render_template
from models.images import images

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template(
        'views/gallery.html',
        images=images)


if __name__ == '__main__':
    app.run(debug=True)





