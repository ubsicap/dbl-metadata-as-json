from .name_like_fields import process_name_like_field


def process_languages_section(dom, json_dict):
    languages_sections = dom.xpath("languages")
    if len(languages_sections) > 0:
        json_dict["languages"] = []
        for language_section in languages_sections[0].xpath("language"):
            language_object = {}
            for field in [
                "name"
                ]:
                field_elements = process_name_like_field(language_section, field)
                if len(field_elements) > 0:
                    language_object[field] = field_elements
            for field in [
                "bcp47",
                "rod",
                "scriptDirection"
            ]:
                field_nodes = language_section.xpath(field)
                if len(field_nodes) > 0:
                    language_object[field] = str(field_nodes[0].text)
            json_dict["languages"].append(language_object)
