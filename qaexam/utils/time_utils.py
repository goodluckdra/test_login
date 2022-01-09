from datetime import datetime


TIME_H_M_S = '%Y%m%d%H:%M' 


def curr_time_to_str() -> str:
    '''
    output: 202201012230 ->2022/01/01/ 22:30
    '''
    now = datetime.now()
    current_time = now.strftime(TIME_H_M_S)
    return current_time