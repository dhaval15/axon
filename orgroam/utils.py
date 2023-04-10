import re
from .config import *

def trim_quotes(str):
    return str[1: len(str) - 1]

def elisp_map_to_json(text:str):
    return text.replace('" . "', '" : "') \
        .replace(') (', ',') \
        .replace('((', '{') \
        .replace('))', '}') \

def elisp_list_to_json(text: str):
    return text.replace('(', '[').replace(')', ']')

def extract_inline(path: str, pos: int):
    orig_path = org_roam_path_transformer(path)
    file = open(orig_path)
    file.seek(pos - 1)
    link = _read_link(file)
    file.close()
    match = re.search('\[\[(.*)\]\[(.*)\]\]', link) # Link with urls
    if match is not None:
        return match.groups()[1]
    match = re.search('\[\[(.*)\]\]', link) # Heading links
    if match is not None:
        return match.groups()[0]
    file = open(orig_path)
    file.seek(pos - 1)
    print(file.read(200))

def extract_content(path: str):
    orig_path = org_roam_path_transformer(path)
    print(orig_path)
    file = open(orig_path)
    content = file.read()
    file.close()
    return content

def _read_link(file):
    link = ''
    c = file.read(1)
    im = f' {c}'
    i = 0
    while i < 1000:
        i = i + 1
        c = file.read(1)
        link = link + c
        im = im[len(im) - 1] + c
        if im == '[[':
            link = '[['
        if im == ']]':
            break
    return link.replace('\n', ' ').strip()
