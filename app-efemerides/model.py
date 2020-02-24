# Criando o modelo
from efemerides import db

class Efemerides(db.Model):
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
