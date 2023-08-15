
from flask import Flask, render_template
import sqlite3

douban_flask = Flask(__name__,template_folder="../templates",static_folder='../static')

@douban_flask.route("/")
def index():
    return render_template("index.html")

@douban_flask.route("/index.html")
def indexhome():
    return index()


@douban_flask.route("/movil.html")
def about():
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()

    return render_template("movil.html",movies = datalist) 

@douban_flask.route("/score.html")
def score():
 
    score = [] # 电影评分
    num = []   # 每个评分统计数据
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html",score=score,num=num)

@douban_flask.route("/word.html")
def word():
    return render_template("word.html")

@douban_flask.route("/team.html")
def team():
    return render_template("team.html")





if __name__ == "__main__":
    douban_flask.run(debug=True)
