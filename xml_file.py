import xml.etree.ElementTree as ET
import os
from logger import logger


def xml_parsing(file):
    f = (file)
    tree = ET.parse(f)
    root = tree.getroot()
    # for child in root:
    #    print(child.tag, child.attrib)
    # scheme_elem = root.find('docPublishDate')
    # print (scheme_elem.tag)
    for elem in root.iter():
        if 'fcsNotificationEF' in elem.tag and elem.attrib['schemeVersion'] != '1.0':
            print('err')
            logger(f'{elem.tag, elem.attrib, file}', 'scheme')
        elif elem.tag == 'id':
            print(elem.tag, elem.attrib, elem.text)
            not_id = elem.text
        elif 'purchaseNumber' in elem.tag:
            not_purch_num = elem.text
        elif 'href' in elem.tag:
            not_href = elem.text
        elif 'maxPrice' in elem.tag:
            not_price = elem.text
    os.remove(file)
    print(file)
    return not_id, not_purch_num, not_href, not_price


if __name__ == '__main__':
    f = (f'./tmpxml/notification/fcsNotificationEA44_0145100003014000001_17217.xml')
    tree = ET.parse(f)
    root = tree.getroot()
    #for child in root:
    #    print(child.tag, child.attrib)
    #scheme_elem = root.find('docPublishDate')
    #print (scheme_elem.tag)

    for elem in root.iter():
        print(elem.tag, elem.attrib, elem.text)
