# Dependencies
import pandas as pd
# import pymongo
from bs4 import BeautifulSoup
#import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

# Main web scraping  
def scrape_all():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)
    date, title, paragraph = scrape_mars_news(browser)
    img_url = scrape_mars_image(browser)
    facts = scrape_mars_facts()
    hemisphere_image_urls = scrape_mars_hemispheres(browser)
    
    data = {
        "news": title,
        "paragraph": paragraph,
        "date": date,
        "featured_image": img_url,
        "facts": facts,
        "hemispheres":hemisphere_image_urls
        # "hemispheres_title": hemisphere_image_urls.hemi_title,
        # "hemispheres_url": hemisphere_image_urls.hemi_img_url,

        }
    browser.quit()
    return data 

def scrape_mars_news(browser):
    
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # ### NASA Mars News
    # Examine the results, then determine element that contains sought info
    # results are returned as an iterable list
    results = soup.find_all('div', class_='list_text')
    # results
    # Loop through returned results
    for result in results:
        
        # Error handling
        try:
            # Identify and return title of listing
            date = result.find('div', class_='list_date').text
            title = result.find('div', class_='content_title').text
            # Identify and return the explanation of the listing
            paragraph = result.find('div', class_='article_teaser_body').text
                               
        except:       
                print('Data not found')

    
    return date,title,paragraph


# ### JPL Mars Space Images—Featured Image
def scrape_mars_image(browser):

    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    # HTML Object 
    html_image = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_image, 'html.parser')

    relative_image_path = soup.find_all('img')[1]["src"]

    featured_image_url = url + relative_image_path
    return featured_image_url

# ### Mars Facts
def scrape_mars_facts():
    url = 'https://galaxyfacts-mars.com'
    tables = pd.read_html(url)
    tables

    type(tables)
    table_df = tables[0]
    table_df 

    # Drop the earth data from the dataframe
    table_df = table_df.drop([2], axis=1)
    table_df = table_df.iloc[1: , :]
    table_df.columns=['Description', 'Values']
    table_df.set_index('Description', inplace=True)
    table_df

    # Convert the table back to HTML
    html_table = table_df.to_html()
    html_table = html_table.replace('\n','')
    html_table
    return html_table

# ### Mars Hemispheres
def scrape_mars_hemispheres(browser):
    
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # Get a List of All the Hemispheres
    # HTML Object
    html_hemispheres = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_hemispheres, 'html.parser')

    # Retreive all items that contain mars hemispheres information
    items = soup.find_all('div', class_='item')

    # Create empty list for hemisphere urls 
    hemisphere_image_urls = []

    # Store the main_ul 
    hemispheres_main_url = 'https://marshemispheres.com/'

    # Loop through the items previously stored
    for i in items: 
        # Store title
        hemi_title = i.find('h3').text
        
        # Store link that leads to full image website
        partial_img_url = i.find('a', class_='itemLink product-item')['href']
        
        # Visit the link that contains the full image website 
        browser.visit(hemispheres_main_url + partial_img_url)
        
        # HTML Object of individual hemisphere information website 
        partial_img_html = browser.html
        
        # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = BeautifulSoup( partial_img_html, 'html.parser')
        
        # Retrieve full image source 
    
        hemi_img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
        
        # Append the retreived information into a list of dictionaries 
        hemisphere_image_urls.append({"title" : hemi_title, "img_url" : hemi_img_url})
        

    return hemisphere_image_urls




if __name__ == "__main__":
    print(scrape_all())