import time
import schedule

from datetime import datetime
from scraping.register_crawlers import manager


def execute_tasks():
    # importa os crawlers cadastrados, e os executa
    manager.execute_crawlers()


def schedule_task(scheduled_date):
    now = datetime.now()
    delay = scheduled_date - now

    # Agendar a tarefa com o atraso calculado
    schedule.every(delay.seconds).seconds.do(execute_tasks)

    # flag para checar se tarefa agendada já foi executada
    task_completed = False

    while not task_completed:
        schedule.run_pending()
        time.sleep(1)

        # Verificar se a tarefa foi executada
        if datetime.now() >= scheduled_date:
            task_completed = True
