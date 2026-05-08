import http.server
import socketserver
import webbrowser
from pathlib import Path

PORT = 8000
DIRECTORY = Path(__file__).resolve().parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

if __name__ == "__main__":
    url = f"http://localhost:{PORT}/test.html"
    print(f"Serving '{DIRECTORY / 'test.html'}' at {url}")
    webbrowser.open(url)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            httpd.server_close()
