from flask import Flask, render_template, request, redirect, session, url_for, flash, make_response

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def home():

      if "count" not in session:
            session["count"] = 1
      else:
            session["count"] +=1

      return render_template ("index.html")



@app.route('/reset')
def reset_counter():
      session.clear()
      return redirect('/')
      



if __name__ == '__main__':
      app.run(debug=True)

