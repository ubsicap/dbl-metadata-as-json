def process_scripture_text_type(dom, json_dict):
    for string_field in [
        "projectType",
        "translationType",
        "audience",
        "usfmVersion"
    ]:
        field_nodes = dom.xpath(string_field)
        if len(field_nodes) > 0:
            json_dict[string_field] = str(field_nodes[0].text)


def process_scripture_audio_type(dom, json_dict):
    for string_field in [
        "dramatization"
    ]:
        field_nodes = dom.xpath(string_field)
        if len(field_nodes) > 0:
            json_dict[string_field] = str(field_nodes[0].text)
    for stream_section in dom.xpath("source|production"):
        stream_type = stream_section.tag
        json_dict[stream_type] = {}
        for string_field in [
            "compression",
            "trackConfiguration",
            "timingDir"
        ]:
            field_nodes = stream_section.xpath(string_field)
            if len(field_nodes) > 0:
                json_dict[stream_type][string_field] = str(field_nodes[0].text)
        for integer_field in [
            "bitRate",
            "bitDepth",
            "samplingRate"
        ]:
            field_nodes = stream_section.xpath(integer_field)
            if len(field_nodes) > 0:
                try:
                    json_dict[stream_type][integer_field] = int(field_nodes[0].text)
                except:
                    pass


def process_scripture_sign_language_type(dom, json_dict):
    for string_field in [
        "translationType",
        "audience",
        "timingDir",
        "container"
    ]:
        field_nodes = dom.xpath(string_field)
        if len(field_nodes) > 0:
            json_dict[string_field] = str(field_nodes[0].text)
    for stream_section in dom.xpath("videoStream|audioStream|subtitleStream"):
        stream_type = stream_section.tag
        json_dict[stream_type] = {}
        for string_field in [
            "compression",
            "trackConfiguration",
            "codec",
            "screenResolution"
        ]:
            field_nodes = stream_section.xpath(string_field)
            if len(field_nodes) > 0:
                json_dict[stream_type][string_field] = str(field_nodes[0].text)
        for integer_field in [
            "bitRate",
            "bitDepth",
            "samplingRate"
        ]:
            field_nodes = stream_section.xpath(integer_field)
            if len(field_nodes) > 0:
                try:
                    json_dict[stream_type][integer_field] = int(field_nodes[0].text)
                except:
                    pass
        for float_field in [
            "frameRate"
        ]:
            field_nodes = stream_section.xpath(float_field)
            if len(field_nodes) > 0:
                try:
                    json_dict[stream_type][float_field] = float(field_nodes[0].text)
                except:
                    pass



def process_scripture_print_type(dom, json_dict):
    for string_field in [
        "contentType",
        "pod",
        "width",
        "height",
        "scale",
        "orientation",
        "color"
    ]:
        field_nodes = dom.xpath(string_field)
        if len(field_nodes) > 0:
            json_dict[string_field] = str(field_nodes[0].text)
    for integer_field in [
        "pageCount"
    ]:
        field_nodes = dom.xpath(integer_field)
        if len(field_nodes) > 0:
            try:
                json_dict[integer_field] = int(field_nodes[0].text)
            except:
                pass
    for bool_field in [
        "pod"
    ]:
        field_nodes = dom.xpath(bool_field)
        if len(field_nodes) > 0:
            try:
                json_dict[bool_field] = field_nodes[0].text == "true"
            except:
                pass
    edge_space_sections = dom.xpath("edgeSpace")
    if len(edge_space_sections) > 0:
        json_dict["edgeSpace"] = {}
        for string_field in [
            "top",
            "bottom",
            "inside",
            "outside"
        ]:
            field_nodes = edge_space_sections[0].xpath(string_field)
            if len(field_nodes) > 0:
                json_dict["edgeSpace"][string_field] = str(field_nodes[0].text)
    thumbnail_sections = dom.xpath("thumbnail")
    if len(thumbnail_sections) > 0:
        json_dict["thumbnail"] = {}
        for string_field in [
            "color"
        ]:
            field_nodes = thumbnail_sections[0].xpath(string_field)
            if len(field_nodes) > 0:
                json_dict["thumbnail"][string_field] = str(field_nodes[0].text)
        for integer_field in [
            "width",
            "height"
        ]:
            field_nodes = thumbnail_sections[0].xpath(integer_field)
            if len(field_nodes) > 0:
                try:
                    json_dict["thumbnail"][integer_field] = int(field_nodes[0].text)
                except:
                    pass
    fonts_sections = dom.xpath("fonts")
    if len(fonts_sections) > 0:
        json_dict["fonts"] = {}
        for font in fonts_sections[0]:
            try:
                font_name = font.text
                font_type = font.attrib["type"]
                json_dict["fonts"][font_name] = font_type
            except:
                pass


def process_scripture_braille_type(dom, json_dict):
    for bool_field in [
        "isContracted"
    ]:
        field_nodes = dom.xpath(bool_field)
        if len(field_nodes) > 0:
            json_dict[bool_field] = field_nodes[0].text == "true"
    process_braille_convertor(dom, json_dict)
    process_hyphenation_dictionary_convertor(dom, json_dict)
    process_continuous_poetry_convertor(dom, json_dict)
    process_braille_number_sign(dom, json_dict)
    process_braille_content(dom, json_dict)
    process_braille_page(dom, json_dict)


def process_braille_convertor(dom, json_dict):
    pass

def process_hyphenation_dictionary_convertor(dom, json_dict):
    pass

def process_continuous_poetry_convertor(dom, json_dict):
    pass

def process_braille_number_sign(dom, json_dict):
    pass

def process_braille_content(dom, json_dict):
    pass

def process_braille_page(dom, json_dict):
    pass
