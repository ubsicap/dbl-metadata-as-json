def process_name_like_field(dom, field):
    elements = dom.xpath(field)
    element_objects = {}
    for element in elements:
        try:
            element_objects[element.attrib["lang"]] = element.text
        except:
            pass
    return element_objects

