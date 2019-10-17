'''
For the XML file get a list of all data attributes and print them. Then print the first 5 calEvent Nodes
'''
import xml.etree.ElementTree as ET

tree = ET.parse('festivals-and-events-historical-xml-feed-jan-2014-dec-2016.xml')
root = tree.getroot()

count = 0

for item in root[0]:
    print(item.attrib)

root = root[0:5]

for item in root:
    count += 1
    print('CalEvent No: %s' %(count))
    for item2 in item:
        print('- '+ item2.attrib.get('name'))
        if item2[0].text is None:
            for item3 in item2:
                for item4 in item3:
                    print(item4.text)
        else:
            print(item2[0].text)
                
        