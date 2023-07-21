import re
import nltk.data

SEARCH_TERMS = [" table ", " sitting ", " seat ", " sit ", " sat "]

with open("cains_jawbone.txt", "r") as file:
    full_text = file.read()

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    # split text by pages
    pages = full_text.split("\n________________\n")

    # search through each page in Cain's jawbone looking for matches to the search term (case ignored)
    # when match is found, print the term matched, page number, and sentence term appears in
    page_index = 1
    for page in pages:
        for term in SEARCH_TERMS:
            matches_in_page = re.findall(term.lower(), page.lower())
            if len(matches_in_page) > 0:
                sentences = tokenizer.tokenize(page)
                for sentence in sentences:
                    matches_in_sentence = re.findall(term.lower(), sentence.lower())
                    if len(matches_in_sentence) > 0:
                        print("*",  "\"" + sentence + "\"", "(pg. " + str(page_index) + ")",)
        page_index += 1