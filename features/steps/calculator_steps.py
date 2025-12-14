from behave import given, then, when


@given('numbers {a} and {b}')
def set_numbers(context, a, b):
    context.a = a
    context.b = b


@when('I submit "{operation}"')
def submit_operation(context, operation):
    context.response = context.client.post(
        "/",
        data={"a": context.a, "b": context.b, "op": operation},
        follow_redirects=True,
    )


@then('the result should be "{expected}"')
def check_result(context, expected):
    assert context.response is not None
    assert expected.encode() in context.response.data


@then('I should see an error message "{message}"')
def check_error(context, message):
    assert context.response is not None
    assert message.encode() in context.response.data
