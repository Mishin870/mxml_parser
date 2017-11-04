from xml.dom import minidom


def pretty_xml(xml):
    print('\n'.join([line for line in xml.toprettyxml(indent=' '*2).split('\n') if line.strip()]))


root = minidom.parse('music.xml')
part_list = root.getElementsByTagName('part-list')[0]
# print(pretty_xml(part_list))

parts = root.getElementsByTagName('part')
for part in parts:
    pretty_xml(part)