"""
Basic imports (Flask, flask-markdown, os to read files...)
"""
from flask import Flask, Response, request, render_template
import markdown2

import pygments
from os import listdir, path
from os.path import isfile, join
from time import strftime, ctime
import datetime

import re
import json
import logging, sys

"""
App logging and set up
"""
logging.basicConfig(stream=sys.stderr)
app = Flask(__name__)
markdowner = markdown2.Markdown(extras=["fenced-code-blocks","code-friendly"])
meta_file = json.loads(open("./posts/meta.json", 'r').read())

"""
Index route, lists the posts
"""
@app.route("/")
def index():

  posts = []
  
  meta_file = json.loads(open("./posts/meta.json", 'r').read())
  
  for post in meta_file:
    posts.append({
      "title":meta_file[post]['title'],
      "filename":meta_file[post]['file'],
      "unique":post,
      "last_date":datetime.datetime.strptime(meta_file[post]['date'], "%d/%m/%Y").strftime("%B %d, %Y")
    })
  posts.sort(key=lambda k: datetime.datetime.strptime(k['last_date'], '%B %d, %Y'), reverse=True)
  return render_template('index.html', **locals())

@app.route("/favicon.ico")
def favicon():
  return ""

"""
Shows a post
"""
@app.route("/<post>")
def show(post):
  in_post = True
  try:
    title = meta_file[post]['title']
    post = {
      "title":meta_file[post]['title'],
      "filename":meta_file[post]['file'],    
      "last_date":datetime.datetime.strptime(meta_file[post]['date'], "%d/%m/%Y").strftime("%B %d, %Y"),
      "content":markdowner.convert(open("./posts/%s" % meta_file[post]['file'], 'r').read())
    }
    return render_template('show.html', **locals())
  except KeyError:
    return render_template('error.html', **locals())

"""
Humanizes a file name
"""
def humanize(text):
  return re.sub("_", " ", re.sub(".md", "", text)).capitalize()


if __name__ == "__main__":
  print("Ready!")
  app.run(debug=True)