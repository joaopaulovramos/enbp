def get_diarias(data_hora_inicio, data_hora_fim, hospedagem: bool):
    delta_dias = (data_hora_fim - data_hora_inicio).days
    delta_dias_horas = (data_hora_fim - data_hora_inicio).days + (
                ((data_hora_fim - data_hora_inicio).seconds // 3600) / 24)

    if not hospedagem:
        if delta_dias_horas > 0.5:
            if delta_dias_horas >= delta_dias:
                return delta_dias + 0.5
            else:
                return delta_dias
        else:
            return 0
    else:
        if data_hora_fim > data_hora_inicio:
            return delta_dias / 2
        else:
            return 0
