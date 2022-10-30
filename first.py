import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm')

for line in fhand:
    print(line.decode().strip())
