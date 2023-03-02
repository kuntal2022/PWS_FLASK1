from flask import Flask, render_template, request, redirect, url_for,jsonify

app=Flask(__name__)

@app.route('/')

def welcome():
    return render_template('final.html')

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



@app.route("/submit", methods=["GET", "POST"])
def submit():
    total=0
    t=""
    if request.method=="POST":
        math=float(request.json['math'])
        bio=float(request.json['bio'])
        geo=float(request.json['geo'])
        c=float(request.json['c'])
        others=float(request.json["others"])
        total=math+bio+geo+c+others
        tavg=total/5
        res="yes"
    if tavg>=50:
        t=f"You have Passed with {tavg} as Average"
    else:
        t=f"You have Failed with {tavg} as Average"
    return jsonify(t)
   
        






if __name__=="__main__":
    app.run(debug=True)
