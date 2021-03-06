from .name_like_fields import process_name_like_field

def process_identification_section(dom, json_dict):
    identification_sections = dom.xpath("identification")
    if len(identification_sections) > 0:
        identification_section = identification_sections[0]
        json_dict["identification"] = {}
        for field in [
            "name",
            "abbreviation",
            "description"]:
                field_elements = process_name_like_field(identification_section, field)
                if len(field_elements) > 0:
                    json_dict["identification"][field] = field_elements
        for field in [
            'dateStarted',
            'dateCompleted'
        ]:
            field_nodes = identification_section.xpath(field)
            if len(field_nodes) > 0:
                json_dict["identification"][field] = field_nodes[0].text
        system_id_elements = identification_section.xpath("systemId")
        if len(system_id_elements) > 0:
            system_id_objects = {}
            for system_id_element in system_id_elements:
                try:
                    prefix, _ = system_id_element.text.split("::")
                    system_id_objects[prefix] = {
                        "id": system_id_element.text
                    }
                    if "revision" in system_id_element.attrib:
                        system_id_objects[prefix]["revision"] = system_id_element.attrib["revision"]
                except:
                    pass
            json_dict["identification"]["systemId"] = system_id_objects
