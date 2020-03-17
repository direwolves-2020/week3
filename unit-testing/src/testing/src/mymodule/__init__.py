import os
import os.path
import matplotlib.pyplot as plt


class RemovalService(object):
    """Sample class that wraps the rm os call"""

    def rm(self, file_name):
        if os.path.isfile(file_name):
            os.remove(file_name)
