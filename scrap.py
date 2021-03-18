import re
import json
import requests

from typing import Optional
from schema import Use, Schema

# URL of the RRATs catalog.
url = "http://astro.phys.wvu.edu/rratalog/rratalog.txt"


def validator(s: str) -> Optional[float]:

    """
    A validator to deal with numeric values that could possibly be NULL.
    """

    if s == "--":
        return None
    else:
        return float(s)


# The key-value map for the database.
kvs = {
    "NAME": Use(str),
    "P": Use(validator),
    "PDOT": Use(validator),
    "DM": Use(validator),
    "RA": Use(str),
    "DEC": Use(str),
    "GAL_L": Use(validator),
    "GAL_B": Use(validator),
    "RATE": Use(validator),
    "LOG_B": Use(validator),
    "LOG_TS": Use(validator),
    "D_HAT": Use(validator),
    "FLUX_D": Use(validator),
    "W": Use(validator),
    "SURVEY": Use(str),
}


def scrap() -> None:

    """
    Scrap the RRATs database and serialise it into a JSON file.
    """

    cat = requests.get(url)
    data = cat.content.decode()
    rows = [
        [_ for _ in re.split(r"\s+|\t+|\r+", _) if _]
        for _ in re.split(r"\n+", data)[1:-1]
    ]
    rratp = lambda keys, vals: {key: val for key, val in zip(keys, vals)}
    rrats = {
        str(i + 1): Schema(kvs).validate(rratp(kvs.keys(), row))
        for i, row in enumerate(rows)
    }

    with open("rrats.json", "w+") as fobj:
        json.dump(
            rrats,
            fobj,
            indent=4,
        )


if __name__ == "__main__":

    scrap()