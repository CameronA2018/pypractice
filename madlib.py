story = '''As a boy, {0} was {10} and sad. He had no friends, was {2} by {1}, and tried to {3}. One day a little {6} told him that she 
thought he was {11}, and that she wanted to {4} him. Thinking she meant to {6}, he pushed her away and created a story in his mind as to why he 
pushed her away. He told himself that she was an {12} {7} from Mars. And soon, he began to believe it. When he saw her in the school hallways, he saw an 
{7} that was trying to eat {8}, and in genuine fear for his life, he told {9} what he was {5}. They thought he was {13}, and he was sent to 
a mental institute where he was strapped to a bed in a straight jacket and put in a padded white room. 
No one outside of the facility ever heard from poor {0} again.'''

print ('''As a boy, ___ was ___ and sad. He had no friends, was ___ by ___, and tried to ___. One day a little ___ told him that she
thought he was ___, and that she wanted to ___ him. Thinking she meant to ___, he pushed her away and created a story in his mind as to why he
pushed her away. He told himself that she was an ___ ___ from Mars. And soon, he began to believe it. When he saw her in the school hallways, he saw an
___ that was trying to eat ___, and in genuine fear for his life, he told ___ what he was ___. They thought he was ___, and he was sent to
a mental institute where he was strapped to a bed in a straight jacket and put in a padded white room.
No one outside of the facility ever heard from poor ___ again.''')

name1 = raw_input('Enter a name ')
name2 = raw_input('Enter a second name ')
verb1 = raw_input('Enter a verb ')
verb2 = raw_input('Enter another verb ')
verb3 = raw_input('Enter another verb ')
verb4 = raw_input('Enter another verb ')
noun1 = raw_input('Enter a noun ')
noun2 = raw_input('Enter another noun ')
noun3 = raw_input('Enter another noun ')
noun4 = raw_input('Enter another noun ')
adjective1 = raw_input('Enter an adjective ')
adjective2 = raw_input('Enter another adjective ')
adjective3 = raw_input('Enter another adjective ')
adjective4 = raw_input('Enter another adjective ')

adjusted = story.format(name1, name2, verb1, verb2, verb3, verb4, noun1, noun2, noun3, noun4, adjective1, adjective2, adjective3, adjective4)

print (adjusted)


# Madlib Short Story
##  1111/4  nouns
##  1111/4  verbs
##  1111/4  adjectives
##  11/2  names
