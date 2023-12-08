from flask import Flask, render_template, request, redirect

from app_flask.usuarios import Usuario

app=Flask(__name__, template_folder='app_flask')

@app.route('/')
def index():
    return render_template('new_user.html')


@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    Usuario.save(request.form)
    return redirect('/users')


#correccion para que se vea la lista de usuarios
@app.route('/users')
def new():
    usuarios = Usuario.get_all()
    return render_template("users.html", usuarios=usuarios)



if __name__=="__main__":
    app.run(debug=True)