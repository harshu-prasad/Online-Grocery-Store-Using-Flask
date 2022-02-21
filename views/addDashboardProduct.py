from flask import Blueprint,render_template # Importing Blueprint to handle routes related to addDashboardProduct page

addDashboardProduct = Blueprint('addDashboardProduct',__name__,static_folder='static',template_folder='templates') # Creating a Blueprint so that it could be accesed from files from outside

@addDashboardProduct.route('/')
def renderAddDashboardProductPage():
    ''' This is the function that will run when someone called for '/' route '''
    return render_template('addDashboardProduct.html') # Rendering addDashboardProduct.html page