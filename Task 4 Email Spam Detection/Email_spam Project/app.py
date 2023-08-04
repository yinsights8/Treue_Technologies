from flask import Flask, jsonify, request

from Data_Preprocessing import remove_spaces, expand, handling_accented, clean_data, autocorrect, lemmatization

import pickle


count_model = pickle.load(open("models/count_vec.pkl","rb"))
mb_model = pickle.load(open("models/Model.pkl","rb"))


app = Flask(__name__)



@app.route("/")
def Home():
    return jsonify({"Response": "This is Home"})



@app.route("/result",methods=["GET", "POST"])
def prediction():
    requested_data = request.get_data(as_text=True)

    if request.method == "POST":
        
        clean_text_train = remove_spaces(requested_data)
        clean_text_train = expand(requested_data)
        clean_text_train = handling_accented(requested_data)
        clean_text_train = clean_data(requested_data)
        clean_text_train = lemmatization(requested_data)

        vector = count_model.transform([clean_text_train])
        print(vector)
        prediction = mb_model.predict(vector)

        result = " "
        if prediction[0] == 1:
            result = "Spam"
        else:
            result = "Not Spam"

    return jsonify({"E-Mail": requested_data, "Prediction made" : result})

if __name__ == "__main__":
    app.run(debug=True,port="8080")