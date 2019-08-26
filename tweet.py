from datetime import datetime as dt
import time


class Tweet:
    def __init__(self,author,text):
        self.__author = author
        self.__text = text
        self.__age = dt.now()

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_age(self):
        tweetAge = dt.now() - self.__age
        days = tweetAge.days
        hours = tweetAge.seconds // 3600
        minutes = tweetAge.seconds % 3600 // 60
        seconds = tweetAge.seconds % 60
        ageUnit = ""
        if days:
            ageUnit += f' {days}d'
        if hours:
            ageUnit += f' {hours}h'
        if minutes:
            ageUnit += f' {minutes}m'
        if seconds:
            ageUnit += f' {seconds}s'

        return ageUnit
        
