from flask import Flask, render_template
import psycopg2

app = Flask(__name__)  # Flask constructor


def connect_to_db():
    return psycopg2.connect(
        user="postgres",
        password="123456789",
        host="localhost",
        port=5432,
        database="postgres"
    )


@app.route('/')  # decorator
def hello():
    conn = connect_to_db()  # Connect to the database
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM employee''')
    rows = cursor.fetchall()

    cursor.close()  # Close the cursor
    conn.close()  # Close the connection

    return render_template("home.html", employees=rows)  # Pass data to the template


if __name__ == '__main__':
    app.run(debug=True)
