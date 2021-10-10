import tweepy
import secrets
import pyodbc
from teams import teaminfo 

# Gets the twitter data for the past 12 hours for the team entered as a parameter
# Just pulls all the tweets, adds the tweet body to a dictionary of strings and timestamps
def get_data_for_team(team_abbreviation):
    pass

# Authenticates to our Azure SQL DB using the credentials stored in secrets.py
# Will be utilized by main to write the data from get_data_for_team into our database
def write_to_database(database_name, data_name):
    pass

# Main logic for pulling our data and writing it to our database
def main():
    pass

if __name__ == '__main__':
    main()

