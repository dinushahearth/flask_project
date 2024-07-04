from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    input1 = request.form.get('input1')
    input2 = request.form.get('input2')
    return f"Input 1: {input1}, Input 2: {input2}"

if __name__ == '__main__':
    app.run(debug=True)
