from .name_like_fields import process_name_like_field


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
                field_elements = process_name_like_field(agency, field)
                if len(field_elements) > 0:
                    agency_record[field] = field_elements
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
