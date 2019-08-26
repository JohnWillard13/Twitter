from tweet import Tweet

tweetList = []

runAgain = 1

while runAgain == 1:
    print('\n')
    print("Tweet Menu")
    print("-------------")
    print("1. Make a Tweet")
    print("2. View Recent Tweets")
    print("3. Search Tweets")
    print("4. Quit")

    option = input("Which option would you like to use: ")

    if option == '1':

        author = input("What is your name: ")
        while True:
                
            text = input("Enter your tweet (140 char max): ")
            if len(text) > 140:
                print("Tweets can only be 140 characters long. Try again.")
            else:
                break
        tweetList.append(Tweet(author,text))
        continue
    if option == '2':

        if not tweetList:
            print("There are currently no tweets.")
            continue
        else:

            for tweets in reversed(tweetList):
                print('\n')
                print(f'{tweets.get_author()} - {tweets.get_age()}\n{tweets.get_text()}')
        continue

    if option == '3':
        word = input("Enter a word you would like to search for: ")

        if not tweetList:
            print("There are currently no tweets.")
            continue
        else:
        
            for tweets in reversed(tweetList):
                if word in tweets.get_text():
                    print('\n')
                    print(f'{tweets.get_author()} - {tweets.get_age()}\n{tweets.get_text()}')
        continue

    if option == '4':
        print("Exiting...")
        break

    else:
        print("Not a valid option")
        continue

    again = input("Would you like to choose a different option (y/n): ")
    if again == 'y':
        runAgain == 1
    else:
        print("Exiting...")
        break
