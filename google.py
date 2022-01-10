from googleapi import google
num_page = 3
search_results = google.search("koala bears")
print(len(search_results))

