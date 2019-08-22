def process_root_atts(dom, json_dict):
    """
    Process root attributes
    """
    if "schemaVersion" in dom.attrib:
        try:
            json_dict["schemaVersion"] = dom.attrib["schemaVersion"]
        except:
            json_dict["schemaVersion"] = None
