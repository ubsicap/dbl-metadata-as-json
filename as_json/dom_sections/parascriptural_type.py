def process_parascriptural_word_alignment_type(dom, json_dict):
    for string_field in [
        "autoAlignerVersion"
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
    stemmer_sections = dom.xpath("stemmer")
    if len(stemmer_sections) > 0:
        json_dict["stemmer"] = {}
        for string_field in [
            "name",
            "version"
        ]:
            field_nodes = stemmer_sections[0].xpath(string_field)
            if len(field_nodes) > 0:
                json_dict["stemmer"][string_field] = str(field_nodes[0].text)
        for bool_field in [
            "affixes"
        ]:
            field_nodes = stemmer_sections[0].xpath(bool_field)
            if len(field_nodes) > 0:
                json_dict["stemmer"][bool_field] = field_nodes[0].text == "true"
    manual_sections = dom.xpath("manualAlignment")
    if len(manual_sections) > 0:
        json_dict["manualAlignment"] = {}
        for string_field in [
            "user"
        ]:
            field_nodes = manual_sections[0].xpath(string_field)
            if len(field_nodes) > 0:
                json_dict["manualAlignment"][string_field] = str(field_nodes[0].text)
        reference_sections = manual_sections[0].xpath("references")
        if len(reference_sections) > 0:
            json_dict["manualAlignment"]["reference"] = []
            for line_id in reference_sections[0].xpath("lineId"):
                line_starts = line_id.xpath("start")
                if len(line_starts) > 0:
                    line_ob = {"start": line_starts[0].text}
                    line_ends = line_id.xpath("end")
                    if len(line_ends) > 0:
                        line_ob["end"] = line_ends[0].text
                    json_dict["manualAlignment"]["reference"].append(line_ob)


