def process_snapshot_section(dom, json_dict):
    snapshot_sections = dom.xpath("snapshot")
    if len(snapshot_sections) > 0:
        snapshot_section = snapshot_sections[0]
        json_dict["snapshot"] = {}
        for whodunnit_element in snapshot_section.xpath("creation|uploading"):
            whodunnit_object = {}
            software_elements = whodunnit_element.xpath("software")
            if len(software_elements) > 0:
                whodunnit_object["software"] = software_elements[0].text
            user_elements = whodunnit_element.xpath("user")
            if len(user_elements) > 0:
                if user_elements[0].text:
                    whodunnit_object["user_name"] = user_elements[0].text
                if "id" in user_elements[0].attrib:
                    whodunnit_object["user_id"] = user_elements[0].attrib["id"]
            json_dict["snapshot"][whodunnit_element.tag] = whodunnit_object
        for field in [
            "comments"
        ]:
            field_nodes = snapshot_section.xpath(field)
            if len(field_nodes) > 0:
                json_dict["snapshot"][field] = str(field_nodes[0].text)
