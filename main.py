from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        "id":1,
        "contact":"9242134304",
        "name":"ram",
        "done":"false"
    },
    {
        "id":2,
        "contact":"9825639123",
        "name":"raju",
        "done":"true"
    }
]
@app.route("/add_data",methods=["POST"])
def addtasks():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        })
    task={
        "id":tasks[-1]["id"]+1,
        "contact":request.json["contact"],
        "name":request.json.get("name","")
    }
    tasks.append(task)
    return jsonify({
            "status":"success",
            "message":"task added successfully"
        })
@app.route("/get_data")
def get_data():
    return jsonify({
            "data":tasks
        })
if __name__=="__main__":
    app.run()