import wikipedia as wk
import pandas as pd

# Search Wikipedia Page
print(wk.search("Indian Institute of Technology Madras"))


# Search Top Two Result
print(wk.search("Indian Institute of Technology Madras",results=2))


# Summary Of Wikipedia Page
print(wk.summary("Indian Institute of Technology Madras"))


# Summary Of Wikipedia Page in Two Sentences
print(wk.summary("Indian Institute of Technology Madras",sentences=2))


# Create Full Wikipedia Page Instance
full_page = wk.page("Indian Institute of Technology Madras")


# Return Full Wikipedia Page
print(full_page.content)


# Return Wikipedia Search Page URL
print(full_page.url)


# Return Wikipedia Search Page References
print(full_page.references)


# Return Wikipedia Search Page Title
print(full_page.title)


# Return Full Page Image URL
print(full_page.images)


# Return Wikipedia Search Page First Image URL
print(full_page.images[0])


# Return Wikipedia Search Page HTML Table
html = wk.page("Indian Institute of Technology Madras").html().encode("UTF-8")
df = pd.read_html(html)
print(df)