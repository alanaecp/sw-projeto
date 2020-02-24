from datetime import date

# def extenso1(dia, mes, ano):
#     meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
#     return "{} de {} de {}".format(dia, meses[int(mes)-1].lower(), ano)


def hoje():
    hoje = date.today()
    dia = hoje.day
    mes = hoje.month
    ano = hoje.year
    return hoje, dia, mes, ano
def extenso(dia, mes, ano):
    meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
    return "{} de {} de {}".format(dia, meses[mes].lower(), ano)


def dia_da_semana(dia, mes, ano):
    data = date(ano, mes, dia) #  date(ano, mes, dia)
    # 0 - segunda, 1 -terça-feira, 2 - quarta, 3 -quinta, 4-sexta, 5 - sabado, 6 - domingo
    semana ={ 0: 'segunda-feira', 1: 'terça-feira', 2: 'quarta-feira', 3: 'quinta-feira', 4: 'sexta-feira', 5: 'sábado', 6 : 'domingo'}
    return semana[data.weekday()]


def ate_o_fim_do_ano(dia, mes, ano):
    data = date(ano, mes, dia) #  date(ano, mes, dia)
    fim_do_ano = date(ano, 12, 31) #  date(ano, mes, dia)
    qde_dias = fim_do_ano.toordinal() - data.toordinal()
    return qde_dias


def dia_do_ano(dia, mes, ano):
    data = date(ano, mes, dia) #  date(ano, mes, dia)
    ultimo_dia_do_ano_passado = date(ano-1, 12, 31) #  date(ano, mes, dia)
    qde_dias = data.toordinal() - ultimo_dia_do_ano_passado.toordinal()
    return qde_dias


def adicionar_dias(dia, mes, ano, qde_dias):
    data = date(ano, mes, dia) #  date(ano, mes, dia)
    nova_data = date.fromordinal(data.toordinal() + qde_dias)
    return nova_data


# === from Date type

def mes_extenso(mes):
    meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
    return meses[int(mes)]

def extenso_dt(data):
    meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
    return "{} de {} de {}".format(data.day, meses[data.month].lower(), data.year)


def ate_o_fim_do_ano_dt(data):
    fim_do_ano = date(data.year, 12, 31) #  date(ano, mes, dia)
    qde_dias = fim_do_ano.toordinal() - data.toordinal()
    return qde_dias

def dia_da_semana_dt(data):
    # 0 - segunda, 1 -terça-feira, 2 - quarta, 3 -quinta, 4-sexta, 5 - sabado, 6 - domingo
    semana ={ 0: 'segunda-feira', 1: 'terça-feira', 2: 'quarta-feira', 3: 'quinta-feira', 4: 'sexta-feira', 5: 'sábado', 6 : 'domingo'}
    return semana[data.weekday()]

def dia_do_ano_dt(data):
    ultimo_dia_do_ano_passado = date(data.year-1, 12, 31) #  date(ano, mes, dia)
    qde_dias = data.toordinal() - ultimo_dia_do_ano_passado.toordinal()
    return qde_dias

def semana_do_ano_dt(data):
    ultimo_dia_do_ano_passado = date(data.year-1, 12, 31) #  date(ano, mes, dia)
    qde_dias = len([ x for x in range(ultimo_dia_do_ano_passado.toordinal(), data.toordinal()+1) if date.fromordinal(x).weekday() == data.weekday() ])
    return qde_dias

def adicionar_dias(data, qde_dias):
    nova_data = date.fromordinal(data.toordinal() + qde_dias)
    return nova_data
