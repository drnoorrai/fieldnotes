import os
import secrets
from flask import Flask, jsonify, request, send_from_directory
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")
NOTES_PASSWORD = os.environ.get("NOTES_PASSWORD", "")


def get_db():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn


def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id SERIAL PRIMARY KEY,
            article_id TEXT NOT NULL,
            text TEXT NOT NULL,
            highlight BOOLEAN NOT NULL DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT NOW()
        );
        CREATE INDEX IF NOT EXISTS notes_article_id_idx ON notes(article_id);
    """)
    conn.commit()
    cur.close()
    conn.close()


def check_auth():
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        return False
    provided = auth[len("Bearer "):]
    return NOTES_PASSWORD and secrets.compare_digest(provided, NOTES_PASSWORD)


@app.route("/api/auth", methods=["POST"])
def verify_auth():
    data = request.get_json()
    if not data or not data.get("password"):
        return jsonify({"error": "password required"}), 400
    if NOTES_PASSWORD and secrets.compare_digest(data["password"], NOTES_PASSWORD):
        return jsonify({"ok": True})
    return jsonify({"ok": False}), 401


@app.route("/api/notes/<article_id>", methods=["GET"])
def get_notes(article_id):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, text, highlight, created_at FROM notes WHERE article_id = %s ORDER BY created_at DESC",
            (article_id,)
        )
        rows = cur.fetchall()
        cur.close()
        conn.close()
        notes = []
        for r in rows:
            notes.append({
                "id": r["id"],
                "text": r["text"],
                "highlight": r["highlight"],
                "time": r["created_at"].isoformat()
            })
        return jsonify(notes)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/notes/<article_id>", methods=["POST"])
def add_note(article_id):
    if not check_auth():
        return jsonify({"error": "unauthorized"}), 401
    try:
        data = request.get_json()
        if not data or not data.get("text"):
            return jsonify({"error": "text is required"}), 400
        text = data["text"]
        highlight = bool(data.get("highlight", False))
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO notes (article_id, text, highlight) VALUES (%s, %s, %s) RETURNING id, text, highlight, created_at",
            (article_id, text, highlight)
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({
            "id": row["id"],
            "text": row["text"],
            "highlight": row["highlight"],
            "time": row["created_at"].isoformat()
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/notes/<article_id>/<int:note_id>", methods=["DELETE"])
def delete_note(article_id, note_id):
    if not check_auth():
        return jsonify({"error": "unauthorized"}), 401
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM notes WHERE id = %s AND article_id = %s",
            (note_id, article_id)
        )
        conn.commit()
        cur.close()
        conn.close()
        return "", 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/notes/counts", methods=["GET"])
def note_counts():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT article_id, COUNT(*) as count FROM notes GROUP BY article_id")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify({r["article_id"]: r["count"] for r in rows})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/posts/<path:filename>")
def serve_posts(filename):
    return send_from_directory("posts", filename)


@app.route("/")
def serve_index():
    return send_from_directory(".", "index.html")


@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory(".", "index.html")


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)
