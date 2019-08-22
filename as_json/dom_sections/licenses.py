from .name_like_fields import process_name_like_field


def process_licenses_section(dom, json_dict):
    licenses_sections = dom.xpath("licenses")
    if len(licenses_sections) > 0:
        licenses_section = licenses_sections[0]
        json_dict["licenses"] = []
        non_license_elements = licenses_section.xpath("allRightsReserved|publicDomain")
        if len(non_license_elements) > 0:
            json_dict["licenses"].append({non_license_elements[0].tag: None})
        else:
            licenses_record = {}
            for license in licenses_section.xpath("license"):
                license_record = {}
                license_definitions = license.xpath("url|ingredient")
                if len(license_definitions) > 0:
                    license_record[license_definitions[0].tag] = license_definitions[0].text
                json_dict["licenses"].append(license_record)
