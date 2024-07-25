import os
import webbrowser
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def get_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line == "eof":
            break
        lines.append(line)
    return "\n".join(lines)

html_content = get_input("Enter your HTML content (eof to end):")
css_content = get_input("Enter your CSS content (eof to end):")
file_html = "index.html"
file_css = "style.css"
with open(file_html, "w") as html_file:
    html_file.write(html_content)

with open(file_css, "w") as css_file:
    css_file.write(css_content)

print(f"Files {file_html} {file_css} created successfully!! ")

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

port = 8000
with TCPServer(("", port), MyHandler) as httpd:
    print(f"Serving on http://localhost:{port}")
    webbrowser.open(f"http://localhost:{port}")
    httpd.serve_forever()
