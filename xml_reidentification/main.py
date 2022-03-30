import glob


img_folder='E:/reannotation/all'

import xml.etree.ElementTree as ET



for xml_file in glob.glob(img_folder+'/*.xml'):
    # print(xml_file)
    mytree = ET.parse(xml_file)
    myroot = mytree.getroot()
# iterating through the price values.
    for prices in myroot.iter('name'):
        # updates the price value
        # print(prices.text)
        if prices.text in ['player', 'referee', 'other']:
            prices.text = 'person'
            # print(prices.text)
        elif prices.text =='ball':
            prices.text='sports ball'
            # print(prices.text)
    for diff in myroot.iter('difficult'):
        diff.text=str(0)
    mytree.write(xml_file)



