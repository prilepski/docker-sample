from flask import Flask
import os
import socket
import sys

app = Flask(__name__)

@app.route("/")
def hello():
        f = open("/mnt/" + "test.txt", "w")
        f.write("test text")
        f.close()

        f = open("/mnt/" +  sys.argv[1], "r")
        service = f.read()
        f.close()
        html = "<h3>Hello {name}!</h3>" \
            "<b>Hostname:</b> {hostname}<br/>" \
            "<b> Servicename:</b> {service}<br>"
        return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), service=service)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=sys.argv[2])
