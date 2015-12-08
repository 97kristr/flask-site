"""Author: krille, 2015"""


from flask import Flask,render_template
#importerar flask och render_template

app = Flask(__name__)
#starta flask_app

@app.route('/')
#@ före en funktion är en creator
@app.route('/startpage/')
#en hemsida kan ha flera sidor

def startpage():
    #funktionen som startar sidan.
    return render_template("startpage.html")
    #skickar tillbaka en "return" till klienten
    

if (__name__ == "__main__"):
    #name=filen vi är i, main=filen vi executerar.
    app.run()
    #kör appen