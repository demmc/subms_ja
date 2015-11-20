import re
import argparse

import praw
import bs4

VERSION = '0.1.0'


def parse_args():
    p = argparse.ArgumentParser(description='get japanese subreddits')
    p.add_argument('--version', action='version', version='subms_ja v%s' % VERSION)
    return p.parse_args()


def main():
    _ = parse_args()

    reddit = praw.Reddit('subms_ja/{VERSION}'.format(**globals()))
    page = reddit.get_wiki_page('newsokur', 'subreddits_jp')

    subms = set()
    bs = bs4.BeautifulSoup(page.content_html, 'html.parser')
    for a in bs.select('.wiki tbody a'):
        href = a.get('href')

        href_re = r'(?i)/?r/([0-9a-z_]+)'
        href_m = re.match(href_re, href)
        if not href_m or '+' in href:
            continue

        subm = href_m.group(1)
        subms.add(subm)

    for s in sorted(subms):
        print(s)


if __name__ == '__main__':
    main()
