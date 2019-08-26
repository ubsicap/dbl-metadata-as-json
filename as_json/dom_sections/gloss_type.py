def process_glossed_text_story_type(dom, json_dict):
    for string_field in [
        "storyVersion"
    ]:
        field_nodes = dom.xpath(string_field)
        if len(field_nodes) > 0:
            json_dict[string_field] = str(field_nodes[0].text)
    for bool_field in [
        "stopWords"
    ]:
        field_nodes = dom.xpath(bool_field)
        if len(field_nodes) > 0:
            json_dict[bool_field] = field_nodes[0].text == "true"
