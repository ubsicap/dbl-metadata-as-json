#!/usr/bin/env python3

import os
import pytest
import re
import sys
sys.path.append(os.path.join(__file__, "..", ".."))
from as_json.metadata_as_json import MetadataAsJson

@pytest.mark.parametrize(
    "xml_filename",
    [
        "scripture_text.xml",
        "scripture_audio.xml",
        "scripture_sign_language.xml",
        "scripture_print_pdf.xml"
    ]
)
def test_valid_xml_to_json(xml_filename):
    """
    Convert valid XML examples to JSON
    """
    md2j = MetadataAsJson(
        xml_path=os.path.abspath(
            os.path.join(
                __file__,
                "..",
                "..",
                "test",
                "xml_examples",
                xml_filename
            )
        )
    )
    print(md2j.json())
