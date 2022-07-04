from flask  import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
  return render_template('index.html')

@app.route('/<data>')
def calcula_presidente(data):
  if 70 > int(data) >= 35:
    resultado = 'Ja pode ser PRESIDENTE'
    return jsonify({'Resultado':resultado})
  elif int(data) >= 70:
    resultado = 'Nao acha que esta muito velho para ser PRESIDENTE'
    return jsonify({'Resultado':resultado})  
  elif int(data) < 0:
    resultado = 'Nem nasceu ainda'
    return jsonify({'Resultado':resultado})
  elif int(data) > 1000:
    resultado = 'Ja esta sentado ao lado de Deus'
    return jsonify({'Resultado':resultado})
  else:
    resultado = (f'Faltam {35 - int(data)} anos para voce poder ser PRESIDENTE')
    return jsonify({'Resultado':resultado})


app.run(host='0.0.0.0')
