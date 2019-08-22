import re
from lxml import etree

from .xhtml import xhtml2string

def process_copyright_section(dom, json_dict):
    copyright_sections = dom.xpath("copyright")
    if len(copyright_sections) > 0:
        copyright_section = copyright_sections[0]
        json_dict["copyright"] = []
        statement_elements = copyright_section.xpath("statement")
        if len(statement_elements) > 0:
            for statement_element in statement_elements:
                statement_object = {}
                if "type" in statement_element.attrib:
                    statement_object["type"] = statement_element.attrib["type"]
                if "format" in statement_element.attrib:
                    statement_object["format"] = statement_element.attrib["format"]
                if "lang" in statement_element.attrib:
                    statement_object["lang"] = statement_element.attrib["lang"]
                if statement_element.xpath("node()"):
                    if statement_element.xpath("*"):
                        statement_object["content"] = xhtml2string(statement_element)
                    else:
                        statement_object["content"] = statement_element.text
                json_dict["copyright"].append(statement_object)
