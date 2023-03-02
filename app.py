from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/')

def welcome():
    return render_template('final.html')

@app.route("/submit", methods=["GET", "POST"])
def submit():
    total=0
    if request.method=="POST":
        math=float(request.form['math'])
        bio=float(request.form['bio'])
        geo=float(request.form['geo'])
        c=float(request.form['c'])
        others=float(request.form["others"])
        total=math+bio+geo+c+others
        tavg=total/5
        res="yes"
    if tavg<0 or tavg>100:
        return "<H1>SCORE CAN'T BE >100 <H1>"
    else:
        return redirect(url_for(res, score=tavg))

@app.route('/yes/<float:score>')

def yes(score):
    x={}
    if score>=50:
        x['Pass']='Yes'
        x['Score']=score
    else:
        x["Pass"]='No'
        x['Score']=score
    res1=x
    return render_template('index.html', result=res1)






if __name__=="__main__":
    app.run(debug=True)
