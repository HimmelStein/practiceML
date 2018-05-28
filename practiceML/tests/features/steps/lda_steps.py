from behave import given, when, then
from hamcrest import assert_that, equal_to, instance_of, is_

from practiceML.core.lda import get_content_words


@given('the sentence "{sentence}"')
def step__given_a_sentence(context, sentence):
    context.original_sentence = sentence

@when('we extract the content words')
def step__extract_content_words(context):
    context.extracted_words = get_content_words(context.original_sentence)

@then('we get "{expected}"')
def step__verify_result(context, expected):
    assert_that(context.extracted_words, equal_to(expected))
