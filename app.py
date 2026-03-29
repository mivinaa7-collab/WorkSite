from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

@app.route("/link/<int:link_id>")
def link_page(link_id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "SELECT project, price FROM links WHERE id = %s",
        (link_id,)
    )

    data = cur.fetchone()
    conn.close()

    if not data:
        return "Ошибка"

    project, price = data

    return render_template(
        "privat.html",
        price=price,
        link_id=link_id
    )
import os 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
