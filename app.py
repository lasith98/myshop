from flask import Flask, jsonify, request
from resmem import ResMem, transformer
from PIL import Image

model = ResMem(pretrained=True)
model.eval()

def image_process(raw_img):
    img = Image.open(raw_img)
    img = img.convert('RGB')
    image_x = transformer(img)
    return image_x


def prediction(image_x):
    result = model(image_x.view(-1, 3, 227, 227))
    return result


app = Flask(__name__)
@app.route('/predict', methods=['GET', 'POST'])
def predict_image():
    file = request.files.get('file')
    image_z = image_process(file)
    return jsonify(prediction(image_z))


@app.route('/', methods=['GET'])
def index():
    return "welcome"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')