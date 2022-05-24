from pickle import TRUE
from flask import Flask, render_template
import frontmatter
import os
from markdown import markdown
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    posts_list = []
    for item in os.listdir('static/posts'):
        with open("./static/posts/"+item, encoding='utf-8') as f:
            data = frontmatter.load(f)
            post = {
                "title": data["title"],
                "url": data["slug"],
                "date": data["date"],
                "postno": data["postno"],
                "tags":data["tags"]
            }
            posts_list.append(post)
            posts_list = sorted(
                posts_list, key=lambda k: k["postno"], reverse=True)
    return render_template('index.html', data=posts_list)


@app.route("/post/<slug>", methods=["GET"])
def post(slug):
    data = ""
    with open('static/posts/'+str(slug)+".md", encoding='utf-8') as f:
        fm_data = frontmatter.load(f)
        data = markdown(fm_data.content)

    return render_template('post.html', post=data)


@app.route("/about", methods=["GET"])
def about():
    about = ""
    with open('static/about/about.md', encoding='utf-8') as f:
        fm_data = frontmatter.load(f)
        about = markdown(fm_data.content)
    return render_template('about.html', about=about)


@app.route("/tag/<tag>", methods=["GET"])
def tag_posts():
    pass


if __name__ == "__main__":
    app.run(debug=True)
