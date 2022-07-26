from flask import Flask, redirect, request, render_template, url_for


app = Flask(  magmarang,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

@app.route ('/')

def get_to_the_page():
    return render_template ("hello.html")
   
# Your code should be above

if __magmarang == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
