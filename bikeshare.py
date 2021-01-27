import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv','new york city': 'new_york_city.csv','washington': 'washington.csv' }
cities= ['chicago','new york city','washington']
months=['January','February','March','April','May','June','July','August',
        'September','October','November','December','All']
days= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
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
        city=str(input("Would you like to see data for chicago,new york city, or washington? ")).lower()
        if city not in cities:
                print("Please enter valid city")
        else:
                    break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=str(input("Would you like to filter the data by month? If yes wirite month else write 'all'? ")).title()
        if month not in months:
         print("please writr valid month name")
        else:
         break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
     day= input("Would you like to filter the data by day? If yes wirite day else write 'all'? ").title()
     if day not in days:
      print('please writr valid day name')
     else:
        break


    print('-'*40)
    return city,month,day


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
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month !='All':
        month=month.index(month)+1
        df=df[df['month']==month]
    if day!='All':
        df=df[df['day_of_week']== day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']= df['Start Time'].dt.weekday_name

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_mode=df['month'].mode()[0]
    print('most common month is {}'.format(months[month_mode-1]))

    # TO DO: display the most common day of week
    print('most common day is {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print('most common start hour is {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start statio is {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('most commonly used end station is {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    most_combination= df['Start Station'].map(str)+'to'+df['End Station']
    print('most frequent combination of start station and end station trip is {}'.format(most_combination.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_m,total_s= divmod(df['Trip Duration'].sum(),60)
    total_h,total_m= divmod(total_m,60)
    print('total travel time is ',total_h,'hours,',total_m,'minutes,and',total_s,'seconds.')

    # TO DO: display mean travel time
    mean_m,mean_s= divmod(df['Trip Duration'].mean(),60)
    mean_h,mean_m= divmod(mean_m,60)
    print('mean travel time is ',mean_h,'hours,',mean_m,'minutes,and',mean_s,'seconds.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('user types {}'.format(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    if('Gender' not in df):
        print('Sorry!')
    else:
        print('Gender is \n{}'.format(df['Gender'].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' not in df):
        print('wrong birth year')
    else:
        print('earliest birth year is {}'.format(df['Birth Year'].min()))
        print('most recent birth year is {}'.format(df['Birth Year'].max()))
        print('most common year of birth year is {}'.format(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def view_data(df):
    start=0
    choice=input('\n Woluld you like to view data? Enter yes or no.\n')
    while choice=='yes':
        try:
            n=int(input('How many row would you like to view\n'))
            n=start+n
            print=(df[start:n])
            choice=input('Do you like view more rows?Enter yes or no.\n')
            start=n
        except ValueError:
            print("Oops! That was no valid number.Try again")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
