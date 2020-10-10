import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    
    city = ["chicago", "new york city", "washington"]
    city_name = input("Please enter the name of the city you want to analyse (chicago, new york city or washington)\n") 
    while city_name.lower() not in city:
        message = "This city is not available. Please enter correct city (chicago, new york city or washington)\n"
        city_name = input(message)

    # TO DO: get user input for month (all, january, february, ... , june)
    
    months = ["all", "january", "february", "march", "april", "may", "june"]
    month = input("Please enter the month to filter by. If you do not want to filter data by month, please enter all\n")
    while month.lower() not in months:
        message = "This month is not available. Please enter correct month. If you do not want to filter data by month, please enter all\n"
        month = input(message)
       
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = input("Please enter the day of week to filter by. If you do not want to filter by day of week, please enter all\n")
    while day.lower() not in days:        
        message = "This day is not available. Please enter correct day. If you do not want to filter by day of week, please enter no\n"
        day = input(message)
        

    print('-'*40)
    return city_name, month, day


def load_data(city_name, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city_name.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month.lower() != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month

    # find the most common month
    common_month = df['month'].mode()[0]

    print('Most common month: ', common_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract day of week from the Start Time column to create a day of week column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # find the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]

    print('Most common day of week: ', common_day_of_week)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create a hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common start hour
    common_start_hour = df['hour'].mode()[0]

    print('Most common start hour: ', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # find the most common used start station
    common_used_start_station = df['Start Station'].mode()[0]

    print('Most common start station: ', common_used_start_station)

    # TO DO: display most commonly used end station
    
    # find the most common used end station
    common_used_end_station = df['End Station'].mode()[0]

    print('Most common end station: ', common_used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = [
    ' '.join([x, 'to', y]) for x, y in zip(df['Start Station'], df['End Station'])]
    
    most_freq_combination = df['route'].mode()[0]
    
    print("Most frequent combination of start and end station trip: ", most_freq_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    
    print('Total travel time: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        
        gender = df['Gender'].value_counts()
    
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
    
        earliest_birth = df['Birth Year'].min()
    
        print("Earliest birth year: ", earliest_birth)
    
        most_recent_birth = df['Birth Year'].max()
    
        print("Most recent birth year: ", most_recent_birth)
    
        most_common_year_of_birth = df['Birth Year'].mode()[0]
    
        print("Most common year of birth: ", most_common_year_of_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    
    while (view_data.lower() != "no" and view_data.lower() != "yes"):
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        
    while (view_data.lower() == "yes"):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data= input("Do you wish to continue? Enter yes or no\n")
        
        while (view_data.lower() != "no" and view_data.lower() != "yes"):
            view_data = input("Do you wish to continue? Enter yes or no\n")
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
