import requests


def main():
    print_the_header()

    code = input('What zipcode do you want the weather (97201)? ')

    # get html from web
    get_html_from_web(78213)

    # parse the html
    # display for the forecast


def print_the_header():
    print('---------------------------')
    print('       WEATHER APP')
    print('---------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    # print(response.status_code)
    print(response.text[0:250])


if __name__ == '__main__':
    main()
