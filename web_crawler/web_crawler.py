#Building web crawler from udacity CS 101

#library import recommended
def get_page(url):
    try:
        import urllib
        return urllib.urllibopen(url).read()
        except:
            return"
#get_next_target procedure returns the next quote and its end position
#it uses a string page as an input
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

def print_all_links(page):
    while get_next_target(page):
        url, endPos = get_next_target(page)
        if url:
            print url
            page = page[endPos:]
        else:
            break
  
#page = "webpage as string"

#test
print_all_links(get_page('http://xkcd.com/353/'))
