from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('two.html', prof=prof)

@app.route('/list_prof/<list>')
def list_prof(list):
    return render_template('three.html', list=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
