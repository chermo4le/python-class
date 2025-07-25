from flask import Flask, request, jsonif 
from cliente #importa el archivo de cliente

app = Flask(__name__)
@app.route("/clientes",methods=["post"])
def buscar_cliente():
    data = request.get_json()

    ci = data.get("ci")

    if not ci:
        return jsonif({"error":"falta el campo ci"}),400
    resultado = cliente.consultar_cliente 
    if resultado:
        return jsonif(resultado)
    else:
        return jsonif({"mensaje":"cliente no encontrado"}),404

    if __name__=="__main__":
        app.run(port=5003)