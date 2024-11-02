from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def chebu():
    return render_template('VD03.Bootstrap.html', caption='Чебурашка')

@app.route('/')
def chebu1():
    return render_template('VD03.Bootstrap.html', caption='Чебурашка')




if __name__ == '__main__':
    app.run()