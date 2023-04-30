from flask import Flask , render_template

#Create Flask Instance
app = Flask(__name__)  #This help flask find all the files

#Create a route decorator
@app.route('/')

#Filters that we can use HTML are safe , capitalize , lower , upper , title(captalize first word in sen) , trim , striptags

def index():
#     return "<h1> Hello World! </h1>"
    first_name = 'Austin'
    stuff = 'This is a <strong>Bold</strong> Tag'

    favourite_pizza = ['peproni','cheeze','paneer tikka','garlic bread' ,41]
    return render_template('index.html' ,  
                           first_name = first_name , 
                           stuff=stuff , 
                           favourite_pizza=favourite_pizza) 


@app.route('/user/<name>') #<name> This will allow to pass the name and we can pass any name
def user(name):
    # return "<h1> Hello {} !</h1>".format(name)  #Name passed in url will be printed here
    return render_template('user.html' , user_name=name)

#Create Custom Error Page

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Internal Server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)