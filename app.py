from flask import Flask, render_template
import sqlite3


helloworld = Flask(__name__)
@helloworld.route('/')
def run():
  return "{\"message\":\"Python\"}"

@helloworld.route('/home')
def home():
  # get existing messages 
  existing_messages = []
  # create a message from input
  create_message = ""
  # store message into sqlite

  conn = sqlite3.connect('messages.db')
  c = conn.cursor()

  c.execute('''CREATE TABLE IF NOT EXISTS messages 
              (message text)''')

  c.execute("INSERT INTO messages VALUES (?)", (create_message,))
  conn.commit()
  conn.close()

  return render_template('base.html', data=existing_messages)

if __name__ == "__main__":
  helloworld.run(host="0.0.0.0", port=int("5000"), debug=True)