# Set up your imports here!
# import ...

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Fuck yeah I made the page</h1>"

@app.route('/puppy-latin/<name>') 
def puppylatin(name):
    original_name = name
    pup_name = name.split(' ')
    for i in range(0,len(pup_name)):
        if pup_name[i][-1] == 'y':
            pup_name[i]=pup_name[i].replace('y','iful')
        else:
            pup_name[i] += 'y'
    pup_name = ' '.join(pup_name)
    return 'Submitted Puppy Name: {one}<br>Puppy Latin Name: {two}'.format(one=original_name,two =pup_name)






if __name__ == '__main__':
    # Fill me in!
    app.run()
