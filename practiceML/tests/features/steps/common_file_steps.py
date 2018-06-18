import os
import practiceML

from behave import given

RAW_FOLDER = 'raw-text'
CLEAN_FOLDER = 'clean-text'

SAMPLES_PATH = os.path.join(os.path.dirname(practiceML.__file__), 'tests/samples/')


@given('we are working on samples in the folder "{folder}"')
def step__set_working_folder(context, folder):
    working_directory = os.path.join(SAMPLES_PATH, folder)
    context.directories = {"rawTxtDir": os.path.join(working_directory, RAW_FOLDER),
                           "cleanTxtDir": os.path.join(working_directory, CLEAN_FOLDER)}
