from flask import Flask, flash, render_template, request, redirect, url_for # Importar a biblioteca Flask
from flask_sqlalchemy import SQLAlchemy
from funcoes import *
from forms import EfemeridesForm
from model import *


app = Flask(__name__)

# Definir rotas

@app.route('/')
def index():
    hj, dia, mes, ano = hoje()
    data_em_texto = []

    linha1 = 'Hoje é {}'.format(extenso(dia, mes, ano))
    linha2 = 'Hoje é o {}º dia de {} e o {}º {}.'.format(dia_do_ano_dt(hj),ano, semana_do_ano_dt(hj), dia_da_semana_dt(hj))
    linha3 = 'Há {} dias restantes em {}'.format(ate_o_fim_do_ano_dt(hj),ano)

    data_em_texto.append(linha1)
    data_em_texto.append(linha2)
    data_em_texto.append(linha3)

    efemerides = Efemerides.query.filter_by(mes = mes, dia = dia).all()
    # efemerides = Efemerides.query.all()
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/

    temp = [descricao  for descricao in efemerides if dia == dia and mes == mes]
    return render_template('index.html', efemerides=efemerides, data_em_texto = data_em_texto )

@app.route('/todos')
def todos():
    efemerides = Efemerides.query.all()
    return render_template('todos.html', efemerides=efemerides )


@app.route('/cadastrar', methods = ['GET','POST'])
def cadastrar():

    if request.method == 'POST':
        form = EfemeridesForm(request.form)

        if form.validate():
            # descricao, dia, mes, ano_primeira_ocorrencia
            novo = Efemerides(request.form['descricao'],request.form['dia'],request.form['mes'], request.form['ano_primeira_ocorrencia'] )
            db.session.add(novo)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return redirect(url_for('cadastrar'))

    elif request.method == 'GET':

        form = EfemeridesForm()
        return render_template('cadastrar.html', form = form)



@app.route('/localizar', methods = ['GET','POST'])
def localizar():
    if request.method == 'POST':
        # localizar
        dia = request.form['dia']
        mes = request.form['mes']

        efemerides = Efemerides.query.filter_by(mes = mes, dia = dia).all()
        return render_template('data.html', efemerides = efemerides, dia = dia, mes = mes_extenso(mes))
    else:
        form = EfemeridesForm()
        return render_template('localizar.html', form = form)

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'este é uma chave super secreta'
db = SQLAlchemy(app)



# Roda a aplicação
if __name__ == "__main__":
    db.create_all()  # cria as tabelas
    app.run(debug=True, port=8085)
