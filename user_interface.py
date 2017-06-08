import readwrite
import time
import article_scraper

def main_ui():
    print("-----------------------------------------------------------------")
    while 1:
        print("This program scrapes coding horror website for articles.")
        print("Type !commands for list of commands.")
        try:
            a = input("> ")
        except:
            a = "invalid input"
        parsed = parse_input(a)
        if parsed == "exit":
            break
        print("\n")

def page_parser(page_string):
    pages = []
    for i in page_string.split():
        a = i.split("-")
        if len(a) == 2:
            if a[0].isdigit() and a[1].isdigit():
                for i in range(int(a[0]), int(a[1]) + 1):
                    pages.append(i)
            else:
                return False

def print_commands():
    #get pages
    print("get pages")
    print("  Gets articles from coding horror website on")
    print("  pages specified and prints to txt file")
    print("  Examples and Outputs:")
    print("    get pages 3-28")
    print("    Output: writes pages 3-28 into txt file")
    print("    get pages 3 9")
    print("    Output: writes pages 3 and 9 into txt file")
    print("    get pages")
    print("    Output: gets all pages and puts into txt file")
    #exit
    print("exit")
    print("  exits program")
    #!commands
    print("!commands")
    print("  Prints list of commands")
    
def parse_input(user_input):
    user_input = user_input.lower().split()
    if user_input[0] == "exit":
        print("")
        print("exiting now...")
        time.sleep(0.5)
        return "exit"
    elif user_input[0:2] == ["get", "pages"]:
        pages = "".join(user_input[2:])
        
        return "get pages"
    elif user_input[0] == "!commands":
        print_commands()
        return "!commands"
    else:
        print("invalid input, type !commands for list of commands")
        return "invalid input"

if __name__ == "__main__":
    main_ui()
