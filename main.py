from bottle import route, template, request, static_file

@route('/style.css')
def server_static(filepath="style.css"):
    return static_file(filepath, root='')

@route('/')
@route('/search')
def login():
    search_form = '''
        <form action="/results" method="post">
            Term: <input name="term" type="text" />
            Location: <input name="location" type="text" />
            <input value="Search" type="submit" />
        </form>
    '''
    return template('base', code=search_form)

@route('/results', method='POST')
def do_login():
    term = request.forms.get('term')
    location = request.forms.get('location')
    results = '<p>You searched for {0} in {1}</p>'.format(term,location)
    return template('base', code=results)