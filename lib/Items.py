# pylint: disable=invalid-name, line-too-long, too-many-instance-attributes, too-few-public-methods
from numpy.random import choice
items = {
    "travis":  {
        "common": {
            "name": "business pen",
            "dmg": 2
        },
        "rare": {
            "name": "iphone 3",
            "dmg": 3
        },
        "nothing": {}
    },
    "rob": {
        "common": {
            "name": "used napkin",
            "dmg": 2
        },
        "rare": {
            "name": "nice key board",
            "dmg": 3
        },
        "nothing": {}
    },
    "xiaolu": {
        "common": {},
        "rare": {
            "name": "coke can",
            "dmg": 20

        },
        "nothing": {}
    }
}


def get_items(name):
    probabilities = {"rare": 0.001, "common": 0.3, "nothing": 0.609}
    test = choice(probabilities.keys())
    return items[name][test]
