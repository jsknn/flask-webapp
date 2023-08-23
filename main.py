
'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''
from flask import Flask,redirect,url_for,render_template,request
from testrail import *

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

status=[]
Title=[]
dic ={}
@app.route('/result',methods=['POST','GET'])
def title_status():
    client = APIClient(request.form['enterurl'])#url
    client.user = request.form['username']#config.username
    client.password = request.form['password']#config.password
    run_id = request.form['runid']
    Tests =  client.send_get('get_tests/'+run_id+'&status_id=7,6,5,4,2')
    for i in Tests:
        Titles = i.get('title')
        Title.append(Titles)
        Status = i.get('status_id')
        if Status ==5:
            Status = "FAILED"
            status.append(Status)
        elif Status==2:
            Status = "BLOCKED"
            status.append(Status)
        elif Status==6:
            Status = "PASSED CAUTION" 
            status.append(Status)
        elif Status==7:
            Status = "SKIPPED"  
            status.append(Status)
        elif Status==3:
            Status = "UNTESTED"
            status.append(Status)
        elif Status==4:
            Status= "RETEST"
            status.append(Status)
        else:
            status.append(Status)
        

    d=zip(Title,status)
    dd = dict(d)
    return render_template('result.html',result=dd)
    


if __name__=='__main__':
    app.run(debug=True)