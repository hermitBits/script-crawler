import os

from datetime import datetime
from prompt_toolkit import prompt


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_appointment():
    while True:
        clear()
      
        try:
            day = int(prompt('Selecione um dia para agendar: '))
            month = int(prompt('Selecione um mês para agendar: '))
            year = int(prompt('Selecione um ano para agendar: '))

            hour = prompt('Digite a hora para agendar (formato 24 horas, por exemplo, 14:30): ')

            hour_split = hour.split(':')

            # Tentar criar um objeto datetime com os valores fornecidos
            appointment_date = datetime(year, month, day, int(hour_split[0]), int(hour_split[1]))

            # Validar se a data é maior que o tempo atual
            if appointment_date > datetime.now():
                clear()
                print('Agendado, não fechar script!')
                return appointment_date
            else:
                print("A data e hora devem ser maiores que o tempo atual.")
                input('Pressione Enter para tentar novamente...')

        except Exception as e:
            print(f'Erro: {e}')
            input('Pressione Enter para tentar novamente...')