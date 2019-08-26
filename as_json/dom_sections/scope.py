def process_scope(dom, json_dict):
    scope_sections = dom.xpath("scope")
    if len(scope_sections) > 0:
        json_dict["scope"] = []
        for book in scope_sections[0].xpath("bookScope"):
            if book.text:
                json_dict["scope"].append(book.text)
