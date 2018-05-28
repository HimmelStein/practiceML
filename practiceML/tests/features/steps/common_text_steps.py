from behave import given


@given('the text to be analyzed is')
@given('the following lines of text')
def step__given_text(context):
    context.original_lines = context.text
