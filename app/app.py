from flask import Flask, render_template, make_response
from models import ItemModel

app = Flask(__name__)
model = ItemModel()

@app.route('/')
def index():
    # Контроллер запрашивает данные у модели
    items = model.get_all_items()
    # И передает их в представление (шаблон)
    response = make_response(render_template('index.html', items=items))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
