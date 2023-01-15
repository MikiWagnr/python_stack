from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "with great power, there must also come great responsibily"

@app.route('/')
def counting_views():
    if 'views' in session:
        session['views'] += 1
    else:
        session['views'] = 1
    return render_template("index.html")

@app.route('/add2')
def increase_by2():
    session['views']+=1
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)