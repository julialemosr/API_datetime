from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/verificar_data/<ano>-<mes>-<dia>')
def verificar_data(ano,mes,dia):
    try:
        ano = int(ano)
        mes = int(mes)
        dia = int(dia)

        data_recebida = datetime.datetime(ano, mes, dia).date()
        data_atual = datetime.datetime.now().date()


        dia_diferenca = data_atual - data_recebida
        meses_diferenca = (data_atual.year - data_recebida.year) * 12
        anos_diferenca = data_atual.year - data_recebida.year

        if data_recebida > data_atual:
            situacao = "Futuro"
        elif data_recebida < data_atual:
            situacao = "Passado"
        else:
            situacao = "Presente"

        return jsonify({
            'situacao': situacao,
            'dias_diferenca': str(dia_diferenca),
            'meses_diferenca': meses_diferenca,
            'anos_diferenca': anos_diferenca,
        })

    except ValueError:
        return jsonify({
            'erro':'valor inválido'
        })

if __name__ == '__main__':
    app.run(debug=True)