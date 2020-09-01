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
    while True:
        city=input('\nWould you like to see data for Chicago, New York City, or Washington? ')
        city=city.lower()
        if city in ['chicago','new york city','washginton']:
            break
        else:
            print('\nThis is an invalid input, please enter Chicago, New York City, or Washington ')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('\nWould you like to filter the data by month? If so, please type any of the first 6 months name. Type all for no time filter ')
        month=month.lower()
        if month in ['all','january','february','march','april','may','june']:
            break
        else:
            print('\nThis is an invalid input, please enter January, February, March, April, May, June, or All ')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('\nWould you like to filter the data by day of week? If so, please type any day or week. Type all for no time filter ')
        day=day.lower()
        if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            break
        else:
            print('\nThis is an invalid input, please enter Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All ')

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    #print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=df['month'].mode()[0]
    #print(most_common_month)

    print('\nMost Common Month: ',most_common_month)
    # TO DO: display the most common day of week
    most_common_dayofweek=df['day_of_week'].mode()[0]

    print('\nMost Common Day of Week: ', most_common_dayofweek)
    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    #print(df['hour'].unique())
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]

    print('\nMost Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('\nMost commonly used start station is: ', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('\nMost commonly used end station is: ', end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['Combination Station'] = df['Start Station']+" "+df['End Station']
    combo_station = df['Combination Station'].mode()[0]
    print('\nMost commonly used combination of start station and end station is: ', combo_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_duration = df['Trip Duration'].sum()
    print('\nThe total travel time is: ', sum_duration)
    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('\nThe average travel time is: ',mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nThe counts of user types is: \n')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\nThe counts of gender is: \n')
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('\nThe most earliest year of birth is: ',df['Birth Year'].min())
        print('\nThe most recent year of birth is: ',df['Birth Year'].max())
        print('\nThe most common year of birth is: ',df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
