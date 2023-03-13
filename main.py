from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    with open('templates/base.html', 'r', encoding='utf-8') as f:
        return f.read().replace('{{ title }}', title).replace('{{ style_main }}', url_for('static', filename='css/style_main.css'))


@app.route('/training/<prof>')
def training(prof):
    with open('templates/training.html', 'r', encoding='utf-8') as f:
        if 'строитель' in prof.lower():
            prof = 'строитель'
        elif 'инженер' in prof.lower():
            prof = 'инженер'
        img = prof + '_img.png'
        return f.read().replace('{{ title }}', prof).replace('{{ style_main }}', url_for('static', filename='css/style_main.css')).replace('{{ image }}', url_for('static', filename='img/' + img))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')