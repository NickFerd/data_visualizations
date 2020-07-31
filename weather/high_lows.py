import csv
import matplotlib.pyplot as plt
from datetime import datetime


def get_data(csv_reader):
    """Gets needed data from csv-file"""
    highs, lows, dates = [], [], []
    next(csv_reader)  # Get rid of headers

    for row in csv_reader:
        try:
            high = int(row[1])
            low = int(row[3])
            date = datetime.strptime(row[0], '%Y-%m-%d')
        except ValueError:
            print(date, " - missing data")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(date)

    return highs, lows, dates


def main():
    # csv files to parse data from
    sitka = 'sitka_weather_2014.csv'
    death_valley = 'death_valley_2014.csv'

    # Get min, max temperature and date for each day
    with open(sitka) as sitka, open(death_valley) as death_v:
        reader_sitka = csv.reader(sitka)
        reader_valley = csv.reader(death_v)

        highs_valley, lows_valley, dates_v = get_data(reader_valley)
        highs_sitka, lows_sitka, dates_s = get_data(reader_sitka)

    # Visualize data
    fig, axs = plt.subplots(1, 2, sharey=True, figsize=(14, 7), dpi=128)
    fig.suptitle("Daily high and low temperatures, 2014", y=0.98, fontsize=18)
    fig.autofmt_xdate()  # Rotation of x-axes labels

    # Sitka subplot
    axs[0].plot(dates_s, highs_sitka, '-r', dates_s, lows_sitka, '-b')
    axs[0].set_title("Sitka, Alaska", fontsize=16)
    axs[0].set_ylabel('Temperature (F)', fontsize=16)
    axs[0].set_xlabel('Date', fontsize=16)
    axs[0].fill_between(dates_s, highs_sitka, lows_sitka,
                        facecolor='blue', alpha=0.25)
    axs[0].grid(axis='both', linestyle='--')

    # Death-valley subplot
    axs[1].plot(dates_v, highs_valley, '-r', dates_v, lows_valley, '-b')
    axs[1].set_title('Death-Valley, California', fontsize=16)
    axs[1].set_xlabel('Date', fontsize=16)
    axs[1].fill_between(dates_v, highs_valley, lows_valley,
                        facecolor='blue', alpha=0.25)
    axs[1].grid(axis='both', linestyle='--')

    plt.savefig('high-lows_comparison.png')


if __name__ == '__main__':
    main()
