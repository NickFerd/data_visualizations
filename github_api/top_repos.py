import requests
import pygal
from requests.exceptions import HTTPError
from pygal.style import LightenStyle, DarkSolarizedStyle, DarkStyle, CleanStyle, Style
from datetime import date


def main():
    """Visualization of top 30 repositories on Github
            of each programming language in the list"""
    langs = ['python', 'javascript', 'c++', 'java', 'golang']
    for language in langs:
        repos_info = make_api_call(language)
        plot_data(language, repos_info)


def make_api_call(language):
    """Make Github API call
    If status code : 200 - returns list of top 30 repos (list of dicts)
    else - returns Error message"""
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars"
    try:
        response = requests.get(url)

        # raise exceptions if error occurs
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        resp = response.json()
        repos_info = resp['items']  # type list, consists of dicts with info about repo
        return repos_info


def plot_data(language, repos_info: list):
    # Gather data of each repository to plot it
    names, plot_dicts = [], []
    for repo in repos_info:
        names.append(repo['name'])
        plot_dict = {
            'value': repo['stargazers_count'],
            'label': str(repo['description']),
            'xlink': repo['html_url']
        }
        plot_dicts.append(plot_dict)

    # Make visualization with Pygal
    # Create different styles
    styles = {
        'python': LightenStyle('#FFFF00', base_style=DarkSolarizedStyle),
        'javascript': LightenStyle('#FFFF33', base_style=DarkStyle),
        'c++': LightenStyle('#0066CC'),
        'java': LightenStyle('#FF8000', base_style=CleanStyle),
        'golang': Style(font_family='googlefont:Raleway', colors=('#00CCCC',))
    }

    # Adjust some settings of the plot
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.truncate_label = 15
    my_config.show_legend = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=styles[language])
    chart.title = f"Top 30 {language.capitalize()} Projects on GitHub, updated on {date.today()}"
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file(f'{language}_repos.svg')


if __name__ == '__main__':
    main()
