from bs4 import BeautifulSoup

# Example HTML content with the anchor tag
html_content = '<a href="/?sa=X&amp;ved=0ahUKEwigxqGhpIqGAxWZqZUCHbcWBYUQOwgC"><span class="V6gwVd">G</span><span class="iWkuvd">o</span><span class="cDrQ7">o</span><span class="V6gwVd">g</span><span class="ntlR9">l</span><span class="iWkuvd tJ3Myc">e</span></a>'

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the anchor tag
anchor_tag = soup.find('a')

# Extract the value of the href attribute
href_value = anchor_tag.get('href')

print(href_value)
