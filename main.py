from flask import Flask, render_template, request, redirect
import search_engine

app = Flask(__name__)
app.config.update(
    DEBUG_MODE=True
)

@app.route('/')
@app.route('/search')
def index() -> 'html': # type: ignore
    return render_template(
        'index.html',
        query='',
        results=''
    )

@app.route('/поиск')
def ru_index() -> '302': # type: ignore
    return redirect('/')

@app.route('/search', methods = ['POST'])
def do_search() -> 'html': # type: ignore
    results = str(search_engine.search4symbols(request.form['query']))
    return render_template(
        'search.html',
        query=request.form['query'],
        results=results
    )

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG_MODE'])
