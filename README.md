# Using upyter Notebook, BeautifulSoup, Pandas, Requests/Splinter, MongoDB,Flask 
Scraping data related to Mission to Mars and displaying the info in a single html page

There are 2 parts to this 

1. Scraping 

2. MongoDB and Flask Application



## Part  1: Scraping

Completed the initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Created a Jupyter Notebook file called `mission_to_mars.ipynb`. Used this file to complete all the scraping and analysis tasks. The following information outlines what to scrape.

### NASA Mars News
![image](https://user-images.githubusercontent.com/105729336/221997514-0b267e42-4c93-446c-816d-04a709f52ea7.png)


* Scraped the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assigned the text to variables that can be referenced later.


### JPL Mars Space Images—Featured Image
![image](https://user-images.githubusercontent.com/105729336/221997732-b8b139ea-4b8c-467b-b4a6-e980491b8f44.png)


* Visited the Featured Space Image site [here](https://spaceimages-mars.com).

* Used Splinter to navigate the site and find the image URL for the current Featured Mars Image, then assigned the URL string to a variable called `featured_image_url`.


### Mars Facts

* Visited the [Mars Facts webpage](https://galaxyfacts-mars.com) and use Pandas to scrape the table containing facts about the planet including diameter, mass, etc.

* Used Pandas to convert the data to a HTML table string.

### Mars Hemispheres
![image](https://user-images.githubusercontent.com/105729336/221997980-cc5e94c6-90f7-4ab3-b9c8-8d5d748cfbe3.png)

* Visited the [astrogeology site](https://marshemispheres.com/) to obtain high-resolution images for each hemisphere of Mars.

* Saved the image URL string for the full resolution hemisphere image and the hemisphere title containing the hemisphere name. Used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image URL string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.

## Part 2: MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above.

* Started by converting your Jupyter notebook into a Python script called `scrape_mars.py` by using a function called `scrape`. This function executed all the scraping code from above and return one Python dictionary containing all the scraped data.

* Next, created a route called `/scrape` that will import the `scrape_mars.py` script and call the `scrape` function.

  * Stored the return value in Mongo as a Python dictionary.

* Created a root route `/` that will query the Mongo database and pass the Mars data into an HTML template for displaying the data.

* Created a template HTML file called `index.html` that took the Mars data dictionary and displayed all the data in the appropriate HTML elements. 
