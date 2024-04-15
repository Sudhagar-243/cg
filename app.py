from flask import Flask, render_template, request,redirect,session
import numpy as np
import pickle
import mysql.connector
app = Flask(__name__)
app.secret_key = '2403'
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/')
def login():
    return render_template('signIn.html')
@app.route('/features')
def features():
    return render_template("features.html")
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/skills')
def skills():
    return render_template("skill.html")
@app.route('/eee')
def test_eee():
    return render_template("eee.html")
@app.route('/cse')
def test_cse():
    return render_template("cse.html")
@app.route('/ece')
def test_ece():
    return render_template("ece.html")
@app.route('/mech')
def test_mech():
    return render_template("mech.html")
@app.route('/civil')
def test_civil():
    return render_template("civil.html")
@app.route('/signUp')
def signup():
    return render_template("signup.html")
@app.route('/signin')
def signin():
    return render_template("signIn.html")

@app.route('/submit', methods=['POST'])
def submit():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="eee",
    auth_plugin='mysql_native_password'
    )
    mycursor=mydb.cursor()
    
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    sql_query = "INSERT INTO UserDetails (email, username, password) VALUES (%s, %s, %s)"
    try:
        mycursor.execute(sql_query, (email, username, password))
    except mysql.connector.IntegrityError as e:
        return redirect("/failure")
    mydb.commit()
    mycursor.close()
    mydb.close()
    session['username'] = username
    return redirect("/index")
@app.route('/validate',methods=['POST'])
def validate():
    if request.method == 'POST':
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="eee",
        auth_plugin='mysql_native_password'
        )
        mycursor=mydb.cursor()
        username = request.form['username']
        password = request.form['password']
        # Check if the username and password exist in the database
        mycursor.execute("SELECT * FROM UserDetails WHERE username=%s", (username,))
        user = mycursor.fetchone()

        if user:
            if user[2] == password:
                session['username'] = username
                return redirect('/index')
            else:
                return user
        else:
            return redirect('/loginfailure')
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/signin')
@app.route('/test')
def test():
    session.pop('username', None)
    return render_template("domain.html")
@app.route('/result_eee',methods = ['POST', 'GET'])
def result_eee():
    # if 'username' not in session:
    #     return redirect('/signin')
    if request.method == 'POST':
        result = request.form
        i = 0
        print(result)
        res = result.to_dict(flat=True)
        print("res:",res)
        arr1 = res.values()
        arr = ([value for value in arr1])
        vector = np.vectorize(np.int_)
        data = np.array(arr)
        
        data = data.reshape(1,-1)
        print(data)
        loaded_model = pickle.load(open("eee.pkl", 'rb'))
        predictions = loaded_model.predict(vector(data))
        # return render_template('testafter.html',a=predictions)
        
        print(predictions)
        pred = loaded_model.predict_proba(vector(data))
        print(pred)
        #acc=accuracy_score(pred,)
        pred = pred > 0.05
        #print(predictions)
        i = 0
        j = 0
        index = 0
        res = {}
        final_res = {}
        while j < 17:
            if pred[i, j]:
                res[index] = j
                index += 1
            j += 1
        # print(j)
        #print(res)
        index = 0
        for key, values in res.items():
            if values != predictions[0]:
                final_res[index] = values
                print('final_res[index]:',final_res[index])
                index += 1
        #print(final_res)
        jobs_dict = {0:'Control System Engineer With AI/ML Expertise',
                    1:'Integration Engineer',
                    2:'Field Service Engineer',
                    3:'Business Analyst',
                    4:'Technical Support Engineer',
                    5:'System Security Engineer',
                    6:'Singnal Processing Scientist',
                    7:'Control System Engineer',
                    8:'PCB Designer',
                    9:'Embedded Systems Engineer',
                    10:'Field Service Technician',
                    11:'Power System Engineer',
                    12:'Telecommmunication Engineer',
                    13:'Project Manager',
                    14:'Firmware Engineer',
                    15:'Quality Assurance Engineer',
                    16:'Technical Documentation Specialist'}
                    
        #print(jobs_dict[predictions[0]])
        job = {}
        #job[0] = jobs_dict[predictions[0]]
        index = 1
        
            
        data1=predictions[0]
        print(data1)
        return render_template("testafter.html",final_res=final_res,job_dict=jobs_dict,job0=data1)
@app.route('/result_cse',methods = ['POST', 'GET'])
def result_cse():
    # if 'username' not in session:
    #     return redirect('/signin')
    
    if request.method == 'POST':
        result = request.form
        i = 0
        print(result)
        res = result.to_dict(flat=True)
        print("res:",res)
        arr1 = res.values()
        arr = ([value for value in arr1])
        vector = np.vectorize(np.int_)
        data = np.array(arr)
        
        data = data.reshape(1,-1)
        print(data)
        loaded_model = pickle.load(open("cse.pkl", 'rb'))
        predictions = loaded_model.predict(vector(data))
        # return render_template('testafter.html',a=predictions)
        
        print(predictions)
        pred = loaded_model.predict_proba(vector(data))
        print(pred)
        #acc=accuracy_score(pred,)
        pred = pred > 0.05
        #print(predictions)
        i = 0
        j = 0
        index = 0
        res = {}
        final_res = {}
        while j < 17:
            if pred[i, j]:
                res[index] = j
                index += 1
            j += 1
        # print(j)
        #print(res)
        index = 0
        for key, values in res.items():
            if values != predictions[0]:
                final_res[index] = values
                print('final_res[index]:',final_res[index])
                index += 1
        #print(final_res)
        jobs_dict = {0:'AI ML Specialist',
                    1:'API Integration Specialist',
                    2:'Application Support Engineer',
                    3:'Business Analyst',
                    4:'Customer Service Executive',
                    5:'Cyber Security Specialist',
                    6:'Data Scientist',
                    7:'Database Administrator',
                    8:'Graphics Designer',
                    9:'Hardware Engineer',
                    10:'Helpdesk Engineer',
                    11:'Information Security Specialist',
                    12:'Networking Engineer',
                    13:'Project Manager',
                    14:'Software Developer',
                    15:'Software Tester',
                    16:'Technical Writer'}
                    
        #print(jobs_dict[predictions[0]])
        job = {}
        #job[0] = jobs_dict[predictions[0]]
        index = 1
        
            
        data1=predictions[0]
        print(data1)
        return render_template("testafter.html",final_res=final_res,job_dict=jobs_dict,job0=data1)
@app.route('/result_mech',methods = ['POST', 'GET'])
def result_mech():
    # if 'username' not in session:
    #     return redirect('/signin')
    
    if request.method == 'POST':
        result = request.form
        i = 0
        print(result)
        res = result.to_dict(flat=True)
        print("res:",res)
        arr1 = res.values()
        arr = ([value for value in arr1])
        vector = np.vectorize(np.int_)
        data = np.array(arr)
        
        data = data.reshape(1,-1)
        print(data)
        loaded_model = pickle.load(open("careerlast.pkl", 'rb'))
        predictions = loaded_model.predict(vector(data))
        # return render_template('testafter.html',a=predictions)
        
        print(predictions)
        pred = loaded_model.predict_proba(vector(data))
        print(pred)
        #acc=accuracy_score(pred,)
        pred = pred > 0.05
        #print(predictions)
        i = 0
        j = 0
        index = 0
        res = {}
        final_res = {}
        while j < 17:
            if pred[i, j]:
                res[index] = j
                index += 1
            j += 1
        # print(j)
        #print(res)
        index = 0
        for key, values in res.items():
            if values != predictions[0]:
                final_res[index] = values
                print('final_res[index]:',final_res[index])
                index += 1
        #print(final_res)
        jobs_dict = {0:'Predictive Maintenance Analyst',
                    1:'Interoperability Engineer',
                    2:'Thermal Engineer',
                    3:'Business Analyst',
                    4:'Customer Service Executive',
                    5:'Automobile Engineer',
                    6:'Mechanical System Analyst',
                    7:'Manfactyuring Engineer',
                    8:'Aerospace Engineer',
                    9:'Hardware Engineer',
                    10:'Technical Support Engineer',
                    11:'Product Security Engineer',
                    12:'System Integration Engineer',
                    13:'Project Manager',
                    14:'Mechanical Systems Software Engineer',
                    15:'Quality Assurance Engineer',
                    16:'Technical Documentation Analyst'}
                    
        #print(jobs_dict[predictions[0]])
        job = {}
        #job[0] = jobs_dict[predictions[0]]
        index = 1
        
            
        data1=predictions[0]
        print(data1)
        return render_template("testafter.html",final_res=final_res,job_dict=jobs_dict,job0=data1)
@app.route('/result_ece',methods = ['POST', 'GET'])
def result_ece():
    # if 'username' not in session:
    #     return redirect('/signin')
    
    if request.method == 'POST':
        result = request.form
        i = 0
        print(result)
        res = result.to_dict(flat=True)
        print("res:",res)
        arr1 = res.values()
        arr = ([value for value in arr1])
        vector = np.vectorize(np.int_)
        data = np.array(arr)
        
        data = data.reshape(1,-1)
        print(data)
        loaded_model = pickle.load(open("ece.pkl", 'rb'))
        predictions = loaded_model.predict(vector(data))
        # return render_template('testafter.html',a=predictions)
        
        print(predictions)
        pred = loaded_model.predict_proba(vector(data))
        print(pred)
        #acc=accuracy_score(pred,)
        pred = pred > 0.05
        #print(predictions)
        i = 0
        j = 0
        index = 0
        res = {}
        final_res = {}
        while j < 17:
            if pred[i, j]:
                res[index] = j
                index += 1
            j += 1
        # print(j)
        #print(res)
        index = 0
        for key, values in res.items():
            if values != predictions[0]:
                final_res[index] = values
                print('final_res[index]:',final_res[index])
                index += 1
        #print(final_res)
        jobs_dict = {0:'Digital Signal Processing Engineer',
                    1:'Wireless Communication Engineer',
                    2:'Digital Communication Engineer',
                    3:'Business Analyst',
                    4:'Customer Service Executive',
                    5:'Information Security Engineer',
                    6:'Microwave Engineer',
                    7:'Telecommunication System Engineer',
                    8:'Analog Design Engineer',
                    9:'Optical Communication Engineer',
                    10:'Digital Signal Processing Engineer',
                    11:'RF (Radio Frequency) Engineer',
                    12:'Network Engineer',
                    13:'Project Manager',
                    14:'Embedded Systems Engineer',
                    15:'Power Electronics Engineer',
                    16:'Project Documentation Coordinator'}
                    
        #print(jobs_dict[predictions[0]])
        job = {}
        #job[0] = jobs_dict[predictions[0]]
        index = 1
        
            
        data1=predictions[0]
        print(data1)
        return render_template("testafter.html",final_res=final_res,job_dict=jobs_dict,job0=data1)
@app.route('/result_civil',methods = ['POST', 'GET'])
def result_civil():
    # if 'username' not in session:
    #     return redirect('/signin')
    
    if request.method == 'POST':
        result = request.form
        i = 0
        print(result)
        res = result.to_dict(flat=True)
        print("res:",res)
        arr1 = res.values()
        arr = ([value for value in arr1])
        vector = np.vectorize(np.int_)
        data = np.array(arr)
        
        data = data.reshape(1,-1)
        print(data)
        loaded_model = pickle.load(open("civil.pkl", 'rb'))
        predictions = loaded_model.predict(vector(data))
        # return render_template('testafter.html',a=predictions)
        
        print(predictions)
        pred = loaded_model.predict_proba(vector(data))
        print(pred)
        #acc=accuracy_score(pred,)
        pred = pred > 0.05
        #print(predictions)
        i = 0
        j = 0
        index = 0
        res = {}
        final_res = {}
        while j < 17:
            if pred[i, j]:
                res[index] = j
                index += 1
            j += 1
        # print(j)
        #print(res)
        index = 0
        for key, values in res.items():
            if values != predictions[0]:
                final_res[index] = values
                print('final_res[index]:',final_res[index])
                index += 1
        #print(final_res)
        jobs_dict = {0:'Structural Engineer',
                    1:'Transportation Engineer',
                    2:'Geotechnical Engineer',
                    3:'Business Analyst',
                    4:'Environmental Engineer',
                    5:'Construction Engineer',
                    6:'GIS (Geographic Information Systems) Specialist',
                    7:'Hydraulic Engineer',
                    8:'Materials Engineer',
                    9:'Urban Planner',
                    10:'Environmental Data Analyst',
                    11:'Materials Testing Technician',
                    12:'Remote Sensing Specialist',
                    13:'Project Manager',
                    14:'Simulation Engineer',
                    15:'Land Development Engineer',
                    16:'Surveyor'}
                    
        #print(jobs_dict[predictions[0]])
        job = {}
        #job[0] = jobs_dict[predictions[0]]
        index = 1
        
            
        data1=predictions[0]
        print(data1)
        return render_template("testafter.html",final_res=final_res,job_dict=jobs_dict,job0=data1)
if __name__ == '__main__':
    app.run(debug=True)