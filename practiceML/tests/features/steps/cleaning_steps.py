from behave import given, when, then
from hamcrest import assert_that, equal_to, instance_of, is_, contains_string, not_

import os
from io import StringIO

from practiceML.pre.extract_texts import without_hyphens
from practiceML.util.file_processing import derived_filename, process_file


def text_as_in_memory_file(text):
    in_memory_file = StringIO()
    for line in text.splitlines():
        in_memory_file.write(line + '\n')
    in_memory_file.seek(0)
    return in_memory_file


@when('the system cleans this text')
def step__clean_the_text(context):
    file = text_as_in_memory_file(context.original_lines)
    context.cleaned_lines = without_hyphens(file)


@then('they become one string')
def step__check_the_result_is_a_string(context):
    assert_that(context.cleaned_lines, instance_of(str))


@then('the lines stay unchanged')
def step__check_that_cleaned_and_original_lines_are_equal(context):
    assert_that(context.cleaned_lines.splitlines(), equal_to(context.original_lines.splitlines()))


@then('the text consists of the following lines')
def step__check_that_cleaned_lines_are_as_given(context):
    assert_that(context.cleaned_lines.splitlines(), equal_to(context.text.splitlines()))


@given('a text file named "{filename}"')
def step__given_a_text_file(context, filename):
    source_name = os.path.join(context.directories["rawTxtDir"], filename)
    context.filename = filename
    context.source_name = source_name
    assert_that(os.path.isfile(source_name), is_(True))


@given('a corresponding oracle file')
def step__given_an_test_oracle(context):
    filename = derived_filename(context.filename, 'cln_', '.expected.txt')
    oracle_name = os.path.join(context.directories["cleanTxtDir"], filename)
    context.oracle_name = oracle_name
    assert_that(os.path.isfile(oracle_name), is_(True))


@when('we create a cleaned file')
def step__create_a_cleaned_file(context):
    filename = derived_filename(context.filename, 'cln_', '.actual.txt')
    target_name = os.path.join(context.directories["cleanTxtDir"], filename)
    context.target_name = target_name
    process_file(context.source_name, target_name, without_hyphens)


@then('the cleaned file exists')
def step__check_the_cleaned_file_exists(context):
    assert_that(os.path.isfile(context.target_name), is_(True))


@then('contains the same as the oracle file')
def step__check_cleaned_file_and_oracle_file_contain_the_same(context):
    with open(context.target_name) as target, open(context.oracle_name) as oracle:
        for actual, expected in zip(target, oracle):
            assert_that(actual, equal_to(expected))


@then('the text contains "{word}"')
def step__result_contains_word(context, word):
    assert_that(context.cleaned_lines, contains_string(word))


@step('the text does not contain "{word}"')
def step__result_does_not_contain_word(context, word):
    assert_that(context.cleaned_lines, not_(contains_string(word)))
