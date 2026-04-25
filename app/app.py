from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = "aceest.db"


def get_db():
    return sqlite3.connect(DB_NAME)


@app.route("/")
def home():
    return {"message": "ACEest DevOps API Running 🚀"}


@app.route("/clients", methods=["POST"])
def add_client():
    data = request.json
    name = data.get("name")

    conn = get_db()
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY, name TEXT UNIQUE)")
    
    try:
        cur.execute("INSERT INTO clients (name) VALUES (?)", (name,))
        conn.commit()
        return {"message": "Client added"}, 201
    except:
        return {"error": "Client exists"}, 400


@app.route("/clients", methods=["GET"])
def get_clients():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM clients")
    return jsonify(cur.fetchall())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)