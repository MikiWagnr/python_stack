from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "day by day, what you think and what you do is who you become"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def result():
    print('got post info')
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def form_result():
    print('displaying user info')
    print(request.form)
    return render_template('result.html', name_on_template = session['name'], location_on_template = session['location'], language_on_template = session['language'], comment_on_template = session['comment'])

if __name__=="__main__":
    app.run(debug=True)

