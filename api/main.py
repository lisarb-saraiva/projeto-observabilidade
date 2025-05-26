from flask import Flask, jsonify, request
from prometheus_client import Counter, Histogram, generate_latest, CollectorRegistry
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)

# Prometheus metrics
registry = CollectorRegistry()
REQUEST_COUNT = Counter('request_count', 'Total de requisições por rota', ['method', 'endpoint'], registry=registry)
RESPONSE_TIME = Histogram('response_time', 'Tempo de resposta por rota', ['endpoint'], registry=registry)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/books', methods=['GET'])
def get_books():
    books = [{"title": "1984", "author": "George Orwell"}, {"title": "Brave New World", "author": "Aldous Huxley"}]
    REQUEST_COUNT.labels('GET', '/books').inc()
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    book = request.json
    REQUEST_COUNT.labels('POST', '/books').inc()
    return jsonify(book), 201

@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest(registry)

# Middleware for Prometheus metrics
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app(registry)
})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)