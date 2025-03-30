import os
import time
import queue
import dotenv
import logging
import logging.config
import logging.handlers

import src.logger_api as logger_api
import src.ZLAC8030D_API as ZLAC8030D_API

dotenv.load_dotenv(dotenv_path=r"C:\Users\Muranyi Peter\OneDrive\Desktop\AG_2025_01_LineDriveControl\data\.env")

def create_app(test_config=None):
    #region Create and initiate modules
    main_path = os.environ.get("main_path", default=r"C:\Users\Muranyi Peter\OneDrive\Desktop\AG_2025_01_LineDriveControl")
    log_path = os.environ.get("core_log_path", default=r"log")
    
    Logger_m = logger_api.Logger_API(LOG_path=os.path.join(main_path, log_path, r"dev.log"))
    # Logger letrehozasa a main process-hez
    logger = Logger_m.config_logger_initial()
    logging.config.dictConfig(Logger_m.config_worker)
    # Queue logger letrehozasa
    Logger_m.start_process()
    time.sleep(1)
    # Logger letrehozasa a main process-hez
    logger = logging.getLogger()
    logger.info(f"Main process PID: {os.getpid()}")
    logger.info(f"Logger process succesfully started! PID: {Logger_m.lp.pid}")

    # Service user
    logger.info(f"Service is managed by {os.getlogin()} user.")

    Controller = ZLAC8030D_API.ZLA8030D(port=os.environ.get("COM", default=r"COM4"), baudrate=os.environ.get("BAUD", default=115200), slave_address=1, logger=logger)















    Logger_m.stop_process()