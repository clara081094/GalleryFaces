
from flask import Flask, render_template
import os
# Import the images dictionary
#from models.images import images

app = Flask(__name__)


@app.route('/caras')
def hello_world():
    # Pass the images dictionary data to the gallery page

    lista=[]
    path="/home/ubuntu/proyectos/microservicePlatanitos/pictures/"

    cameras = os.listdir(path)
    for camera in cameras:
        images=os.listdir(path+str(camera)+"/registered/")
        for face in images:
            item ={"camera":camera,"face":face}
            lista.append(item)

    return render_template('views/gallery.html',
    faces=lista)


if __name__ == '__main__':
    app.run(debug=True,port=8000)





