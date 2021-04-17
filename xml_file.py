import xml.etree.ElementTree as ET
import os
from logger import logger


def xml_parsing(file_name):
    _f = file_name
    tree = ET.parse(_f)
    root = tree.getroot()
    for elem in root.iter():
        if 'fcsNotificationEF' in elem.tag and elem.attrib['schemeVersion'] != '1.0':
            logger(f'{elem.tag, elem.attrib, file_name}', 'scheme')
            break
        elif elem.tag == '{http://zakupki.gov.ru/oos/types/1}id':
            _not_id = elem.text
        elif 'purchaseNumber' in elem.tag:
            _not_purch_num = elem.text
        elif 'href' in elem.tag:
            _not_href = elem.text
        elif 'maxPrice' in elem.tag:
            _not_price = elem.text
    os.remove(file_name)
    logger(f'{file_name} parsed and removed', 'xml_parsing')
    return _not_id, _not_purch_num, _not_href, _not_price


def test_parsing(file_name):
    _f = file_name
    print(file_name)
    tree = ET.parse(f)
    root = tree.getroot()
    for elem in root.iter():
        print(elem.tag)


if __name__ == '__main__':
    f = f'./tmpxml/notification/notification_Sankt-Peterburg_2014010100_2014020100_122.xml/fcsNotificationEP44_0372100030814000563_1046.xml'
    # test_parsing(f)
    not_id, not_purch_num, not_href, not_price = xml_parsing(f)
    print(not_id, not_purch_num, not_href, not_price)
