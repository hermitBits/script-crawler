import logging

from colorlog import ColoredFormatter


def setup_logger(logger_name, log_file=None):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    formatter = ColoredFormatter(
        (
            '%(asctime)s '
            '[%(log_color)s%(levelname)s%(reset)s] '
            '[%(cyan)s%(name)s%(reset)s] '
            '%(message_log_color)s%(message)s'
        ),
        reset=True,
        log_colors={
            'DEBUG': 'bold_cyan',
            'INFO': 'bold_green',
            'WARNING': 'bold_yellow',
            'ERROR': 'bold_red',
            'CRITICAL': 'bold_red,bg_white',
        },
        secondary_log_colors={
            'message': {
                'DEBUG': 'white',
                'INFO': 'bold_white',
                'WARNING': 'bold_yellow',
                'ERROR': 'bold_red',
                'CRITICAL': 'bold_red',
            },
        },
        style='%'
    )

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # Adicionar um manipulador de arquivo, se um arquivo de log for fornecido
    if log_file:
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger