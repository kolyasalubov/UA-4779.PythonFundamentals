from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort


# def get_db_connection():
#     connection = sqlite3.connect('database.db')
#     connection.row_factory = sqlite3.Row
#     return connection

# def get_post(post_id):
#     connection = get_db_connection()
#     post = connection.execute('SELECT * FROM posts WHERE id = ?',
#                               (post_id,)).fetchone()
#     connection.close()
#     if post is None:
#         abort(404)
#     return post



app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/<int>:post_id')
def post(post_id):
    post = Post.query.get(post_id)
    return render_template('post.html', post=post)

@app.get('/create')
def create():
    return render_template('create.html', post=post)

@app.post('/create')
def submit_create():
    title = request.form['title']
    content = request.form['content']

    if not title:
        flash("Title is required")
    else:
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html', post=post)

@app.get('/<int:id>/edit')
def edit(id):
    post = Post.query.get(id)
    return render_template('edit.html', post=post)

@app.post('/<int:id>/edit')
def submit_edit(id):
    post = Post.query.get(id)
    title = request.form['title']
    content = request.form['content']

    if not title:
        flash('Title is required')
    else:
        post.title = title
        post.content = content
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html', post=post)

@app.post('/<int:id>/delete')
def delete(id):
    post = Post.query.get(id)
    if post:
        db.session.delete(post)
        db.session.commit()
        flash('"{}" was successfully deleted!'.format(post.title))
        return redirect(url_for('index'))
    else:
        abort(404)





if __name__ == '__main__':
    app.run(debug=True)

