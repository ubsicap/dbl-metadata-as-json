#!/usr/bin/env python3

import os
import pytest
import re
import sys
sys.path.append(os.path.join(__file__, "..", ".."))
from as_json.metadata_as_json import MetadataAsJson


def test_valid_xml_to_json():
    """
    Convert valid XML examples to JSON
    """
    md2j = MetadataAsJson(xml_path=os.path.abspath(os.path.join(__file__, "..", "..", "test", "xml_examples", "scripture_text.xml")))
    print(md2j.json())
