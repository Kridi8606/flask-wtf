from flask import Flask, url_for, request

app = Flask(__name__)

lst = ['Инженер-исследователь',
'Пилот',
'Строитель',
'Экзобиолог',
'Врач',
'Инженер по терраформированию',
'Климатолог',
'Специалист по радиационной защите',
'Астрогеолог',
'Гляциолог',
'Инженер жизнеобеспечения',
'Метеоролог',
'Оператор марсохода',
'Киберинженер',
'Штурман',
'Пилот дронов']

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


@app.route('/list_prof/<list>')
def list_prof(list):
    with open('templates/list_prof.html', 'r', encoding='utf-8') as f:
        html = f.read()
    list_text = ''
    for i in lst:
        list_text += '<li>' + i + '</li>'
    if list not in ['ol', 'ul']:
        list = 'ol'
        html += '<h1>Вы неверно ввели тип списка,<br>так что я вас не послушал и поставил тип на своё усмотрение</h1>'
    html = html.replace('{{ type }}', list).replace('{{ list }}', list_text).replace('{{ style_main }}', url_for('static', filename='css/style_main.css'))
    return html



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')