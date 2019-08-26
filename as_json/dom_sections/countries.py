from lxml import etree
from .name_like_fields import process_name_like_field


def process_countries_section(dom, json_dict):
    countries_sections = dom.xpath("countries")
    if len(countries_sections) > 0:
        countries_section = countries_sections[0]
        json_dict["countries"] = []
        for country in countries_section.xpath("country"):
            country_record = {}
            for field in [
                "name"
                ]:
                field_elements = process_name_like_field(country, field)
                if len(field_elements) > 0:
                    country_record[field] = field_elements
                for field in [
                    "iso"
                ]:
                    field_nodes = country.xpath(field)
                    if len(field_nodes) > 0:
                        country_record[field]= str(field_nodes[0].text)
            json_dict["countries"].append(country_record)