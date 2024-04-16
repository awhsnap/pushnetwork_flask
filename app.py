from flask import Flask
helloworld = Flask(__name__)
@helloworld.route('/')
def run():
  return "{\"message\":\"Python\"}"

if __name__ == "__main__":
  helloworld.run(host="0.0.0.0", port=int("4321"), debug=True)