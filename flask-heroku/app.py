from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "hello wwwww"
@app.route("/tes")
def test():
    return "test"

if __name__ == '__main__':
    app.run(debug=True,port="3030")
