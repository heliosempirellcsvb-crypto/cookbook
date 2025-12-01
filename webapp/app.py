from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

SCAN_DIRS = [
    "../cookbook",
    "../vscode-remote-release"
]
FILE_EXTS = (".py", ".ipynb")
WALLET_EMAIL = "heliosempirellcsvb@gmail.com"
WALLET_LINK = f"https://pay.google.com/send?email={{WALLET_EMAIL}}"

def list_scripts():
    scripts = []
    for dirname in SCAN_DIRS:
        for root, dirs, files in os.walk(dirname):
            for fname in files:
                if fname.endswith(FILE_EXTS):
                    rel_path = os.path.relpath(os.path.join(root, fname), ".")
                    scripts.append(rel_path)
    return scripts

@app.route("/")
def index():
    scripts = list_scripts()
    return render_template(
        "index.html",
        scripts=scripts,
        wallet_email=WALLET_EMAIL,
        wallet_link=WALLET_LINK
    )

@app.route("/download/<path:filepath>")
def download(filepath):
    directory = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
