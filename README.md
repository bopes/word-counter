## Word Counter

App that displays the most commonly used words present for a given URL. Based on Real Python's 'Flask by Example' tutorial (available [here](https://realpython.com/blog/python/flask-by-example-part-1-project-setup/)).

#### Instructions

Submit a url via the form as a POST request. The url's webpage is scraped and the raw data is parsed to remove HTML and separate the page text into words. The frequency of each word is counted, and common words are eliminated. Each url and the counts for all and uncommon words are stored to a database. The id for this database  used to retrieve the uncommon words as a list, which is reduced to the ten most common. These ten words are returned as the result of the initial POST request. This process is handled as a Redis job to allow for better scaling at high request volume.

While the above process occurs, the submit button is disabled and a loading gif plays. When the process is complete, the button functionality is stored and the gif disappears. The top ten words are then displayed in a table view and in a bar graph displaying frequency. The visual elements are controlled by AngularJS and the bar graph is generated using D3.

#### Technology:
 * [Flask](http://flask.pocoo.org/) - Python microframework
 * [PostGreSQL](https://www.postgresql.org/) - Opensource SQL Database
 * [Redis](http://redis.io/) - In-memory data store
 * [AngularJS](https://angularjs.org/) - JavaScript MVW framework
 * [D3](https://d3js.org/) - Data visualization JavaScript library
 * [Beautiful Soup](https://pypi.python.org/pypi/beautifulsoup4) - Python package for web scraping
 * [Natural Language Toolkit](http://www.nltk.org/) - Python package for language parsing


