''' Insert heading comments here.'''


def open_file():
    '''Insert docstring here.'''
    pass  # insert your code here
    user_file = input("\nEnter filename: ")
    
    while True:
        try:
            fp = open(user_file, "r",encoding="utf-8")
            return fp 
            break
        except IOError:
            print("\nFile not found!")
            user_file = input("\nEnter filename: ")
              
def find_max(num, name, max_num, max_name):
    '''Insert docstring here.'''
    pass  # insert your code here
    
    if max_num > num:
        return max_num, max_name
    
    elif num >  max_num:
        return num, "\n\t{}".format(name)
        
    else:
        return max_num, "{}\n\t{}".format(max_name,name)
        
    
def find_min(num, name, min_num, min_name):
    
    '''Insert docstring here.'''
    pass  # insert your code here
    
    if num > min_num:
        return min_num, min_name

    elif min_num > num:
        return num, "\n\t{}".format(name)
        
    else:
        return min_num, "{}\n\t{}".format(min_name,name)

def read_file(data_fp):
    max_score = 0.0
    max_score_name = ""
    max_episodes = 0.0
    max_episode_name = ""
    min_score = float("inf")
    min_score_name = ""
    total_score = 0.0
    count = 0

    for line in data_fp:
        title = line[0:100].strip()
        score_str = line[100:105].strip()
        episodes_str = line[105:110].strip()

        if score_str != "N/A":
            score = float(score_str)
            total_score += score
            count += 1
            max_score, max_score_name = find_max(score, title, max_score, max_score_name)
            min_score, min_score_name = find_min(score, title, min_score, min_score_name)

        if episodes_str != "N/A":
            episodes = float(episodes_str)
            max_episodes, max_episode_name = find_max(episodes, title, max_episodes, max_episode_name)

    avg_score = round(total_score / count, 2) if count > 0 else 0.0
    return max_score, max_score_name, max_episodes, max_episode_name, min_score, min_score_name, avg_score
            
                
def search_anime(data_fp, anime_name):
    
    '''Insert docstring here.'''
    pass  # insert your code here
    count = 0
    empty_str = ""
    
    for line in data_fp:
        line = line.strip()
        title = line[0:100]
        release_season = line[110:122]
        
        if anime_name in line:
            count += 1
            empty_str += "\n\t{:100s}{:12s}".format(title,release_season)
            
    return count, empty_str 
    
    
            
def main():
    
    BANNER = "\nAnime-Planet.com Records" \
             "\nAnime data gathered in 2022"
    
    MENU ="Options" + \
          "\n\t1) Get max/min stats" + \
          "\n\t2) Search for an anime" + \
          "\n\t3) Stop the program!" + \
          "\n\tEnter option: "
    
    print(BANNER)
    
    
    while True:
        
        
        option = input(MENU)
        
        if option == "3":
            print("\nThank you using this program!")
            break
        
        while (option not in MENU) or (option.isalpha()):
            print("\nInvalid menu option!!! Please try again!")
            option = input(MENU)
            
        if option == "1":
            #prompt the user to open a specific anime file
            data_fp = open_file()
            
            #call the read_file function to get the values to returns and store them
            max_score,max_score_name, max_episode,max_episode_name,min_score,min_score_name,avg_score = read_file(data_fp)
            #close the file
            data_fp.close()
            
            print("\n\nAnime with the highest score of {:.2f}:".format(max_score))
            #print(f"{max_score:.2f}")
            print(max_score_name)
            
            print("\n\nAnime with the highest episode count of {:3,.0f}:".format(max_episode))
            #print(f"{max_episode:.0f}")
            print(max_episode_name)
            
            print("\n\nAnime with the lowest score of {:.2f}:".format(min_score))
            #print(f"{min_score:.2f}")
            print(min_score_name)
            
            print("\n\nAverage score for animes in file is {:.2f}".format(avg_score))
            #print(f"{avg_score:.2f}")
            
        elif option == "2":
              # Prompt user for file and search string
              
              data_fp = open_file()
              search_str = input("\nEnter anime name: ")
             
              # Search anime titles and display results
              
              num_of_titles, release_season = search_anime(data_fp, search_str)
              data_fp.close()
              
              if num_of_titles > 0: 
                  print("\nThere are {} anime titles with '{}'".format(num_of_titles,search_str))
                  print(release_season)
                  
              else:
                  print("\nNo anime with '{}' was found!".format(search_str))
              
              


# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    

"\nEnter filename: "
"\nFile not found!"
"\n\t{}"
"{}\n\t{}"
"\n\t{}{}"
"\n\nAnime with the highest score of {}:"
"\n\nAnime with the highest episode count of {}:"
"\n\nAnime with the lowest score of {}:"
"\n\nAverage score for animes in file is {}"
"\nEnter anime name: "
"\nNo anime with '{}' was found!"
"\nThere are {} anime titles with '{}'"
"\nInvalid menu option!!! Please try again!"
"\nThank you using this program!"




# def open_file():
#     while True:
#         filename = input("Enter file name: ")
#         try:
#             fp = open(filename, "r", encoding="utf-8")
#             return fp
#         except FileNotFoundError:
#             print("File not found! Please try again.")


# def find_max(value, name, max_value, max_name):
#     if value > max_value:
#         return value, "{}\n\t{}".format(name, value)
#     else:
#         return max_value, max_name


# def find_min(value, name, min_value, min_name):
#     if value < min_value:
#         return value, "{}\n\t{}".format(name, value)
#     else:
#         return min_value, min_name


# def read_file(data_fp):
#     max_score = 0.0
#     max_score_name = ""
#     max_episodes = 0.0
#     max_episode_name = ""
#     min_score = float("inf")
#     min_score_name = ""
#     total_score = 0.0
#     count = 0

#     for line in data_fp:
#         title = line[0:100].strip()
#         score_str = line[100:105].strip()
#         episodes_str = line[105:110].strip()

#         if score_str != "N/A":
#             score = float(score_str)
#             total_score += score
#             count += 1
#             max_score, max_score_name = find_max(score, title, max_score, max_score_name)
#             min_score, min_score_name = find_min(score, title, min_score, min_score_name)

#         if episodes_str != "N/A":
#             episodes = float(episodes_str)
#             max_episodes, max_episode_name = find_max(episodes, title, max_episodes, max_episode_name)

#     avg_score = round(total_score / count, 2) if count > 0 else 0.0

# return max_score, max_score_name, max_episodes, max_episode_name, min_score, min_score_name, avg_score


# def main():
#     option = ""
#     while option != "3":
#         print("\nOptions:\n1. Analyze anime data\n2. Search anime titles\n3. Exit program")
#         option = input("Enter your option: ")
        
#         if option == "1":
#             # Prompt user for file and read data
#             data_fp = open_file()
#             max_score, max_score_name, max_episodes, max_episode_name, min_score, min_score_name, avg_score = read_file(data_fp)
#             data_fp.close()
            
#             # Display results
#             print("\nHighest Score:")
#             print(f"{max_score:.2f}")
#             print(max_score_name)
            
#             print("\nHighest Episode Count:")
#             print(f"{max_episodes:.0f}")
#             print(max_episode_name)
            
#             print("\nLowest Score:")
#             print(f"{min_score:.2f}")
#             print(min_score_name)
            
#             print("\nAverage Score:")
#             print(f"{avg_score:.2f}")
            
        # elif option == "2":
        #     # Prompt user for file and search string
        #     data_fp = open_file()
        #     search_str = input("Enter search string: ")
            
        #     # Search anime titles and display results
        #     results = search_anime(data_fp, search_str)
        #     data_fp.close()
            
        #     print(f"\n{results[0]} titles found:")
        #     for the title, season in results[1]:
        #         print(f"{title} ({season})")
                
#         elif option != "3":
#             # Invalid option
#             print("Invalid option. Please try again.")

