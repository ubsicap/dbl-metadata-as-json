def process_id_servers(dom, json_dict):
    id_server_objects = {}
    for id_server_dom in dom.xpath("idServer"):
        try:
            id_server_objects[id_server_dom.attrib["prefix"]] = id_server_dom.text
        except:
            pass
    json_dict["idServer"] = id_server_objects
