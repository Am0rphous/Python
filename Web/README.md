# Web

- [https://gunicorn.org/](https://gunicorn.org/) - Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.
- [Pynecone](https://github.com/pynecone-io/pynecone) - 🕸 Web apps in pure Python 🐍


### Web servers
````python
python -m http.server 8000
python3 -m http.server 8000
python3 -m http.server 8000 --bind 127.0.0.1 --ssl-cert server.pem --ssl-key server.key #only accessible to localhost
python3 -m http.server 8000 --bind 0.0.0.0 --ssl-cert server.pem --ssl-key server.key #open for every interface
````
[Updog](https://github.com/sc0tfree/updog) - Updog is a replacement for Python's SimpleHTTPServer. It allows uploading and downloading via HTTP/S, can set ad hoc SSL certificates and use http basic auth.

<details open>
  <summary><h4 style="display: inline-block; font-size: 18px; font-weight: bold;">
      Using Flask
  </h4></summary>

````python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(ssl_context=('server.pem', 'server.key'))
````
</details>




<details open><summary><h4 style="display: inline-block; font-size: 18px; font-weight: bold;">Use a specific/vulnerable Flask version</h4></summary>
    
1. Specify an old flask version `pip install Flask>=1.0.0`

````python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(ssl_context=('server.pem', 'server.key'))
````
</details>





<details open><summary><h4 style="display: inline-block; font-size: 18px; font-weight: bold;">
  Create a vulnerable Flask app
</h4></summary>
    
1. Specify an old flask version `pip install Flask>=1.0.0`

````python
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip_address = request.form['ip_address']
        result = subprocess.run(['ping', '-c', '4', ip_address], capture_output=True, text=True)
        return render_template_string('''
            <html>
              <head>
                <title>Ping Result</title>
              </head>
              <body>
                <h1>Ping Result for {{ ip_address }}</h1>
                <pre>{{ output }}</pre>
              </body>
            </html>
        ''', ip_address=ip_address, output=result.stdout)
    return render_template_string('''
        <html>
          <head>
            <title>Ping App</title>
          </head>
          <body>
            <h1>Ping App</h1>
            <form method="POST">
              <label for="ip_address">IP Address:</label>
              <input type="text" id="ip_address" name="ip_address">
              <button type="submit">Ping</button>
            </form>
          </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
````
</details>




<details open>
  <summary><h4 style="display: inline-block; font-size: 18px; font-weight: bold;">
      Using Werkzeug
  </h4></summary>
  
````python
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response('Hello, World!', content_type='text/plain')

if __name__ == '__main__':
    run_simple('localhost', 8000, application, ssl_context=('server.pem', 'server.key'))
````
</details>
