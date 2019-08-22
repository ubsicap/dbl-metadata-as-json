from .name_like_fields import process_name_like_field


def process_names_section(dom, json_dict):
    names_sections = dom.xpath("names")
    if len(names_sections) > 0:
        names_section = names_sections[0]
        json_dict["names"] = {}
        for name_node in names_section.xpath("name"):
            try:
                name_id = name_node.attrib["id"]
            except:
                continue
            json_dict["names"][name_id] = {}
            for field in [
                "abbr",
                "short",
                "long"
            ]:
                field_object = process_name_like_field(name_node, field)
                if len(field_object) > 0:
                    json_dict["names"][name_id][field] = field_object
