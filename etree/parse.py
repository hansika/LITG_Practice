# various ways of parsing xml files
from io import BytesIO
from lxml import etree

# using the fromstring() function to parse a string
some_xml_data = "<root>data</root>"

root = etree.fromstring(some_xml_data)  # returns an element object
print root.tag
print etree.tostring(root)

# using the xml() function parse a string
root = etree.XML("<root>data</root>")  # returns an element object
print root.tag
print etree.tostring(root)

# using the parse() function to parse from files and file like objects
some_file_like_object = BytesIO("<root>data</root>")
tree = etree.parse(some_file_like_object)  # returns an ElementTree object
print etree.tostring(tree)

#getting the root element object from the tree
root = tree.getroot()
print root.tag
print etree.tostring(root)
