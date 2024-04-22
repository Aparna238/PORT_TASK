from pathlib import Path
import xml.etree.ElementTree as ET
import pandas as pd
import logging
import argparse

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='task2.log'
                    )    
   
data = []
ns = {'autosar': 'http://autosar.org/schema/r4.0'}

def parse_xml(file,tag):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for interface in root.findall(tag,ns):
            interface_name = interface.find('.//autosar:SHORT-NAME', ns).text
            logging.info(f"Found interface swc: {interface_name}")
            for type in interface.findall('.//autosar:TYPE-TREF',ns):
                interface_type = type.get('DEST')
                interface_type_ref = type.text
                interface_type_ref = interface_type_ref.split('/')[-1]
                logging.info(f"Found interface type reference: {interface_type_ref}")
                data.append({'interface_name':interface_name, 'interface_type':interface_type,'interface_type_ref':interface_type_ref})

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input','-i')
    args = parser.parse_args()

    folder_path = Path(args.input)

    for file_path in folder_path.iterdir():
        if file_path.name == 'PortInterfaces.arxml':
            logging.info(f"Started parsing {file_path.name}")
            parse_xml(file_path,".//autosar:SENDER-RECEIVER-INTERFACE")
            logging.info(f"Parsing done {file_path.name}")

    df = pd.DataFrame(data)
    df = df.drop_duplicates()
    # print(df)
    df.to_excel("2.xlsx",index = False)



