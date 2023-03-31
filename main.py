#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_revel_n import SourceRevelN

if __name__ == "__main__":
    source = SourceRevelN()
    launch(source, sys.argv[1:])
