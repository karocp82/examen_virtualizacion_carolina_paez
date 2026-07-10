from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.route("/")
def home():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS visitas (
            id SERIAL PRIMARY KEY,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    cur.execute("INSERT INTO visitas DEFAULT VALUES;")

    cur.execute("SELECT COUNT(*) FROM visitas;")
    contador = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return f"<h1>Visitas registradas: {contador}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
