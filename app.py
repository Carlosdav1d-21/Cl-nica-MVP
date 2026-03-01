from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok", service="api")

@app.get("/records/<patient_id>")
def get_record(patient_id):
    # MVP: aquí luego conectamos a SQL Server con consultas parametrizadas.
    return jsonify(patient_id=patient_id, record="(demo)")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
