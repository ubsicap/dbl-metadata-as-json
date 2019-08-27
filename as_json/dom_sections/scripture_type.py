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
    convertor_sections = dom.xpath("brailleConvertor")
    if len(convertor_sections) > 0:
        json_dict["brailleConvertor"] = {}
        for string_field in [
            "version"
        ]:
            field_nodes = convertor_sections[0].xpath(string_field)
            if len(field_nodes) > 0:
                json_dict["brailleConvertor"][string_field] = str(field_nodes[0].text)
        table_sections = convertor_sections[0].xpath("table")
        if len(table_sections) > 0:
            json_dict["brailleConvertor"]["table"] = {}
            for string_field in [
                "src",
                "name"
            ]:
                field_nodes = table_sections[0].xpath(string_field)
                if len(field_nodes) > 0:
                    json_dict["brailleConvertor"]["table"][string_field] = str(field_nodes[0].text)


def process_hyphenation_dictionary_convertor(dom, json_dict):
    hyphenation_sections = dom.xpath("hyphenationDictionary")
    if len(hyphenation_sections) > 0:
        json_dict["hyphenationDictionary"] = {}
        if "src" in hyphenation_sections[0].attrib:
            json_dict["hyphenationDictionary"]["src"] = hyphenation_sections[0].attrib["src"]
        for string_field in [
            "name"
        ]:
            field_nodes = hyphenation_sections[0].xpath(string_field)
            if len(field_nodes) > 0:
                json_dict["hyphenationDictionary"][string_field] = str(field_nodes[0].text)


def process_continuous_poetry_convertor(dom, json_dict):
    poetry_sections = dom.xpath("continuousPoetry")
    if len(poetry_sections) > 0:
        json_dict["continuousPoetry"] = {}
        for string_field in [
            "startIndicator",
            "lineIndicator",
            "lineIndicatorSpaced",
            "endIndicator"
        ]:
            field_nodes = poetry_sections[0].xpath(string_field)
            if len(field_nodes) > 0:
                json_dict["continuousPoetry"][string_field] = str(field_nodes[0].text)


def process_braille_number_sign(dom, json_dict):
    sign_sections = dom.xpath("numberSign")
    if len(sign_sections) > 0:
        json_dict["numberSign"] = {}
        for string_field in [
            "character"
        ]:
            field_nodes = sign_sections[0].xpath(string_field)
            if len(field_nodes) > 0:
                json_dict["numberSign"][string_field] = str(field_nodes[0].text)
        for bool_field in [
            "useInMargin"
        ]:
            field_nodes = sign_sections[0].xpath(bool_field)
            if len(field_nodes) > 0:
                json_dict["numberSign"][bool_field] = field_nodes[0].text == "true"


def process_braille_content(dom, json_dict):
    content_sections = dom.xpath("content")
    if len(content_sections) > 0:
        json_dict["content"] = {}
        for string_field in [
            "chapterNumberStyle",
            "verseSeparator"
        ]:
            field_nodes = content_sections[0].xpath(string_field)
            if len(field_nodes) > 0:
                json_dict["content"][string_field] = str(field_nodes[0].text)
        for bool_field in [
            "chapterHeadingsNumberFirst",
            "includeIntros"
        ]:
            field_nodes = content_sections[0].xpath(bool_field)
            if len(field_nodes) > 0:
                json_dict["content"][bool_field] = field_nodes[0].text == "true"
        versed_sections = content_sections[0].xpath("versedParagraphs")
        if len(versed_sections) > 0:
            json_dict["versedParagraphs"] = []
            for versed_book in versed_sections[0].xpath("book"):
                try:
                    json_dict["versedParagraphs"].append(versed_book.text)
                except:
                    pass
        for extra_section in content_sections[0].xpath("footnotes|crossReferences|characterStyles"):
            json_dict["content"][extra_section.tag] = {}
            for string_field in [
                "callerSymbol",
                "emphasizedWord",
                "emphasizedPassageStart",
                "emphasizedPassageEnd"
            ]:
                field_nodes = extra_section.xpath(string_field)
                if len(field_nodes) > 0:
                    json_dict["content"][extra_section.tag][string_field] = str(field_nodes[0].text)
            

def process_braille_page(dom, json_dict):
    page_sections = dom.xpath("page")
    if len(page_sections) > 0:
        json_dict["page"] = {}
        for integer_field in [
            "charsPerLine",
            "linesPerPage",
            "defaultMarginWidth",
            "carryLines"
        ]:
            field_nodes = page_sections[0].xpath(integer_field)
            if len(field_nodes) > 0:
                try:
                    json_dict["page"][integer_field] = int(field_nodes[0].text)
                except:
                    pass
        for bool_field in [
            "versoLastLineBlank"
        ]:
            field_nodes = page_sections[0].xpath(bool_field)
            if len(field_nodes) > 0:
                json_dict["page"][bool_field] = field_nodes[0].text == "true"
