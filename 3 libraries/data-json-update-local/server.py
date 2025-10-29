from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

FILE_PATH = "data.json"

class SimpleJSONHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("content-type","application/json")
        self.end_headers()

    def do_GET(self):
        """"Show all data"""
        self._set_headers()
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH,"w") as f:
                json.dump([], f)
        with open(FILE_PATH,"r") as f:
            data = json.load(f)
        self.wfile.write(json.dumps(data, indent=4).encode())

    def do_PUT(self):
        """end new line with auto increment id"""
        content_length = int(self.headers["Content-Length"])
        new_data = json.loads(self.rfile.read(content_length))

        #load existing data
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as f:
                data = json.load(f)
        else:
            data = []

        #auto increment id
        if data:
            new_id = max(item["id"] for item in data) + 1
        else:
            new_id = 1

        new_data["id"] = new_id
        data.append(new_data)

        with open(FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)

        self._set_headers()
        self.wfile.write(json.dumps({"message": "data added successfully", "new_item": new_data}, indent=4).encode())

def run(server_class=HTTPServer, handler_class=SimpleJSONHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"server running at http://127.0.0.1:{port}/data")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

