if __name__ == "__main__":

    from json import dump
    from requests import get
    from bs4 import BeautifulSoup
    from typing import Dict, Union, Optional

    data: Dict[
        str,
        Dict[
            str,
            Optional[
                Union[
                    str,
                    int,
                    float,
                ]
            ],
        ],
    ] = {}

    rows = BeautifulSoup(
        markup=get("http://astro.phys.wvu.edu/rratalog/").content,
        features="lxml",
    ).table("tr")[2:]

    for i, row in enumerate(rows):
        cells = [_.text for _ in row("td")]
        data[str(i + 1)] = {
            key: (None if (cell == "--") or (cell == "") else conv(cell))
            for (key, conv), cell in zip(
                [
                    ("NAME", str),
                    ("P0", float),
                    ("P1", float),
                    ("DM", float),
                    ("RAJ", str),
                    ("DECJ", str),
                    ("GL", float),
                    ("GB", float),
                    ("BURST_RATE", float),
                    ("LOG_B", float),
                    ("LOG_AGE", float),
                    ("DIST", float),
                    ("S140", float),
                    ("S350", float),
                    ("S1400", float),
                    ("W140", float),
                    ("W350", float),
                    ("W1400", float),
                    ("RM", float),
                    ("LIN_POL", float),
                    ("SURVEY", str),
                ],
                cells,
            )
        }

    with open("rrats.json", "w+") as fobj:
        dump(
            obj=dict(data=data),
            fp=fobj,
            indent=4,
        )
