from flask import Flask, render_template, request, redirect 
from user import User

app = Flask(__name__)


# CREATE
@app.route('/users/new')
def creat_user():
    return render_template('new.html')


@app.route('/users/create', methods=['POST'])
def result():
    print(request.form)
    User.save(request.form)
    return redirect('/')



# READ ALL
@app.route('/')
def index():
    return render_template('index.html', users = User.get_all())


# READ ONE
@app.route("/users/<int:id>")
def get_user(id):
    data = {'id': id}
    return render_template('show.html', user = User.get_one(data))


# UPDATE
@app.route('/users/edit/<int:id>')
def edit_user(id):
    data = {'id': id}
    return render_template('edit.html', user = User.get_one(data))

@app.route('/users/update', methods = ["POST"])
def update_user():
    User.update(request.form)
    print(request.form)
    return redirect('/')

# DELETE
@app.route('/users/delete/<int:id>')
def delete(id):
    data = {'id': id}
    User.delete(data)
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)
