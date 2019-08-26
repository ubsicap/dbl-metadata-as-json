from .canon_spec import process_canon_spec
from .scope import process_scope
from .scripture_type import *
from .gloss_type import *
from .parascriptural_type import *
from .peripheral_type import *


def process_type_section(dom, json_dict):
    type_sections = dom.xpath("type")
    if len(type_sections) > 0:
        type_section = type_sections[0]
        json_dict["type"] = {}
        for string_field in [
            "flavor",
            "flavorType"
        ]:
            field_nodes = type_section.xpath(string_field)
            if len(field_nodes) > 0:
                json_dict["type"][string_field] = str(field_nodes[0].text)
        process_scope(type_section, json_dict["type"])
        confidentiality_sections = type_section.xpath("confidentiality")
        if len(confidentiality_sections) > 0:
            json_dict["type"]["confidentiality"] = {}
            for string_field in [
                "metadata",
                "source",
                "publications"
            ]:
                field_nodes = confidentiality_sections[0].xpath(string_field)
                if len(field_nodes) > 0:
                    json_dict["type"]["confidentiality"][string_field] = str(field_nodes[0].text)

        process_canon_spec(type_section, json_dict["type"])
        process_conventions(type_section, json_dict["type"])
        flavor_details_sections = type_section.xpath("flavorDetails")
        if len(flavor_details_sections) > 0:
            json_dict["type"]["flavorDetails"] = {}
            if "flavor" in json_dict["type"] and "flavorType" in json_dict["type"]:
                if json_dict["type"]["flavor"][:2] == "x-":
                    process_x_type(
                        flavor_details_sections[0],
                        json_dict["type"]["flavorDetails"]
                    )
                elif json_dict["type"]["flavorType"] in flavor_detail_processors and\
                    json_dict["type"]["flavor"] in flavor_detail_processors[json_dict["type"]["flavorType"]]:
                    flavor_detail_processors[json_dict["type"]["flavorType"]][json_dict["type"]["flavor"]](
                        flavor_details_sections[0],
                        json_dict["type"]["flavorDetails"]
                    )


def process_conventions(dom, json_dict):
    conventions_sections = dom.xpath("conventions")
    if len(conventions_sections) > 0:
        json_dict["conventions"] = {}
        for convention in conventions_sections[0].xpath("convention"):
            try:
                convention_version = convention.attrib["version"]
                convention_name = convention.text
                json_dict["conventions"][convention_name] = convention_version
            except:
                pass


def process_x_type(dom, json_dict):
    for child in dom.xpath("*"):
        if child.tag not in ["flavor", "flavorType", "scope", "confidentiality", "canonSpec", "conventions"]:
            json_dict[child.tag] = {}
            process_x_type1(child, json_dict[child.tag])


def process_x_type1(dom, json_dict):
    if len(dom.attrib) > 0:
        json_dict["attributes"] = {k: v for k, v in dom.attrib.items()}
    children = dom.xpath("*")
    if len(children) > 0:
        json_dict["children"] = {}
        for child in children:
            json_dict["children"][child.tag] = {}
            process_x_type1(child, json_dict["children"][child.tag])
    if dom.text:
        json_dict["text"] = dom.text


flavor_detail_processors = {
    "scripture" : {
        "scriptureText": process_scripture_text_type,
        "scriptureAudio": process_scripture_audio_type,
        "scriptureSignLanguageVideo": process_scripture_sign_language_type,
        "scripturePrint": process_scripture_print_type,
        "scriptureBraille": process_scripture_braille_type
    },
    "gloss": {
        "glossedTextStory": process_glossed_text_story_type
    },
    "parascriptural": {
        "parascripturalWordAlignment": process_parascriptural_word_alignment_type
    },
    "peripheral": {
        "peripheralVersification": process_peripheral_versification_type
    }
}
