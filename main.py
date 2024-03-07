from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Integer, String
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = "xb938r4tr8o1bxpncy49p81c"
bootstrap = Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_info.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task: Mapped[str] = mapped_column(String, unique=True, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        text_data = request.form.get("input1")
        new_task = User(
            task=text_data
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("home"))
    all_data = db.session.execute(db.select(User)).scalars().all()
    return render_template("index.html", all_data=all_data)


@app.route("/remove", methods=['POST'])
def remove():
    if request.method == "POST":
        task_id = request.form.get("task_id")
        task_to_delete = User.query.get(task_id)
        if task_to_delete:
            db.session.delete(task_to_delete)
            db.session.commit()
    return redirect(url_for('home'))


@app.route("/edit/<int:task_id>", methods=["POST"])
def edit(task_id):
    if request.method == "POST":
        new_task_text = request.form.get("new_task_text")
        task_to_edit = User.query.get(task_id)
        if task_to_edit:
            task_to_edit.task = new_task_text
            db.session.commit()
            return redirect(url_for('home'))
        else:
            return "Task not found", 404


if __name__ == "__main__":
    app.run(debug=True)
