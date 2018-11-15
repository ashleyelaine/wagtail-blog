from behave import then


@then('print the page contents')
def print_the_page_contents(context):
    print(context.browser.html)  # noqa: T001


@then(u'fail')
def step_impl(context):
    raise Exception('I am intentionally failing')
