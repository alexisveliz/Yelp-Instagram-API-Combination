from bottle import route, post, request, static_file

@route('/')
def server_static(filepath="index.html"):
    return static_file(filepath, root="")

@post('/results')
def process():
    term = request.forms.get('term')
    location = request.forms.get('location')
    return "You searched for {0} in {1}".format(term, location)