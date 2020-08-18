import requests
from requests.exceptions import HTTPError
from operator import itemgetter
from tqdm import tqdm   # progress visualization


def main():
    """Getting top 30 articles on HackerNews ranked by number of comments"""

    # Getting top stories IDs
    top_stories = make_api_call()  # --> type: list

    # Gather info about every story
    stories_dicts = []
    for story_id in tqdm(top_stories[:30]):
        info = make_api_call(story_id)  # --> type: dict

        story_dict = {
            'title': info['title'],
            'link': f'http://news.ycombinator.com/item?id={str(story_id)}',
            'comments': info.get('descendants', 0)
        }
        stories_dicts.append(story_dict)

    # Sort articles by the most comments
    stories_dicts = sorted(stories_dicts, key=itemgetter('comments'),
                           reverse=True)

    for story in stories_dicts:
        print('\nTitle: ', story['title'])
        print('Discussion link: ', story['link'])
        print('Comments number:', story['comments'])


def make_api_call(item_id=None):
    """If no id is passed, returns list of IDs of top stories,
        else returns info (python dict) about the item with passed id"""
    if not item_id:
        url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    else:
        url = f'https://hacker-news.firebaseio.com/v0/item/{str(item_id)}.json'

    # HackerNews API call
    try:
        resp = requests.get(url)

        # raise exceptions if error occurs
        resp.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred with article (id={item_id}): {http_err}')
    except Exception as err:
        print(f'Other error occurred with article (id={item_id}): {err}')
    else:
        answer = resp.json()
        return answer


if __name__ == '__main__':
    main()


