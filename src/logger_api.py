import time
import yaml
import logging
import datetime
import logging.config
import logging.handlers
import multiprocessing as mp


class CustomLogFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super(CustomLogFormatter, self).formatException(exc_info)
        return repr(result)
    def format(self, record):
        d = {
            't': datetime.datetime.fromtimestamp(record.created).astimezone().isoformat(),
            'l': record.levelno,
            'm': record.msg,
        }
        ei = record.exc_info
        if ei is not None:
            d['ei'] = ei[0:2]
            d['ei0'] = str(ei[0])
            d['ei1'] = str(ei[1])
            et = record.exc_text
            if et is not None:
                d['et'] = et
            si = record.stack_info
            # if si is not None:
            #     d['si'] = si
        return yaml.dump(data=d, explicit_start=True, explicit_end=True, default_flow_style=False)


class QueueListenerHandler:
    def handle(self, record):
        if record.name == "root":
            logger = logging.getLogger()
        else:
            logger = logging.getLogger(record.name)
        if logger.isEnabledFor(record.levelno):
            logger.handle(record)


class Logger_API:
    def __init__(self, LOG_path) -> None:
        self.log_queue = mp.Queue()
        self.stop_e = mp.Event()
        self.lp = None
        self.LOG_path = LOG_path

        self.config_initial = {
            'version': 1,
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'INFO',
                },
            },
            'root': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
        }

        self.config_worker = {
            'version': 1,
            'disable_existing_loggers': True,
            'handlers': {
                'queue': {
                    'class': 'logging.handlers.QueueHandler',
                    'queue': self.log_queue,
                },
            },
            'root': {
                'handlers': ['queue'],
                'level': 'DEBUG',
            },
        }


        self.config_listener = {
            'version': 1,
            'disable_existing_loggers': True,
            'formatters': {
                'detailed': {
                        'class': 'logging.Formatter',
                        'format': '%(asctime)s %(name)s %(levelname)s\t%(filename)s\t%(message)s',
                    },
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'detailed',
                    'level': 'INFO',
                },
                'file': {
                    'class': 'logging.handlers.TimedRotatingFileHandler',
                    'formatter': 'detailed',
                    'filename': str(self.LOG_path),
                    'when': 'midnight',
                    'backupCount': 14,
                    'encoding': 'utf-8',
                },
            },
            'root': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
            },
        }

    def start_process(self):
        # Queue logger letrehozasa
        self.lp = mp.Process(target=self.log_listener_process, name='listener',
                    args=(self.log_queue, self.stop_e, self.config_listener,))
        self.lp.start()

    def stop_process(self):
        self.stop_e.set()
        self.lp.join()

    def log_listener_process(self, q, stop_event, config):
        # print("log_listener_process", os.getpid())
        logging.config.dictConfig(config)
        listener = logging.handlers.QueueListener(q, QueueListenerHandler())
        listener.start()
        # if os.name == 'posix':
        #     logger = logging.getLogger('setup')
        stop_event.wait()
        listener.stop()


    def config_logger_initial(self):
        # Queue logger letrehozasa
        logging.config.dictConfig(self.config_initial)
        logger = logging.getLogger('setup')
        last_saver_queue_warning = time.monotonic()
        last_times_warning = time.monotonic()

        return logger


if __name__ == "__main__":
    Logger_m = Logger_API()
    