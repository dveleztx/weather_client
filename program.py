import requests
import bs4


def main():
    print_the_header()

    code = input('What zipcode do you want the weather (97201)? ')

    html = get_html_from_web(code)

    get_weather_from_html(html)

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
    # print(response.text[0:250])

    return response.text


def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature.wu-label'
    # weatherTempCss = '.wu-unit-temperature.wu-value'
    # weatherConditionCss = '.condition-icon'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    # print(soup)


if __name__ == '__main__':
    main()
