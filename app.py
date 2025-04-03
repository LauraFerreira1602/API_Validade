# importar biblioteca
from flask import Flask, jsonify, render_template
# importe para documentacao
from flask_pydantic_spec import FlaskPydanticSpec
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

# [flask routes] para listar rotas da api

# criar variavel para receber a classe Flask
app = Flask(__name__)

#   documentacao OpenAPI
spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0')
spec.register(app)

@app.route('/validade/<quantidade>/<tempo>')
def validade_(quantidade, tempo):
    """
            API para ver a validade

            ## Endpoint:
            'GET /validade/<quantidade>/tempo>'

            ## Parâmetros:
            - 'quantidade' - (int): quantidade
            - 'tempo' - (str): tempo
                - ** Qualquer outro formato resultara em erro. **

            ## Resposta (JSON):
            ''' json
                {"quantidade":
                    "tempo":}
            '''

            ## Erros possiveis:
            - Se o formato da data não for correto, resultara em {'Error': 'Invalido'}

        """
    try:
        prazo = int(quantidade)
        meses = datetime.today()+relativedelta(months=prazo)
        # years
        anos = datetime.today()+relativedelta(years=prazo)
        # weeks
        semanas = datetime.today()+relativedelta(weeks=prazo)
        # days
        dias = datetime.today()+relativedelta(days=prazo)

        data_validade = ""
        print(tempo,f"hhh{tempo == "ano"}")
        if tempo == "ano":
            data_validade = anos

        elif tempo == "meses" or tempo == "mes":
            data_validade = meses

        elif tempo == "semanas" or tempo == "semana":
            data_validade = semanas

        elif tempo == "dias" or tempo == "dia":
            data_validade = dias
        else:
            return jsonify({
                'Error': 'invalido'
            })

        return jsonify(
            {
            "Cadastro": datetime.today().strftime("%d/%m/%Y"),
            "Tempo": tempo,
            "Tipo (dia,semana,mes ou ano)": data_validade,
            "Validade": data_validade
            }
        )

    except ValueError:
        return jsonify({
            'Error': 'Invalido'
        })


# iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)