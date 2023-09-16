import http.server
import socketserver
import os

# Set the port you want the server to run on
PORT = int(os.environ.get("PORT", 8080))
print(PORT,type(PORT),flush=True)

# Define the handler for the web server
handler = http.server.SimpleHTTPRequestHandler

# Create a socket server to listen on the specified port
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at port {PORT}",flush=True)
    # Start the server
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")