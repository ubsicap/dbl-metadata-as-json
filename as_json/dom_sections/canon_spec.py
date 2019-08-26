def process_canon_spec(dom, json_dict):
    canon_specs = dom.xpath("canonSpec")
    if len(canon_specs) > 0:
        canon_spec = canon_specs[0]
        json_dict["canonSpec"] = {}
        if "type" in canon_spec.attrib:
            json_dict["canonSpec"]["type"] = str(canon_spec.attrib["type"])
        components = canon_spec.xpath("component")
        if len(components) > 0:
            json_dict["canonSpec"]["components"] = []
            for component in components:
                component_books = component.xpath("book")
                component_name = str(component.attrib["name"])
                component = {"name": component_name}
                if len(component_books) > 0:
                    component["books"] = []
                    for book in component_books:
                        if book.text:
                            component["books"].append(book.text)
                json_dict["canonSpec"]["components"].append(component)
