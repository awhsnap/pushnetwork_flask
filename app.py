from flask import Flask, render_template
helloworld = Flask(__name__)
@helloworld.route('/')
def run():
  return "{\"message\":\"Python\"}"

@helloworld.route('/home')
def home():
  return render_template('base.html')

if __name__ == "__main__":
  helloworld.run(debug=True)