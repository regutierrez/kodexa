#!/usr/bin/env bash


conda activate kodexa
datamodel-codegen --input kodexa-swagger.json --input-file-type jsonschema --output kodexa_cloud/model.py --target-python-version 3.6