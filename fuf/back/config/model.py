from pydantic import basemodel


class Item(basemodel):
    name: str
    description: str
    tag: str
