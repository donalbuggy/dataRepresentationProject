from flask import Flask, jsonify, request, abort, session, url_for, redirect
from moviesDB import movieDB

app = Flask(__name__, static_url_path='', static_folder='staticpages')
app.secret_key = "secretrg56ugfwr43rh"

# app = Flask(__name__)

movies = [
    {"id":1,"title":"The Shining","director":"Stanley Kubrick","year":"1980","rating":"8.4"},
    {"id":2,"title":"The Irishman","director":"Martin Scorsese","year":"2019","rating":"7.8"},
    {"id":3,"title":"The Hateful Eight","director":"Quentin Tarantino","year":"2015","rating":"7.8"},
    {"id":4,"title":"Django Unchained","director":"Quentin Tarantino","year":"2012","rating":"8.4"},
    {"id":5,"title":"Les Miserables","director":"Tom Hooper","year":"2012","rating":"7.5"},
    {"id":6,"title":"Zodiac","director":"David Fincher","year":"2007","rating":"7.7"},
    {"id":7,"title":"Barry Lyndon","director":"Stanley Kubrick","year":"1975","rating":"8.1"},
    {"id":8,"title":"Mean Streets","director":"Martin Scorsese","year":"1973","rating":"7.2"}
]
newId = 8
@app.route('/')
def home():
    if not 'username' in session:
        return redirect(url_for('login'))
    else:
        return redirect('/movies.html')
    
    # return 'welcome ' + session['username'] +\
    #     '<br><a href="' + url_for('logout') + '">logout</a>'


@app.route('/login')
def login():
    return '<h1>login</h1> ' +\
        '<button>' +\
            '<a href="' + url_for('process_login') + '">' +\
                'login' +\
            '</a>' +\
        '</button>'


@app.route('/process_login')
def process_login():
    session['username'] = "Donal"
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))


# @app.route('/data')
# def getData():
#     if not 'username' in session:
#         abort(401)
#     # user is authoristed
#     return '{"data":"all here"}'


@app.route('/movies', methods=['GET'])
def getAllMovies():
    return movies


@app.route('/movies', methods=['POST'])
def addMovie():
    if not request.json:
        abort(400)

    global newId

    movie = {
        "title": request.json['title'],
        "director": request.json['director'],
        "year": request.json['year'],
        "rating": request.json['rating']
    }

    values = (movie['title'],movie['director'],movie['year'])
    newId = newId + 1
    movie['id'] = newId
    return jsonify(movie)


@app.route('/movies/<int:id>', methods=['PUT'])
def updateEntry(id):
    foundMovie = movieDB.findById(id)
    if not foundMovie:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'year' in reqJson and type(reqJson['year']) is not int:
        abort(400)
    if 'rating' in reqJson and type(reqJson['rating'] is not float):
        abort(400)
    if 'title' in reqJson:
        foundMovie['title'] = reqJson['title']
    if 'director' in reqJson:
        foundMovie['director'] = reqJson['author']
    if 'year' in reqJson:
        foundMovie['year'] = reqJson['year']
    if 'rating' in reqJson:
        foundMovie['rating'] = reqJson['rating']
    values = (foundMovie['title'],foundMovie['director'],foundMovie['year'],foundMovie['rating'],foundMovie['id'])
    movieDB.updateEntry(values)
    return jsonify(foundMovie)


@app.route('/movies/<int:id>', methods=['DELETE'])
def deleteEntry(id):
    movieDB.deleteEntry(id)
    return jsonify({"done":True})



if __name__ == "__main__":
    app.run(debug=True)