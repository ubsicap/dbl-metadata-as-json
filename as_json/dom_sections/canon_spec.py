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
                json_dict["canonSpec"]["components"] += [str(component.attrib["name"])]
