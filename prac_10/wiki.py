"""
CP1404/CP5632 Practical
Wikipedia API with exception handling
"""

import wikipedia


def main():
    page_title = input("Enter page title: ")

    while page_title != "":
        try:
            page = wikipedia.page(page_title, auto_suggest=False)
            print(page.title)
            print(page.summary)
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as error:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(error.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{page_title}" does not match any pages. Try another id!')
        print()
        page_title = input("Enter page title: ")

    print("Thank you.")


if __name__ == "__main__":
    main()
