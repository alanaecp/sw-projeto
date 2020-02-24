from flask_wtf import Form
from wtforms.fields import IntegerField, StringField, SubmitField, SelectField
from wtforms import validators

class EfemeridesForm(Form):
    descricao = StringField('Descrição', [
        validators.Length(min=2,max=50),
        validators.DataRequired()
        ])
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
