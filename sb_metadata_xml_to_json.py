#!/usr/bin/env python3

import os
import re
import sys
from as_json.metadata_as_json import MetadataAsJson

if len(sys.argv) != 3:
    raise Exception("Exactly 2 arguments required: from_dir and to_dir")
from_dir = os.path.abspath(sys.argv[1])
to_dir = os.path.abspath(sys.argv[2])
if not os.path.isdir(from_dir):
    raise Exception("from_dir '{0}' does not exist or is not a directory".format(from_dir))
if os.path.exists(to_dir) and not(os.path.isdir(to_dir)):
    raise Exception("to_dir '{0}' exists but is not a directory".format(to_dir))
for xml_path in os.listdir(from_dir):
    fq_xml_path = os.path.join(from_dir, xml_path)
    convertor_ob = MetadataAsJson(xml_path=fq_xml_path)
    fq_json_path = re.sub("\\.xml$", ".json", os.path.join(to_dir, xml_path))
    if not os.path.exists(to_dir):
        os.makedirs(to_dir)
    with open(fq_json_path, "w") as json_out:
        json_out.write(convertor_ob.json())
