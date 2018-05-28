from behave import when, then


@when('search for words to be filtered')
def step_impl(context):
    raise NotImplementedError('STEP: When search for words to be filtered')


@then('we find "an", "auf", "das", "dass", "dem", "des", "diese", "eine"')
def step_impl(context):
    raise NotImplementedError('STEP: Then we find "an", "auf", "das", "dass", "dem", "des", "diese", "eine"')


@then('we find "einem", "mit", "sich", "sie", "so", "Wird", "wird"')
def step_impl(context):
    raise NotImplementedError('STEP: Then we find "einem", "mit", "sich", "sie", "so", "Wird", "wird"')


@when('we count the remaining words')
def step_impl(context):
    raise NotImplementedError('STEP: When we count the remaining words')


@then('we get the following frequencies')
def step_impl(context):
    raise NotImplementedError('STEP: Then we get the following frequencies')

