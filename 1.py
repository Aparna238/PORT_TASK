from pathlib import Path
import xml.etree.ElementTree as ET
import pandas as pd
import logging
import argparse

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='task1.log'
                    )    
   
data = []
ns = {'autosar': 'http://autosar.org/schema/r4.0'}

def parse_xml(file,tag):
    tree = ET.parse(file_path)
    root = tree.getroot()
    tag1 = ".//autosar:" + tag

    for application in root.findall(tag1,ns):
            swc_name = application.find('.//autosar:SHORT-NAME', ns).text
            logging.info(f"Found swc_name {swc_name}")
            for port in application.findall('.//autosar:P-PORT-PROTOTYPE',ns):
                port_name = port.find('.//autosar:SHORT-NAME', ns).text
                logging.info(f"Provided port name found : {port_name}")
                interface_type = port.find('.//autosar:PROVIDED-INTERFACE-TREF', ns).get('DEST')
                if interface_type=='SENDER-RECEIVER-INTERFACE':
                    interface_name = port.find('.//autosar:PROVIDED-INTERFACE-TREF', ns).text
                    interface_name = interface_name.split('/')[-1]
                    logging.info(f"Found provided interface_name:  {interface_name}")
                    data.append({'Component_type':tag,'Swc_component':swc_name, 'Swc_port':port_name,'Port_type':'Provided', 'Interface_name':interface_name, 'Interface_type': interface_type})

            for port in application.findall('.//autosar:R-PORT-PROTOTYPE',ns):
                port_name = port.find('.//autosar:SHORT-NAME', ns).text
                logging.info(f"Required port name found : {port_name}")
                interface_type = port.find('.//autosar:REQUIRED-INTERFACE-TREF', ns).get('DEST')
                if interface_type=='SENDER-RECEIVER-INTERFACE':
                    interface_name = port.find('.//autosar:REQUIRED-INTERFACE-TREF', ns).text
                    interface_name = interface_name.split('/')[-1]
                    logging.info(f"Found required interface_name:  {interface_name}")
                    data.append({'Component_type':tag,'Swc_component':swc_name, 'Swc_port':port_name,'Port_type':'Required', 'Interface_name':interface_name, 'Interface_type': interface_type})

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input','-i')
    args = parser.parse_args()

    folder_path = args.input

    parse_folder = Path("Ports_arxml")
    folder_path_2 = folder_path / parse_folder

    for file_path in folder_path_2.iterdir():
        if file_path.suffix == '.arxml':
            logging.info(f"Started parsing {file_path.name}")
            parse_xml(file_path,"SERVICE-SW-COMPONENT-TYPE")
            parse_xml(file_path,"APPLICATION-SW-COMPONENT-TYPE")
            logging.info(f"Parsing done {file_path.name}")

    df = pd.DataFrame(data)
    df = df.drop_duplicates()
    # print(df)
    df.to_excel("1.xlsx",index = False)
   
    

