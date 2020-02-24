from flask import Flask, render_template, request, redirect, url_for# Importar a biblioteca Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms.fields import IntegerField, StringField, SubmitField, SelectField
from funcoes import *




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

    eufemerides = Eufemerides.query.filter_by(mes = mes, dia = dia).all()
    # eufemerides = Eufemerides.query.all()

    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/

    temp = [descricao  for descricao in eufemerides if dia == dia and mes == mes]
    return render_template('index.html', eufemerides=eufemerides, data_em_texto = data_em_texto )


@app.route('/cadastrar', methods = ['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        # descricao, dia, mes, ano_primeira_ocorrencia
        novo = Eufemerides(request.form['descricao'],request.form['dia'],request.form['mes'], request.form['ano_primeira_ocorrencia'] )
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('index'))

    elif request.method == 'GET':

        form = EufemeridesForm()
        return render_template('cadastrar.html', form = form)



@app.route('/localizar', methods = ['GET','POST'])
def localizar():
    if request.method == 'POST':
        # localizar
        dia = request.form['dia']
        mes = request.form['mes']

        eufemerides = Eufemerides.query.filter_by(mes = mes, dia = dia).all()
        return render_template('data.html', eufemerides = eufemerides, dia = dia, mes = mes_extenso(mes))
    else:
        form = EufemeridesForm()
        return render_template('localizar.html', form = form)

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'este é uma chave super secreta'
db = SQLAlchemy(app)


# Criando o modelo
class Eufemerides(db.Model):
  id = db.Column(db.Integer, primary_key = True, autoincrement=True)
  descricao = db.Column(db.String(300), nullable= False)
  dia = db.Column(db.Integer(), nullable= False)
  mes = db.Column(db.Integer(), nullable= False)
  ano_primeira_ocorrencia = db.Column(db.Integer(), nullable= True)

  def __str__(self):
      if self.ano_primeira_ocorrencia:
          return '{} ({}/{}/{})'.format(self.descricao, self.dia, self.mes, self.ano_primeira_ocorrencia)
      return '{} ({}/{})'.format(self.descricao, self.dia, self.mes)

  def __init__(self, descricao, dia, mes, ano_primeira_ocorrencia):
      self.descricao = descricao
      self.dia = dia
      self.mes = mes
      self.ano_primeira_ocorrencia = ano_primeira_ocorrencia



class EufemeridesForm(Form):
    descricao = StringField('Descrição')
    dia = IntegerField('Dia')
    mes = SelectField('Mês', choices=[
        ('0', 'Selecione .. '),
        ('1', 'Janeiro'),
        ('2', 'Fevereiro'),
        ('3', 'Março'),
        ('4', 'Abril'),
        ('5', 'Maio'),
        ('6', 'Junho'),
        ('7', 'Julho'),
        ('8', 'Agosto'),
        ('9', 'Setembro'),
        ('10', 'Outubro'),
        ('11', 'Novembro'),
        ('12', 'Dezembro'),
        ])

    ano_primeira_ocorrencia= IntegerField('Ano primeira ocorrência')
    submit = SubmitField('Cadastrar')

# Roda a aplicação
if __name__ == "__main__":
    db.create_all()  # cria as tabelas
    app.run(debug=True, port=8085)
