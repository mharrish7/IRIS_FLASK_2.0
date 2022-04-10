
from flask import Flask, jsonify,render_template,request
import joblib
app = Flask(__name__)

model = joblib.load('iris_model')


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/process" ,methods=['POST'])
def ret():
    sl = request.form['sl']
    sw = request.form['sw']
    pl = request.form['pl']
    pw = request.form['pw']

    try:
        pred = model.predict([[sl,sw,pl,pw]])
        print(pred)
        if pred is not None:
            classes = ['setosa','versicolor','virginica']
            return jsonify({'pred' : classes[pred[0]]})
    
        return jsonify({'error':'error'})
    except:
        return jsonify({'error':'error'})


if __name__ == "__main__":
    app.run(debug=True)