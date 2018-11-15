from behave import when, then


_MAIN_FORM = '#main-content form'


@when('I submit the form with the following values')
def i_submit_the_form_with_the_following_values(context, form=None):
    i_fill_in_the_form_with_the_following_values(context)
    i_submit_the_form(context)


@when('I fill in the form with the following values')
def i_fill_in_the_form_with_the_following_values(context, form=None):
    form = form if form else _MAIN_FORM
    for row in context.table:
        selector = '%s [name="%s"]' % (form, row['field'])
        context.browser.find_by_css(selector).first.fill(row['value'])


@when('I submit the form')
def i_submit_the_form(context, form=None):
    form = form if form else _MAIN_FORM
    selector = '%s button[type="submit"]' % form
    context.browser.find_by_css(selector).first.click()


@then('I should see an error message in the {field} field of the form')
def i_should_see_an_error_message_in_the_field_of_the_form(context, field):
    context.test.assertTrue(context.browser.is_element_present_by_css('form .has-error [name="%s"]' % field))


@then('I should see an error message in the form')
def i_should_see_an_error_message_in_the_form(context):
    context.test.assertTrue(context.browser.is_element_present_by_css('form .has-error'))
