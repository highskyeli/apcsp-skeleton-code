from queue import Queue
import wikipediaapi
import time

user_agent = "MsOrret'sWikipediaGame/1.0 (orret.deborah@pusd.us)"

wiki_wiki = wikipediaapi.Wikipedia(user_agent, "en")

# HELPER FUNCTION: fetch_links(page) passes in a wikipedia page and returns a list of all the pages linked from that page
def fetch_links(page):
    links_list = []
    links = page.links
    for title in sorted(links.keys()):
        links_list.append(title)
        
    return links_list

#IN CLASS: Finish the definition of the wikipedia_game_solver using a Breadth-First-Search Traversal
def wikipedia_game_solver(start_page, target_page):
    print('Working on it...')
    start_time = time.time()
  
    visited = []
    queue = Queue()
    path = []

    queue.put(start_page.title)
    visited.append(start_page)
    queue.get()
    

    while not queue.empty():
        current_title = queue.get()
        if current_title == target_page.title:
            break

        current_page = wiki_wiki.page(current_title)
        next_level = fetch_links(current_page)
        visited.append(current_title)

        for node in next_level:
            if node not in visited:
                queue.put(node)
                parent[node] = current_title

    child = target_page.title
    while child != start_page.title:
        path.append(child)
        child = parent[child]
path.append(start_page.title)
path.reverse()

    
    # FINISH THE CODE HERE

    end_time = time.time()
    print("This algorithm took", end_time-start_time, "seconds to run!")
  
    return path

# Example usage:
start_page = wiki_wiki.page('Nina Tandon')
target_page = wiki_wiki.page('Italian language')
path = wikipedia_game_solver(start_page, target_page)
print("Shortest path:", path)

