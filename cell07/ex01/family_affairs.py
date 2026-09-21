#!/usr/bin/env python3


def find_the_redheads(persons):
    return list(filter(lambda name: persons[name] == "red", persons.keys()))


dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
