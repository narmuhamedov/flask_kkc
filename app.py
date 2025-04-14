from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
#Подключение SQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="db"
)

cursor = db.cursor(dictionary=True)


@app.route("/")
def blog_list():
    cursor.execute("SElECT id, title FROM blog")
    blog = cursor.fetchall()
    return render_template("list.html", blog=blog)

@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    cursor.execute("SELECT * FROM blog WHERE id = %s", (blog_id,))
    blog = cursor.fetchone()
    if blog:
        return render_template('detail.html', blog=blog)

    return 'Блог не найден', 404

if __name__ == "__main__":
    app.run(debug=True)