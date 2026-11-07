import http.server, socketserver, os, sys, urllib.parse

PORT = 4040
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class RewriteHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Force charset UTF-8 on text, html and js files
        ctype = self.headers.get('Content-Type', '')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def guess_type(self, path):
        ctype = super().guess_type(path)
        if ctype.startswith('text/') or ctype in ['application/javascript', 'application/json']:
            return ctype + '; charset=utf-8'
        return ctype
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def translate_path(self, path):
        # Base path resolution from SimpleHTTPRequestHandler
        path = path.split('?', 1)[0]
        path = path.split('#', 1)[0]
        trailing_slash = path.rstrip().endswith('/')
        try:
            path = urllib.parse.unquote(path, errors='surrogatepass')
        except UnicodeDecodeError:
            path = urllib.parse.unquote(path)
        
        words = [w for w in path.split('/') if w and w != '.']
        full_path = DIRECTORY
        for word in words:
            if word == '..':
                continue
            full_path = os.path.join(full_path, word)
        
        # If it doesn't exist directly, check if adding .html exists
        if not os.path.exists(full_path):
            if os.path.isfile(full_path + '.html'):
                return full_path + '.html'
        
        if trailing_slash:
            full_path += '/'
        return full_path

def run():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), RewriteHandler) as httpd:
        print(f"STAGING_SERVER_ACTIVE_AT: http://localhost:{PORT}")
        sys.stdout.flush()
        httpd.serve_forever()

if __name__ == '__main__':
    run()
