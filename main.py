from prompt_toolkit import prompt

from utils.display import get_appointment
from scraping.schedule import schedule_task, execute_tasks


def menu():
    print("1. Agendar tarefa")
    print("2. Executar agora")
    print("3. Sair")
    return prompt('Escolha uma opção: ')


if __name__ == '__main__':
    scheduled_date = None
    while True:
        
        opcao = menu()
        
        ## agendar
        if opcao == '1':
            scheduled_date = get_appointment()
            schedule_task(scheduled_date)
        # executar imediatamente
        elif opcao == '2':
            execute_tasks()
        # sair
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")