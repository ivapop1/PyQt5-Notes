#!/usr/bin/env python3

import sys
import os
import logging.config

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QTranslator, QLocale, QLibraryInfo

from app_modules.views import AppView
from app_modules.controller import AppController


def main():
    # instance of 'QApplication'
    app = QApplication([])
    

    # render the view
    view = AppView()
    view.show()
    # instance of the controller
    ctrl = AppController(view=view)
    logger.info("Started a reminder app")
    sys.exit(app.exec_())


if __name__ == '__main__':
    # setting logger's config
    logging.config.fileConfig('data/logger.conf', disable_existing_loggers=False)
    #translate
    
    
    # setting up logger
    logger = logging.getLogger(__name__)

    main()
