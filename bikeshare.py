import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all', 'january', 'february' , 'march', 'april', 'may', 'june']
days = ['all','monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday' , 'sunday']
yes_no =['yes' , 'no']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago' , 'new york city' , 'washington']
    
    
    
    while True:
        try:
            letter_c = input('Type a number corresponding the city you want to filter by: \n 1 for Chicago \n 2 for New York city \n 3 for Washington\n')
            while int(letter_c) not in list(range(1,4)):
                print('Invalid Input')
                letter_c = input('Type a number corresponding the city you want to filter by: \n 1 for Chicago \n 2 for New York city \n 3 for Washington\n')
        except ValueError:
            print('Please type a number')
            continue
        else:
            break
            
        
    city = cities[int(letter_c)-1] 
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            letter_m = input('Type a number corresponding to the month you want to filter by or 0 for no filters:\n 1 for January \n 2 for February \n 3 for March \n 4 for April \n 5 for May \n 6 for June \n 0 for no filter \n')
            while int(letter_m) not in list(range(7)):
                print('Invalid Input')
                letter_m = input('Type a number corresponding to the month you want to filter by or 0 for no filters:\n 1 for January \n 2 for February \n 3 for March \n 4 for April \n 5 for May \n 6 for June \n 0 for no filter \n')
        except ValueError:
            print('Please type a number')
            continue
        else:
            break        
    month = months[int(letter_m)]
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            letter_d = input('Type a number corresponding to the day you want to filter by or 0 for no filters:\n 1 for Monday \n 2 for Tuesday \n 3 for Wednesday\n 4 for Thursday\n 5 for Friday\n 6 for Saturday\n 7 for Sunday\n 0 for no filter \n')
            while int(letter_d) not in list(range(8)):
                print('Invalid Input')
                letter_d = input('Type a number corresponding to the day you want to filter by or 0 for no filters:\n 1 for Monday \n 2 for Tuesday \n 3 for Wednesday\n 4 for Thursday\n 5 for Friday\n 6 for Saturday\n 7 for Sunday\n 0 for no filter \n')
        except ValueError:
            print('Please type a number')
            continue
        else:
            break
    day = days[int(letter_d)]
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] =df['Start Time'].dt.hour
    
    if month != 'all':
        df = df[df['month'] == months.index(month)]
    
    if day != 'all':
        df = df[df['day'] == day.title()]


    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all' :
        print('\nMost Common Month:')
        print(df['month'].mode()[0])
    else:
        print('You Have filtered by a month, so all stats are within {}'.format(month))
    # TO DO: display the most common day of week
    if day == 'all':
        print('\nMost Common Day Of The Week:')
        print(df['day'].mode()[0])
    else:
        print('You Have filtered by a day, so all stats are within {}'.format(day))

    # TO DO: display the most common start hour
    print('\nMost Common Hour')
    print(df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Common Start Station:')
    print(df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('\nMost Common End Station:')
    print(df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip

    
    df['Combined Stations'] = df['Start Station'] + " --- " + df['End Station']
    print('\nMost Frequent combination of start and end stations:')
    print(df['Combined Stations'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal Travel Time')
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('\nMean Travel Time')
    print(df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('\nUser Types')
    print(user_type)


    # TO DO: Display counts of gender
    if city == 'washington':
        print('\n There is no data about gender or birth year for users in {}'.format(city))
    else:
        
        genders = df['Gender'].value_counts()
        print('\nGendar counts')
        print(genders)
    
    
        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nEarliest year of birth: {}'.format(int(df['Birth Year'].min())))
        print('\nMost Recent year of birth: {}'.format(int(df['Birth Year'].max())))
        print('\nMost common year of birth: {}'.format(int(df['Birth Year'].mode()[0])))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_input(df):
    print('Raw Data are avaialble to view ')
    displayer =input('Would Like to Check it? YES - NO \n')
    while displayer.lower() not in yes_no:
        print('Invalid Input')
        displayer =input('Would Like to Check the Raw Data? YES - NO \n')
    if displayer.lower() == 'yes':
        print('\nOkay here are some info about the data \n')
        print(df.info())
        print('\nPlease specify the number of datapoint/row you want to start from, and the number of dataponts/rows you want to view \n')
        while displayer.lower() == 'yes':
            try:
                start = input('Number of the first Datapoint/row you want to view Choose between and including 1 - {}: \n'.format(str(len(df))))
                while int(start) not in list(range(1,len(df)+1)):
                    print('Invalid Input')
                    start = input('Number of the first Datapoint/row you want to view: \n')
                starter = int(start) -1
                count = input('Number of Datapoints/rows you want to view: \n')
                counter = int(count)
                if starter + counter >= len(df):
                    print(df.iloc[starter: , :])
                else:
                    print(df.iloc[starter : starter + counter, :])
            except ValueError:
                print('Please type a number')
                continue
            else:
                displayer = input('Would Like to check another range of rows? YES - NO \n')
                while displayer.lower() not in yes_no:
                    print('Invalid Input')
                    displayer =input('Would Like to check another range of rows? YES - NO \n')
                if displayer.lower() == 'no':
                    print('Bye For now')
    else:
        print('Bye For now')
        
        
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_input(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

