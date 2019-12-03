# Main Program for Restaurant Vibes
# Collects all files to create a web app at http://localhost:8080 using Bottle
#
# Owners: Haley Anderson, Aimee Bowen, Alejandro Ferrer-Peasley, Elise Mayo, Alexis Veliz
# Date: November 19, 2019

from bottle import route, template, request, static_file, run #http://bottlepy.org
import Connection as Connection

restaurant = ""

# adds the main CSS styles
@route('/style.css')
def server_static(filepath="style.css"):
    return static_file(filepath, root='')

# Home/Search: Creates a form for searching for a term & location and applies the base HTML layout
@route('/')
@route('/search')
def search():
    search_form = '''
        <div class="titles">
            <h1>Restaurant Vibes</h1>
            <h2>Search</h3>
        </div>
        <form id="search" action="/results" method="post">
            <div class="search_info">Term: </div>
            <select name="term">
                <option value="thai">Thai</option>
            </select>
            <div class="search_info">Location: </div>
            <select name="location">
                <option value="los angeles">Los Angeles</option>
                <option value="san francisco">San Francisco</option>
                <option value="seattle">Seattle</option>
            </select>
            <input value="Search" type="submit" />
        </form>
    '''
    return template('base', code=search_form)

# Results: Gets the user input from the above form and prints what the search terms were
# TODO: Create a new template for results that outputs the dictionary as links 
@route('/results', method='POST')
def show_results():
    term = request.forms.get('term')
    location = request.forms.get('location')
    results_dict = Connection.YelpSearch(location,term)
    restaurant_link = "<a href=/restaurant>" + results_dict['name'] + "</a>"
    return template('base', code=restaurant_link)
    

#TODO: Create a template that gets Instagram images and Yelp info and displays them
@route('/restaurant')
def show_info():
    return template('base', code="Results")

# Generates the webpages at http://localhost:8080 in debug mode
run(host='localhost', port=8080, debug=True)