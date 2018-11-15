from behave import when, then, use_step_matcher

from six.moves.urllib.parse import urlparse
from splinter.exceptions import ElementDoesNotExist


FINDERS = ['css', 'xpath', 'tag', 'name', 'text', 'id', 'value']


@when('I go to the {page} page')
def i_go_to(context, page):
    url = context.url_from_page(page)
    context.browser.visit(url)


use_step_matcher('re')


@when('I click the "(?P<text>[^"]+)" (?:link|button)')
def i_click_the_button_or_link(context, text):
    for finder in FINDERS:
        try:
            if getattr(context.browser, 'is_element_present_by_%s' % finder)(text):
                getattr(context.browser, 'find_by_%s' % finder)(text).first.click()
                return
        except ElementDoesNotExist:
            continue

    raise Exception('Cannot find button or link %s' % text)


use_step_matcher('parse')


@when('I click the "{link_text}" link in the "{row_id}" row')
def i_click_the_x_link_in_the_y_row(context, link_text, row_id):
    context.browser \
        .find_by_xpath(
            '//td[text()="%s"]/parent::tr//a[text()="%s"]' % (row_id, link_text)
        ) \
        .first \
        .click()


@then('I should be redirected to the {page} page')
def i_should_be_redirected_to(context, page):
    expected_url = urlparse(context.url_from_page(page))
    current_url = urlparse(context.browser.url)
    context.test.assertEqual(expected_url.path, current_url.path)


use_step_matcher('re')


def _has_message(context, type_):
    return context.browser.is_element_present_by_css('.alert-%s' % type_)


@then('I should see an? (?P<type_>\w+) message')
def i_should_see_a_message(context, type_):
    context.test.assertTrue(_has_message(context, type_))


@then('I should not see an? (?P<type_>\w+) message')
def i_should_not_see_a_message(context, type_):
    context.test.assertFalse(_has_message(context, type_))


use_step_matcher('parse')


@then('I should be denied access')
def i_should_be_denied_access(context):
    context.test.assertEqual(403, context.browser.status_code)
