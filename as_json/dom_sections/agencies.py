def process_agencies_section(dom, json_dict):
    agencies_sections = dom.xpath("agencies")
    if len(agencies_sections) > 0:
        agencies_section = agencies_sections[0]
        json_dict["agencies"] = []
        for agency in agencies_section:
            agency_record = {}
            for field in [
                "name"
                ]:
                list_elements = agency.xpath(field)
                if len(list_elements) > 0:
                    element_objects = {}
                    for element in list_elements:
                        try:
                            element_objects[element.attrib["lang"]] = element.text
                        except:
                            pass
                    agency_record[field] = element_objects
            for text_child in [
                "isRightsHolder",
                "id",
                "abbr",
                "url"
            ]:
                child_nodes = agency.xpath(text_child)
                if len(child_nodes) > 0:
                    agency_record[text_child] = child_nodes[0].text
            contribute_nodes = agency.xpath("contributes")
            if len(contribute_nodes) > 0:
                 for bool_child in [
                    "content",
                    "publication",
                    "management",
                    "finance",
                    "qa"
                ]:
                    child_nodes = contribute_nodes[0].xpath(bool_child)
                    if len(child_nodes) > 0:
                        bool_value = child_nodes[0].text == "true"
                        agency_record["contributes_{0}".format(bool_child)] = bool_value
            if agency.tag == "administrator":
                agency_record["isAdministrator"] = True
            json_dict["agencies"] += [agency_record]
