import lxml.etree as et

#sprawdzanie poprawności dokumentu xml
xml_file = et.parse("kraj.xml")
xml_validator = et.XMLSchema(file="kraj.xsd")
is_valid = xml_validator.validate(xml_file)
print(is_valid)
