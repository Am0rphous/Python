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
- Others...
- [Updog](https://github.com/sc0tfree/updog) - Updog is a replacement for Python's SimpleHTTPServer. It allows uploading and downloading via HTTP/S, can set ad hoc SSL certificates and use http basic auth.

#### Using Flask
````python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(ssl_context=('server.pem', 'server.key'))
````

<details>
  <summary><h4 style="display: inline-block; font-size: 18px; font-weight: bold;">Use a specific/vulnerable Flask version</h4></summary>
    
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


#### Using Werkzeug
````python
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response('Hello, World!', content_type='text/plain')

if __name__ == '__main__':
    run_simple('localhost', 8000, application, ssl_context=('server.pem', 'server.key'))
````
