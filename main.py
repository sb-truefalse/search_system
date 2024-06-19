from flask import Flask, render_template, request, redirect
from markupsafe import escape
import search_engine

app = Flask(__name__)

if __name__ == '__main__':
    app.config.update(
        DEBUG_MODE=True,
        SHOW_LOGS=True,
        LOGS_PATH='logs/development.log'
    )
else:
    app.config.update(
        DEBUG_MODE=False,
        SHOW_LOGS=False,
        LOGS_PATH='logs/production.log'
    )

def log_request(flask_request: 'flask_request', data: str) -> None: # type: ignore
    """Logs the data for the request"""
    with open(app.config['LOGS_PATH'], 'a') as logs:
        print(
            flask_request.form,
            flask_request.remote_addr,
            flask_request.user_agent,
            data,
            file=logs,
            sep='|'
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
    """Search for unique characters"""
    results = str(search_engine.search4symbols(request.form['query']))
    log_request(request, results)
    return render_template(
        'search.html',
        query=request.form['query'],
        results=results
    )

if app.config['SHOW_LOGS']:
    @app.route('/logs')
    def show_logs() -> 'html': # type: ignore
        data = []
        with open(app.config['LOGS_PATH']) as logs:
            for log in logs:
                data.append([])
                for item in log.split('|'):
                    data[-1].append(escape(item))
        return render_template(
            'logs.html',
            data=data
        )

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG_MODE'])
