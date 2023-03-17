#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_revel_new import SourceRevelNew

if __name__ == "__main__":
    source = SourceRevelNew()
    launch(source, sys.argv[1:])
