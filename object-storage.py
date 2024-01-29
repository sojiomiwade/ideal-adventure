from flask import Flask, request

'''
/reponame
/foo.jpg
4839-3AFED
1
a 1
a 3
a 2
b x
c y
how to know the latest version for a given object

you would need a table for object to latest-version. 
get that number, then come back to query by version-id
where key is object-name and version-id

alternatively, have a history table 
when a new version of object comes in, move older version to history
and keep current in the current table (OLF did this)
now key can just be object name with sublinear complexity

object
object_history
workers can asynchronously update backend
'''

app = Flask(__name__)
mdata=[]

@app.route('/')
def hello():
    return 'Hello, this is your simple HTTP service!'

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_data(as_text=True)
    return f'ECHO: {data}'

@app.route('/create', methods=['PUT'])
def create():
    objectname = request.get_data(as_text=True)
    # Here, you can process the data and create something.
    # For simplicity, let's just echo the creation message.
    omdata=(bucketname,objectname,objectid,version)
    mdata.append(omdata)
    object.append()
    return f'Created: {data}'

if __name__ == '__main__':
    app.run(debug=True)

