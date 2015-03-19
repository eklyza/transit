from flask import Flask
app = Flask(__name__)

@app.route("/<username>")
def hello(username):
	return "Good morning, "+username+"!"

if __name__ == "__main__":
	app.run()