import os


from lxml import etree

def process_ingredients_section(dom, json_dict):
    ingredients_sections = dom.xpath("ingredients")
    if len(ingredients_sections) > 0:
        ingredients_section = ingredients_sections[0]
        json_dict["ingredients"] = {}
        for ingredient_element in ingredients_section.xpath("ingredient"):
            ingredient_paths = ingredient_element.xpath("path/text()")
            if len(ingredient_paths) > 0:
                ingredient_path = ingredient_paths[0]
                json_dict["ingredients"][ingredient_path] = {}
                for string_child in [
                    "checksum",
                    "mimeType",
                    "scopeOrRole"
                ]:
                    child_elements = ingredient_element.xpath(string_child)
                    if len(child_elements) > 0:
                        child_element = child_elements[0]
                        json_dict["ingredients"][ingredient_path][string_child] = str(child_element.text)
                for int_child in [
                    "size"
                ]:
                    child_elements = ingredient_element.xpath(int_child)
                    if len(child_elements) > 0:
                        child_element = child_elements[0]
                        try:
                            json_dict["ingredients"][ingredient_path][int_child] = int(child_element.text)
                        except:
                            pass
                for bool_child in [
                    "isSource"
                ]:
                    if bool_child in ingredient_element.attrib:
                        try:
                            json_dict["ingredients"][ingredient_path][bool_child] = ingredient_element.attrib[bool_child] == "true"
                        except:
                            pass
