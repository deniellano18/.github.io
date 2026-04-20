import http.server
import socketserver
import json
import os
from datetime import datetime

PORT = 8000
DATA_FILE = 'data/requests.json'

class DemoRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve the /api/requests endpoint
        if self.path == '/api/requests':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'r') as f:
                    data = f.read()
            else:
                data = '[]'
                
            self.wfile.write(data.encode('utf-8'))
            return
        
        # Otherwise, serve static files as usual
        return super().do_GET()

    def do_POST(self):
        if self.path == '/api/request-demo':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                request_data = json.loads(post_data.decode('utf-8'))
                
                # Add timestamp
                request_data['timestamp'] = datetime.now().isoformat()
                
                # Create data directory if it doesn't exist
                os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
                
                # Load existing data
                existing_data = []
                if os.path.exists(DATA_FILE):
                    with open(DATA_FILE, 'r') as f:
                        try:
                            existing_data = json.load(f)
                        except json.JSONDecodeError:
                            existing_data = []
                
                # Append new data
                existing_data.append(request_data)
                
                # Save back to file
                with open(DATA_FILE, 'w') as f:
                    json.dump(existing_data, f, indent=4)
                
                # Send success response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "message": "Demo request saved"}).encode('utf-8'))
                
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
            
            return
        
        self.send_response(404)
        self.end_headers()

with socketserver.TCPServer(("", PORT), DemoRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Access landing page at http://localhost:{PORT}")
    print(f"Access admin page at http://localhost:{PORT}/admin.html")
    httpd.serve_forever()
import http.server
import socketserver
import json
import os
from datetime import datetime

PORT = 8000
DATA_FILE = 'data/requests.json'

class DemoRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve the /api/requests endpoint
        if self.path == '/api/requests':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, 'r') as f:
                    data = f.read()
            else:
                data = '[]'
                
            self.wfile.write(data.encode('utf-8'))
            return
        
        # Otherwise, serve static files as usual
        return super().do_GET()

    def do_POST(self):
        if self.path == '/api/request-demo':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                request_data = json.loads(post_data.decode('utf-8'))
                
                # Add timestamp
                request_data['timestamp'] = datetime.now().isoformat()
                
                # Create data directory if it doesn't exist
                os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
                
                # Load existing data
                existing_data = []
                if os.path.exists(DATA_FILE):
                    with open(DATA_FILE, 'r') as f:
                        try:
                            existing_data = json.load(f)
                        except json.JSONDecodeError:
                            existing_data = []
                
                # Append new data
                existing_data.append(request_data)
                
                # Save back to file
                with open(DATA_FILE, 'w') as f:
                    json.dump(existing_data, f, indent=4)
                
                # Send success response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "message": "Demo request saved"}).encode('utf-8'))
                
            except Exception as e:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
            
            return
        
        self.send_response(404)
        self.end_headers()

with socketserver.TCPServer(("", PORT), DemoRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Access landing page at http://localhost:{PORT}")
    print(f"Access admin page at http://localhost:{PORT}/admin.html")
    httpd.serve_forever()
