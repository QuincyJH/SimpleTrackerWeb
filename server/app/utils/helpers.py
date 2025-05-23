import re
import unicodedata

def to_snake_case(s):
    s = unicodedata.normalize('NFKD', s)
    s = re.sub(r'[^a-zA-Z0-9\s]', '', s)
    s = re.sub(r'(?<!^)(?=[A-Z])', '_', s)
    return s.lower()

def to_words(s):
    s = unicodedata.normalize('NFKD', s)
    s = re.sub(r'[^a-zA-Z0-9\s]', '', s)
    s = re.sub(r'(?<!^)(?=[A-Z])', ' ', s)
    return s