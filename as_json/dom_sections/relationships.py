def process_relationships_section(dom, json_dict):
    relationships_sections = dom.xpath("relationships")
    if len(relationships_sections) > 0:
        relationship_section = relationships_sections[0]
        json_dict["relationships"] = []
        relation_nodes = relationship_section.xpath("relation")
        for relation_node in relation_nodes:
            if "id" in relation_node.attrib and "revision" in relation_node.attrib:
                relation_object = {}
                for att in [
                    "relationType",
                    "flavor",
                    "id",
                    "revision",
                    "publicationId"
                ]:
                    if att in relation_node.attrib:
                        relation_object[att] = str(relation_node.attrib[att])
            json_dict["relationships"].append(relation_object)
