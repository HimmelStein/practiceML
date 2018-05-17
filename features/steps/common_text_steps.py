from behave import given, when, then, step
from hamcrest import assert_that, equal_to, instance_of, is_

import os 
from io import StringIO

from practiceML.pre.extract_texts import without_hyphens
from practiceML.util.file_processing import derived_filename, process_file

import features._config as cfg


@given('the text to be analyzed is')
@given('the following lines of text')
def step__given_text(context):
    context.original_lines = context.text
