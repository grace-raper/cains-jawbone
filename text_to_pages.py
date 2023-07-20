# Cain's Jawbone word frequency research
PATH_FOR_PAGES = "./page_notes/"

# read in full text file
with open("cains_jawbone.txt", "r") as file:
    full_text = file.read()

    # split text by pages
    pages = full_text.split("\n________________\n")

    pnum = 1
    for page in pages:
        # use the page number to create the markdown file name
        filename = PATH_FOR_PAGES + str(pnum).zfill(3) + ".md"

        # open the markdown file and write the page content as while as spots for notes
        with open(filename, 'w') as f:
            f.write("| Previous Page | Next Page | Narrator | Victim | Date | Location |\n")
            f.write("|:--------------|:---------:|---------:|-------:|-----:|---------:|\n")
            f.write("|               |           |          |        |      |          |\n\n")
            f.write("# Passage\n")
            f.write(">" + page + "\n")
            f.write("# Connected Pages\n")
            f.write("# Clues\n")
            f.write("# Cross-References\n")

        pnum += 1