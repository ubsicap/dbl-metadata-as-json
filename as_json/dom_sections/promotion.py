import re
from lxml import etree

from .xhtml import xhtml2string

def process_promotion_section(dom, json_dict):
    promotion_sections = dom.xpath("promotion")
    if len(promotion_sections) > 0:
        promotion_section = promotion_sections[0]
        json_dict["promotion"] = []
        statement_elements = promotion_section.xpath("statement")
        if len(statement_elements) > 0:
            for statement_element in statement_elements:
                statement_object = {}
                if "format" in statement_element.attrib:
                    statement_object["format"] = statement_element.attrib["format"]
                if "lang" in statement_element.attrib:
                    statement_object["lang"] = statement_element.attrib["lang"]
                if statement_element.xpath("node()"):
                    if statement_element.xpath("*"):
                        statement_object["content"] = xhtml2string(statement_element)
                    else:
                        statement_object["content"] = statement_element.text
                json_dict["promotion"].append(statement_object)
