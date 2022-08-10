from flask import Flask, render_template

from utils import get_by_uid, get_all, get_by_name, get_by_skill

app = Flask(__name__)


@app.route("/")
def page_main():
    candidates = get_all()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:uid>")
def candidate_page(uid):
    candidate = get_by_uid(uid)
    print(candidate)
    return render_template("card.html", candidate=candidate)


@app.route("/search/<name>")
def name_page(name):
    candidates = get_by_name(name)
    return render_template("search.html", candidates=candidates, name=name)


@app.route("/skill/<skill_name>")
def skill_page(skill_name):
    candidates = get_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, skill=skill_name)


if __name__ == "__main__":
    app.run()
