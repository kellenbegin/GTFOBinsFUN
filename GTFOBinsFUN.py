import requests
from bs4 import BeautifulSoup

# ANSI escape codes for colors
HEADER_COLOR = "\033[91m"  # Red
CODE_COLOR = "\033[92m"    # Green
TITLE_COLOR = "\033[95m"   # Purple
RESET_COLOR = "\033[0m"    # Reset to default color

# Prompt the user for input
user_input = input("Enter the name of the GTFO Bin you want to search (or 'all' to list all): ")

art = f'''
{CODE_COLOR}
   _____ _______ ______ ____  ____  _             ______ _    _ _   _ 
  / ____|__   __|  ____/ __ \|  _ \(_)           |  ____| |  | | \ | |
 | |  __   | |  | |__ | |  | | |_) |_ _ __  ___  | |__  | |  | |  \| |
 | | |_ |  | |  |  __|| |  | |  _ <| | '_ \/ __| |  __| | |  | | . ` |
 | |__| |  | |  | |   | |__| | |_) | | | | \__ \ | |    | |__| | |\  |
  \_____|  |_|  |_|    \____/|____/|_|_| |_|___/ |_|     \____/|_| \_|
                                                                      
{RESET_COLOR}
by Kellen Begin | KlusterFun
'''  
print(art)


# Base URL
base_url = "https://gtfobins.github.io/gtfobins/"

if user_input.lower() == "all":
    # Fetch the main page content
    response = requests.get("https://gtfobins.github.io/")
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all items labeled with class="bin-name"
        bin_names = soup.find_all("a", class_="bin-name")
        
        # Print the list of all binaries with alternating colors
        print(f"\n{TITLE_COLOR}List of all GTFOBins:{RESET_COLOR}\n" + "=" * 25)
        for i, bin_name in enumerate(bin_names):
            color = HEADER_COLOR if i % 2 == 0 else CODE_COLOR
            print(f"{color}- {bin_name.get_text().strip()}{RESET_COLOR}")
    else:
        print(f"Failed to fetch content. HTTP Status Code: {response.status_code}")
else:
    # Full URL
    full_url = f"{base_url}{user_input}"

    # Fetch the content of the specific GTFO bin
    response = requests.get(full_url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Print the GTFO bin title with user's input in purple
        print(f"{TITLE_COLOR}GTFOBin: {user_input}{RESET_COLOR}\n" + "=" * (len(user_input) + 10) + "\n")
        
        # Extract the main content
        content = soup.find('body')
        
        if content:
            # Extract headings (h2) and code (pre)
            for element in content.find_all(['h2', 'p', 'pre']):
                if element.name == 'h2':
                    print(f"\n{HEADER_COLOR}{element.get_text().strip()}{RESET_COLOR}\n" + "-" * len(element.get_text().strip()))
                elif element.name == 'pre':
                    print(f"\n{CODE_COLOR}{element.get_text().strip()}{RESET_COLOR}\n")
                else:
                    print(element.get_text().strip())
        else:
            print("No content found.")
    else:
        print(f"Failed to fetch content. HTTP Status Code: {response.status_code}")
