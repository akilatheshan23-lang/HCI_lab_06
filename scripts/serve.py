"""Local browser preview: python scripts/serve.py (http://127.0.0.1:4173)."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from functools import partial
server=ThreadingHTTPServer(('127.0.0.1',4173),partial(SimpleHTTPRequestHandler,directory=str(Path(__file__).resolve().parents[1]/'web')))
print('FitFlow preview: http://127.0.0.1:4173',flush=True)
server.serve_forever()
