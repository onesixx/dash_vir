from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import pandas as pd

from frontend.common.dconfig import base_dir
# base_dir = '/Users/onesixx/my/git/dash_vir'
import pandas as pd


def df_dash_data():   
    data = pd.read_csv('./data/dash_summary_small_data.csv')
    # return data.to_json(date_format='iso' , orient='split')
    return data

def df_dash_raw_data():   

    data = pd.read_csv('./data/big_data.csv')
    data = data.iloc[0:6000000, [3,4,5,6,7,15,21,30]]
    # return data.to_json(date_format='iso' , orient='split')
    return data

def df_dash_q_data():   
    data = pd.read_csv(base_dir+'/data/q_data.csv')
    # return data.to_json(date_format='iso' , orient='split')
    return data


def df_dash_polar_data():   
    data = pd.read_csv('./data/gradar.csv')
    return data



def df_data_status(sStartDate, sEndDate, sBankNo):
    # sStartDate = '2022-01-01'
    # sEndDate = '2022-01-10'
    # sBankNo=1
    data = pd.read_csv(base_dir+'/data/data_status.csv')
    print("-----------------MODEL--------------------")
    data["cyc_date"] = data["cyc_date"].apply(str)

    data = data[(data["bank_no"] == int(sBankNo)) &
                (data["cyc_date"] >= sStartDate.replace('-', '')) &
                (data["cyc_date"] <= sEndDate.replace('-', ''))]
    data = data.sort_values(by=['bank_no', 'cyc_date'], ascending=False)
    # rename columns 
    data.columns = ['a', 'Date', 'Bank', 'Voltage', 'Current', 'ChargeQ', 'SunShine',
                    'DataCount', 'DataFail', 'UseYN', 'UseDesc', 'DTime', 'WeekDay', 'sid']
    selected_col = ['Date', 'WeekDay', 'Bank', 'Voltage', 'Current', 'ChargeQ', 'DataCount', 'DataFail', 'UseYN', 'UseDesc']
    return data[selected_col]



def df_dash_data_box(sCycDate,sBankNo): 
    # data = dataTable_column = pd.DataFrame({
    #                                         'bank_no'       : [1,2,3] ,
    #                                         'voltage'       : [1075.1, 1065.3, 1074.3],
    #                                         'voltage_per'   : [90, 91.1, 92.2],
    #                                         'current_c'     : [17, 18, 17.5],
    #                                         'current_c_per' : [96, 97.1, 95.2],
    #                                         'current_d'     : [24.1, 23.5, 24.5],
    #                                         'current_d_per' : [96, 97.1, 95.2],
    #                                         'charge_q'      : [106.2, 105.4, 109.8],
    #                                         'charge_q_per'  : [93, 94.1, 95.3],
    #                                         'datacount'     : [43200,43201,43202],
    #                                         'datacount_per' : [100,99.8,100],
    #                                         'datafail'      : [0,0,0] ,
    #                                         'datafail_per'  : [0,0,0]
    #                                     })

    data = pd.read_csv('./data/box_data.csv')
    data['cyc_date'] = data['cyc_date'].apply(str)
    data = data[(data["bank_no"]==int(sBankNo)) & (data["cyc_date"]==sCycDate.replace('-','')) ]

    return data
    



    