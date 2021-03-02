#!/usr/bin/env python3
from typing import Optional
import datetime

class Entry:
    start: int
    end: int
    course: dict[str, str]

    def __init__(self, data):
        self.start = data['start']
        self.end = data['end']
        self.course = data['course']

    def active(self, time: int) -> bool:
        return self.start <= time < self.end

    def describe(self):
        return f'{self.start:02d} - {self.end}: {self.course["name"]}'

    def __str__(self) -> str:
        space = max([ int(len(k)) for k in self.course.keys()])

        def fmt(k: str, v: str):
            return f'{k.ljust(space)}: {v}'
        out = [ fmt(k, v) for k, v in self.course.items() ]
        return "\n".join(out)

class Day:

    def __init__(self, data):
        self.entries = [ Entry(v) for v in data ]

    def now(self) -> Optional[Entry]:
        current = int(datetime.datetime.now().strftime('%H'))
        for i in self.entries:
            if i.active(current):
                return i

    def at(self, time: int) -> Optional[Entry]:
        for i in self.entries:
            if i.active(time):
                return i

    entries: list[Entry]

    def __str__(self) -> str:
        def fmt(e: Entry):
            return f'{e.start:02d} - {e.end}: {e.course["name"]}'
        out = [ fmt(e) for e in self.entries  ]
        return "\n".join(out)


class Schedule:

    def __init__(self, days: dict[str, object]) -> None:
        self.days = { k: Day(v) for k, v in days.items() }


    days: dict[str, Day]

    def select(self, name) -> Day:
        try:
            return self.days[name]
        except KeyError:
            return Day({})

    def day(self, name) -> Day:
        return self.select(name)

    def day_delta(self, delta) -> Day:
        selected_day = datetime.datetime.now() + datetime.timedelta(days=delta)
        return self.select(selected_day.strftime("%A").lower())

    def today(self) -> Day:
        return self.day_delta(0)
