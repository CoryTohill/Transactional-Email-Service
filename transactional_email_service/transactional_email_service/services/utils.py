from html.parser import HTMLParser


def convert_html_to_plain_text(html):
    """
     Convert an HTML string to plain text.

    Args:
        html (str): String of html to convert to plain text.

    Returns:
        str: Plain text verion of the html string.
    """
    class HTMLFilter(HTMLParser):
        text = ""
        def handle_data(self, data):
            self.text += data

    html_filter = HTMLFilter()
    html_filter.feed(html)
    return html_filter.text
