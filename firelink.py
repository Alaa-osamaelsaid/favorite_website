import webbrowser
#module that contains user's favorite websites
# Create a dict of sites
sites = {
 "facebook" :"https://www.facebook.com/",
 "instagram":"https://www.instagram.com/?hl=ar",
 "twitter" : "https://twitter.com/",
 "youtube" : "https://www.youtube.com/"
}
# Print the menu of sites
def print_menu():
 print("Please choose a site from the following list:")
 for x in sites:
  print(x)

# Get the user's choice
def get_choice():
 choice = input("Enter your choice: ")
 if choice in sites:
  return sites[choice]
 
#get used to open google chrome application
#open_new is used to open google (default webbrowser)
#webbrowser.open_new("https://google.com")
def firefox(link):
   webbrowser.open_new_tab(link)


