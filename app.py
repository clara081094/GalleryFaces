
from flask import Flask, render_template

# Import the images dictionary
from models.images import images

app = Flask(__name__)


@app.route('/')
def hello_world():
    # Pass the images dictionary data to the gallery page
    return render_template('views/gallery.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)





