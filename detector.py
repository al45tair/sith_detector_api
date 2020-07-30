import random

def sithScore(name, job, likesCats, favouriteLang):
    """Work out whether or not someone is a Sith"""
    score = 0xabadd00d
    for ch in name:
        score += ord(ch)

    for ch in job:
        score += 3 * ord(ch)

    score %= 1879

    if likesCats:
        score /= 7

    if favouriteLang in ('Python', 'Go', 'Rust', 'Haskell', 'Lisp'):
        score /= 5
    elif favouriteLang in ('C', 'C++', 'D'):
        score /= 2
    elif favouriteLang in ('Perl', 'Java'):
        score *= 2
    else:
        score *= 4

    return score

start = [
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P',
    'Qu', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
    ]
vowel = 'aeiou'
consonant = 'bcdfghjklmnprstvwxyz'
endings = [
    '', 'ious', 'er', 'us', 'u'
    ]

def genSithName(seed):
    """Generate a random Sith name"""
    r = random.Random(seed)

    parts = []

    parts.append(start[r.randrange(len(start))])
    parts.append(vowel[r.randrange(len(vowel))])
    if r.random() > 0.5:
        parts.append(vowel[r.randrange(len(vowel))])
    parts.append(consonant[r.randrange(len(consonant))])
    parts.append(endings[r.randrange(len(endings))])

    return ''.join(parts)

score = sithScore(Name, JobTitle, LikesCats, FavouriteLanguage)

if score > 200:
    result = {
        'sith': True,
        'sithName': genSithName(score),
    }
else:
    result = {
        'sith': False
    }
