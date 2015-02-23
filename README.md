cs851-s15
=========

Shared repository for ODU CS 751 / 851 Spring 2015

Assignment 1 Code Details :-

1) Tweets Colector :-
tweets-collector/tweets.py

It collects tweet from Twitter api dumps it into a mongodb.

2) Url Extracter :-
tweets-to-url/tweets_to_url.py

It checks for url's in Tweet and save it in the mongodb. Also 301 redirect url's are also collected in this program using requests api.

3) Carbon Dating :-

tweets-carbon-dating/carbon_date/tweets-carbon-dating.py

It gets the estimated_creation date for the url using the Carbon Dating library.

4) Data Files for drawing histogram and also calculating mean, median, standard deviation and standard error.

create_data_for_graphs/create_data_files.py

Also it calculates number of unique urls as well.