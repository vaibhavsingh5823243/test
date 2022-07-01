from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET',"POST"])
def test():
    return "How sexy you are"
   
if __name__=="__main__":
    app.run()
