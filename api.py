from flask import Flask, request

app = Flask(__name__)

nodes = {}

nodes["All"] = ["Dawid", "Adrian", "Monika","Magda", "Laura", "Marlena", "Iwona"]
nodes["Daniel"] = ["Dawid", "Adrian", "Monika", "Magda"]
nodes["Dawid"] = ["Laura", "Marlena", "Iwona"]


haveCameras = ["Marlena"]
def haveCamera(name):
    for owner in haveCameras:
        if owner == name:
            return owner
def search(name):
    checkList = nodes[name]
    cheked = []
    while checkList:
        person = checkList.pop(0)
        if not person in cheked:
            if haveCamera(person):
                return person
            else:
                try:
                    checkList += nodes[person]
                    cheked.append(person)
                except:
                    cheked.append(person)



@app.route("/camera", methods = ["GET"])
def haveCameraCheck():
       return '''
    <form action="/have" method="get"">
  <label for="name">Name:</label><br>
  <input type="text" id="name" name="name" value=""><br>
  <input type="submit" value="Submit">
</form>
        
        '''
@app.route("/have", methods = ["GET"])
def returnCameraCheck():
        name = request.args.get('name')
        try:
            result = search(name)
            if result != None:

                    try:
                        return f'''
            Najblizej do {name}, kamere ma {result}
                <form action="/">
        <input type="submit" value="Go to Main" />
        </form>
            '''
                    except:
                        return f'''
                {name} nie ma znajomych
                    <form action="/">
        <input type="submit" value="Go to Main" />
        </form>
                '''
            
                
        except: 
            return f'''
                Nikt z nich, nie ma kamery
                    <form action="/">
        <input type="submit" value="Go to Main" />
        </form>
                '''


@app.route("/all")
def allPersons():
    return f'''<p> {','.join(nodes["All"])} </p>
     <form action="/">
    <input type="submit" value="Go to Main" />
    </form>'''

    # return f'''<p> {nodes["All"]} </p>'''


@app.route("/")
def addPersonPage():
    return '''

<form action="/add">
    <input type="submit" value="Add" />
    </form>
<form action="/all">
    <input type="submit" value="See all" />
    </form>
<form action="/camera">
    <input type="submit" value="Have camera" />
    </form>
'''


@app.route('/add',methods=['GET','POST'])
def addPage():
    if request.method == "POST":
        user = request.form['name']
        friend = request.form['connectwith']
        camera = request.form['camera']

        try:
            nodes[user] += [friend]
        except:
            nodes[user] = [friend]
        nodes["All"] += [friend, user]
        return f'''Added: {user}.<br>Friends with: {friend}<br>   
           <form action="/">
    <input type="submit" value="Go to Main" />
    </form>
    <form action="/all">
    <input type="submit" value="See all" />
    </form>'''
    else:    
        return '''
    <form action="/add" method="post"">
  <label for="name">Name:</label><br>
  <input type="text" id="name" name="name" value=""><br>
  <label for="connectwith">Connect with:</label><br>
  <input type="text" id="connectwith" name="connectwith" value=""><br>
<label for="camera">Have camera:</label><br>
  <input type="text" id="camera" name="camera" value=""><br><br>
  <input type="submit" value="Submit">
</form>

'''



app.run()
