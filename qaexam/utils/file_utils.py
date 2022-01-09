from . import time_utils
import os

TEST_TARGET_FOLDER = '../tests/screenshots_pic'
AUTO_TARGET_FOLDER = 'screenshots_pic'
 
def screenshot_path_name(login: bool) -> str:
    timestamp_str = ''.join(time_utils.curr_time_to_str().split(':'))
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/'+ TEST_TARGET_FOLDER + '/' 
    status = '_success.png' if login else '_failed.png'
    res = dir_path + timestamp_str + status
    return res
