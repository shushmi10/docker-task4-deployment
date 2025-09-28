from flask import Flask, render_template, request
app = Flask(__name__)

def bmi_value(weight_kg, height_cm):
    h = height_cm / 100.0
    return round(weight_kg / (h*h), 2)

def bmi_label(bmi):
    if bmi < 18.5: return "Underweight"
    if bmi < 25:   return "Normal"
    if bmi < 30:   return "Overweight"
    return "Obese"

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            w = float(request.form.get("weight", "0"))
            h = float(request.form.get("height", "0"))
            b = bmi_value(w, h)
            result = {"bmi": b, "label": bmi_label(b)}
        except Exception as e:
            result = {"error": f"Invalid input: {e}"}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)
