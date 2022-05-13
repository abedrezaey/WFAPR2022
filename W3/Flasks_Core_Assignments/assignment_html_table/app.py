from flask import Flask, render_template

app = Flask(__name__) 


@app.route('/')        
def users_list ():
    
    user_info = [
        {'first_name' : 'Michael', 'last_name' : 'Choi', 'full_name' : 'Micaheil Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin', 'full_name' : 'John Supsuping'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'full_name' : 'Mark Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel', 'full_name' : 'KB Tonel'}
        ]
    return render_template("table.html", users = user_info)


if __name__=="__main__": 
    app.run(host = 'localhost', debug=True) 

