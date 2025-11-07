#!/usr/bin/env python3

import argparse
import tomllib

from sample import operations


# Parse command-line arguments
parser = argparse.ArgumentParser(
    description="Run a script in this sample project",
)
parser.add_argument("operation", choices=["add", "square"], help="Operation to perform")
parser.add_argument(
    "-p", "--parameters_path", required=True, help="Path to the parameters file to use"
)
cmd_line_args = parser.parse_args()

# Parse parameters
with open(cmd_line_args.parameters_path, "rb") as f:
    params = tomllib.load(f)

if cmd_line_args.operation == "add":
    print(operations.add(**params))

if cmd_line_args.operation == "square":
    raise Exception("Not implemented")
