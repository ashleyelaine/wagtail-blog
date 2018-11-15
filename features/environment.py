from splinter.browser import Browser


def before_all(context):
    context.browser = Browser('django')

    def parse_count(count):
        if count in ('a', 'an'):
            return 1
        else:
            return int(count)

    context.parse_count = parse_count


def after_all(context):
    context.browser.quit()
    context.browser = None
