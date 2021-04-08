# rrats

[![Code style: black][black-badge]][black]

this is my own copy of the RRATs database maintained [**here**][rrats] by Bingyi Cui and Maura McLaughlin. the data in the original catalogue might be out-of-date now, since it was updated last in September 2016. nevertheless, this repository scraps the database on the 12th of every month, at midnight, and stores all the data in full JSONic glory in [**rrats.json**](rrats.json). the code that runs this repository is in [**scrap.py**](scrap.py). this repository will eventually power the [**koshka**][koshka] package, which aims to make accessing all pulsar and radio transient related catalogues easier.

[black]: https://github.com/psf/black
[rrats]: http://astro.phys.wvu.edu/rratalog/
[koshka]: https://github.com/astrogewgaw/koshka
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
