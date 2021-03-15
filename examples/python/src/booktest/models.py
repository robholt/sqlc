# Code generated by sqlc. DO NOT EDIT.
from typing import List
import datetime
import enum

import dataclasses



class BookType(str, enum.Enum):
    FICTION = "FICTION"
    NONFICTION = "NONFICTION"


@dataclasses.dataclass()
class Author:
    author_id: int
    name: str



@dataclasses.dataclass()
class Book:
    book_id: int
    author_id: int
    isbn: str
    book_type: BookType
    title: str
    year: int
    available: datetime.datetime
    tags: List[str]


