import xml.etree.ElementTree as ET
import os

def xml_parsing(file):
    f = (file)
    tree = ET.parse(f)
    root = tree.getroot()
    # for child in root:
    #    print(child.tag, child.attrib)
    # scheme_elem = root.find('docPublishDate')
    # print (scheme_elem.tag)
    for elem in root.iter():
        pass
        print(elem.tag, elem.attrib)
    os.remove(file)


if __name__ == '__main__':
    f = (f'tmp/notification_Sankt-Peterburg_2014010100_2014020100_122.xml/'
         f'fcsNotificationEA44_0145100003014000001_17217.xml')
    tree = ET.parse(f)
    root = tree.getroot()
    #for child in root:
    #    print(child.tag, child.attrib)
    #scheme_elem = root.find('docPublishDate')
    #print (scheme_elem.tag)

    for elem in root.iter():
        print(elem.tag, elem.attrib)