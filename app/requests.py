import urllib.request,json
from flaskblog.models import Quote

# Base URL
base_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def get_quote():
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url.format()

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        displayed_quote = None

        if get_quote_response:
            quote = get_quote_response
            displayed_quote = process_results(quote)


    print(displayed_quote)
    return displayed_quote


def process_results(quote_list):

    '''
    Process quote
    '''
    final_quote = []

    quote = quote_list
    author = quote_list

    quote_component = Quote(quote, author)
    final_quote.append(quote_component.quote)
    return final_quote
