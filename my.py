from flask import *
app = Flask(__name__)


@app.route('/')
@app.route('/helloFossasia')
def index():
    word=request.args.get('name', '')
    word = word.strip()
    if len(word) > 0:
	return render_template('hello.html', name=word)
    return render_template('index.html')

