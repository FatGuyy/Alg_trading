"""
This file just sums up all the files and runs them.
"""

import utils as utils
import mins_15 as mins_15
import ema_5 as ema_5

run_once = True
while run_once:
    mins_15.check_15mins()
    
    ema_5.ema_5()

    run_once = False
    # sleep(300)
