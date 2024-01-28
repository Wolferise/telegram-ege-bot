from datetime import datetime
import inspect
import os
import traceback

# logger class (should be singleton)
class Logger:
    def __init__(self):
        # setting log file relative path (./logs/<logfile_name>) and name
        cur_timestamp = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        self.logfile_name = '-'.join([cur_timestamp, 'bot.log'])
        self.logfile_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', self.logfile_name)

    def log(self, type, message):
        cur_timestamp = str(datetime.now())
        if type == 'ERROR':
            # get error info from python
            caller = ' | '.join([inspect.stack()[2][3], 'CONTEXT: ' + inspect.stack()[2][4][0].strip(' \n')])
        else:
            # get caller function name for logging
            caller = inspect.stack()[1][3]
        # format log
        log =  ' | '.join([cur_timestamp, type, caller, message])
        # print into console
        print(log)
        # append line to logfile
        with open(self.logfile_path, 'a') as f:
            f.writelines([log, '\n'])
            f.close()
    
    # decorator function for telegram bot for managing exceptions
    def crash_log(self, func):
        def wrap(*args):
            # try-catch for the decorated function
            try:
                func(*args)
            except BaseException as e:
                # if any exception is caught, save error logs
                self.log('ERROR', getattr(e, 'message', str(e)).replace('\n', '\\n').replace('\r', '\\r')[:989])
                self.log('ERROR', traceback.format_exc())
        return wrap
