#!/usr/bin/env python3

FILE_MIGRATION_V4_V5 = 'res/fa-migration-v4-v5.txt.original'
FILE_MIGRATION_V4_AND_V5 = 'res/fa-migration-v4-and-v5.txt'

FILE_ICONS_V4 = 'res/fa-icons-v4.txt'
FILE_ICONS_v5 = 'res/fa-icons-v5.txt'

FILE_UNICODE_DIFF_V4_V5 = 'res/fa-unicode-diff-v4-v5.txt'


def output_to_file(file_name: str, contents):
    print('output_to_file({}, {})'.format(file_name, contents))
    with open(file_name, 'w') as f:
        for i in contents:
            if isinstance(i, tuple):
                f.write(' '.join(i))
            else:
                f.write(i)
            f.write('\n')


def normalize_v4_file():
    """Original file from https://fontawesome.com/v4.7.0/cheatsheet/, where the icon section was just copy-pasted."""
    normalize_unicode = lambda s: s.lstrip('[&#x').rstrip('\n').rstrip(';]')

    new_contents = []
    with open(FILE_ICONS_V4) as f:
        for line in f:
            split = line.split(' ')
            if split[1] == '(alias)':
                name = split[0]
                unicode = normalize_unicode(split[2])
            else:
                name = split[0]
                unicode = normalize_unicode(split[1])
            new_contents.append(name + ' ' + unicode)
    output_to_file(FILE_ICONS_V4, new_contents)


def find_removed_unicodes_v4_to_v5() -> list:
    print('find_unicode_diff()')
    v4 = set()
    v5 = set()
    with open('res/fa-unicode-v4.txt') as f:
        for line in f:
            if line.rstrip('\n').isalnum(): v4.add(line.rstrip('\n'))
    with open('res/fa-unicode-v5-solid.txt') as f:
        for line in f:
            if line.rstrip('\n').isalnum(): v5.add(line.rstrip('\n'))
    with open('res/fa-unicode-v5-brands.txt') as f:
        for line in f:
            if line.rstrip('\n').isalnum(): v5.add(line.rstrip('\n'))
    print('v4:', v4)
    print('len(v4)', len(v4))
    print()
    print('v5:', v5)
    print('len(v5)', len(v5))
    print()
    intersection = v4 & v5
    print('intersection:', intersection)
    print('len(intersection)', len(intersection))
    print()
    removed_from_v4 = v4.difference(intersection)
    print('removed_from_v4:', sorted(removed_from_v4))
    print('len(removed_from_v4)', len(removed_from_v4))
    print()
    return sorted(removed_from_v4)


def migration_v4_and_v5_data() -> list:
    print('migration_v4_and_v5_data()')

    v4_name_to_v4_unicode = dict()
    removed_unicodes = find_removed_unicodes_v4_to_v5()
    with open(FILE_ICONS_V4) as f:
        for line in f:
            if len(line.split(' ')) > 1:
                v4_name = line.split(' ')[0]
                v4_unicode = line.split(' ')[1].rstrip('\n')
                if v4_unicode in removed_unicodes:
                    v4_name_to_v4_unicode[v4_name] = v4_unicode

    v4_name_to_v5_unicode = dict()
    with open(FILE_MIGRATION_V4_V5) as f:
        for line in f:
            split = line.rstrip('\n').split('\t')
            v4_name_to_v5_unicode['fa-' + split[0]] = split[3]
    # These weren't mentioned in the migration table from https://fontawesome.com/how-to-use/on-the-web/setup/upgrading-from-version-4
    v4_name_to_v5_unicode['fa-reply'] = 'f3e5'
    v4_name_to_v5_unicode['fa-window-close'] = 'f410'

    v4_name_unicode_v5_unicode = []
    for v4_name, v4_unicode in v4_name_to_v4_unicode.items():
        v5_unicode = v4_name_to_v5_unicode[v4_name]
        v4_name_unicode_v5_unicode.append((v4_name, v4_unicode, v5_unicode))

    return v4_name_unicode_v5_unicode


# Just a little experiment, it is not used
def create_efficient_grep_regex(words) -> str:
    print('create_efficient_grep_regex()')
    root = Node('')
    for word in words:
        node = root
        for c in word:
            node = node.add_child(c)
            print(root)
    print(root)
    print(root.to_grep_regex())

    # grep_regex = '\\({}\\)'.format('\\|'.join(list_of_strings))
    # print(grep_regex)
    return 'todo'


class Node:
    def __init__(self, data):
        self.data = data
        self.children = set()

    def __eq__(self, other):
        print(self.data == other.data)
        return self.data == other.data

    def __lt__(self, other):
        return self.data < other.data

    def __hash__(self):
        print('__hash__ of', self.data, 'is ', hash(self.data))
        return hash(self.data)

    def __str__(self):
        s = '(' + self.data
        for child in sorted(self.children):
            s += str(child)
        s += ')'
        return s

    def to_grep_regex(self) -> str:
        s = self.data
        if self.children:
            s += '['
            for child in sorted(self.children):
                s += child.to_grep_regex()
            s += ']'
        else:
            for child in sorted(self.children):
                s += child.to_grep_regex()
        return s

    def add_child(self, obj):
        if isinstance(obj, Node):
            node = obj
        else:
            node = Node(obj)
        self.children.add(node)
        for child in self.children:
            if child == node:
                return child
        return None


# normalize_v4_file()
# output_to_file(FILE_UNICODE_DIFF_V4_V5, find_unicode_diff())
# output_to_file('res/fa-unicode-diff-with-names-v4-v5.txt', find_unicode_diff_with_names())
# output_to_file(FILE_MIGRATION_V4_AND_V5, migration_v4_and_v5_data())

create_efficient_grep_regex([i[2] for i in migration_v4_and_v5_data()])  # Using list comprehension
