import pandas as pd
import logging 

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='task6.log'
                    ) 

data6 = []
df4 = pd.read_excel('4.xlsx')
df5 = pd.read_excel('5.xlsx')

for ind,rows in df4.iterrows():
        p_core= ""
        r_core= ""
        p_swc = rows['P-port-swc']
        p_swc_name = p_swc + "_EcuSwComposition"
        r_swc = rows['R-port-swc']
        r_swc_name = r_swc + "_EcuSwComposition"
        logging.info(f"P = {p_swc_name}, R = {r_swc_name}")
        for index,row in df5.iterrows():
            if p_swc_name == r_swc_name:
                break
            elif row['swc-name'] == p_swc_name :
                p_core = row['core-no']
            elif row['swc-name'] == r_swc_name:
                r_core = row['core-no']
            if p_core!="" and r_core!="":
                break
        logging.info(f"P_core = {p_core}, R_core = {r_core}")
            
        if p_core != r_core:
            data6.append({"p-core":p_core,"p-port":rows['P-port-name'],"p-port-swc":p_swc,"r-core":r_core,"r-port":rows['R-port-name'],"r-port-swc":r_swc})
            logging.info(f"Different core to appended to data {p_core}-{r_core}")

    
    
    