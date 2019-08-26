from .name_like_fields import process_name_like_field
from .countries import process_countries_section
from .canon_spec import process_canon_spec
from .structure import process_structure
from .scope import process_scope


def process_publications_section(dom, json_dict):
    publications_sections = dom.xpath("publications")
    if len(publications_sections) > 0:
        json_dict["publications"] = {}
        for publication in publications_sections[0].xpath("publication"):
            if "id" in publication.attrib:
                publication_id = publication.attrib["id"]
                json_dict["publications"][publication_id] = {}
                process_publication(publication, json_dict["publications"][publication_id])


def process_publication(dom, json_dict):
    if "default" in dom.attrib:
        json_dict["default"] = dom.attrib["default"] == "true"
    for field in [
        "name",
        "abbreviation",
        "description"]:
            field_elements = process_name_like_field(dom, field)
            if len(field_elements) > 0:
                json_dict[field] = field_elements
    process_canon_spec(dom, json_dict)
    process_scope(dom, json_dict)
    process_countries_section(dom, json_dict)
    process_structure(dom, json_dict)
