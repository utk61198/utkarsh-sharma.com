from deta import Deta
from flask import Flask, render_template
import frontmatter
import os
from markdown import markdown
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

deta = Deta('c0blgm2m_TJ27PXwshU7hSTZp3sNP6jVsrw1WKd6R')
blog_visited_tracker = deta.Base('blog_visited_tracker')


def blog_visit_counter_update():
    count = blog_visited_tracker.get('main_key')['count']
    blog_visited_tracker.put({"count": count+1}, "main_key")
    return count


@app.route("/", methods=["GET"])
def index():
    count = blog_visit_counter_update()
    posts_list = []
    for item in os.listdir('static/posts'):
        with open("./static/posts/"+item, encoding='utf-8') as f:
            data = frontmatter.load(f)
            post = {
                "title": data["title"],
                "url": data["slug"],
                "date": data["date"],
                "postno": data["postno"],
                "tags": data["tags"]
            }
            posts_list.append(post)
            posts_list = sorted(
                posts_list, key=lambda k: k["postno"], reverse=True)
    return render_template('index.html', data=posts_list, count=count)


@app.route("/post/<slug>", methods=["GET"])
def post(slug):
    count = blog_visit_counter_update()
    try:
        f = open('static/posts/'+str(slug)+".md", encoding='utf-8')
        with f:
            fm_data = frontmatter.load(f)
            data = markdown(fm_data.content)
            return render_template('post.html', post=data)
    except:
        return "no such post exists :("


@app.route("/about", methods=["GET"])
def about():
    count = blog_visit_counter_update()
    about = ""
    with open('static/about/about.md', encoding='utf-8') as f:

        fm_data = frontmatter.load(f)
        about = markdown(fm_data.content)
    return render_template('about.html', about=about)


@app.route("/tag/<tag>", methods=["GET"])
def tag_posts(tag):
    count = blog_visit_counter_update()
    post_list = []
    for item in os.listdir('static/posts'):
        with open('./static/posts/'+item, encoding='utf-8') as f:
            data = frontmatter.load(f)
            if tag in data["tags"]:
                post = {
                    "title": data["title"],
                    "url": data["slug"],
                    "date": data["date"],
                    "postno": data["postno"],
                    "tags": data["tags"]
                }
                post_list.append(post)
    if len(post_list):
        return render_template('index.html', data=post_list)
    else:
        return "No such tag exists yet :("


@app.route("/visited", methods=['GET'])
def visited():
    count = blog_visited_tracker.get("main_key")["count"]
    return f"Total blog visits: {count}"
