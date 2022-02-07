from flask import Flask, render_template, request, redirect, session

app = Flask( __name__)
app.secret_key = "estoessecreto"

#1 http://127.0.0.1:5000/ GET OK
@app.route( '/', methods=['GET'] )
def despliegaClickReset():
    if "count" not in session:
        session["count"] = 1
    else:
        session['count'] += 1  #1A GET dentro de la ruta 1 '/'
    return render_template( "index.html" )

#1B
@app.route( '/reset', methods=["GET"] )
def resetlogout():
    session.clear()
    return redirect( '/' )

if __name__ == "__main__":
    app.run( debug = True )