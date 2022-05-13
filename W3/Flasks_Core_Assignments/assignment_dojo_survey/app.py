from flask import Flask, render_template, redirect, flash, request, session


app = Flask(__name__)
app.secret_key = "HelloowWorld!"



@app.route('/')
def index():
      return render_template("index.html")


@app.route("/submission", methods=["GET", "POST"])
def submission():
      print(request.form)
      return render_template("submission.html")

      






@app.route('/')
def back ():
      session.clear()
      return redirect('/')




if __name__ == "__main__":

      app.run(debug=True)