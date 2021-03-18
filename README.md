# rrats

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

this is my own copy of the RRATs database maintained [**here**](http://astro.phys.wvu.edu/rratalog/) by Bingyi Cui and Maura McLaughlin. the data in the original catalogue might be out-of-date now, since it was updated last in September 2016. nevertheless, this repository scraps the database on the 12th of every month, at midnight, and stores all the data in full JSONic glory in **rrats.json**. the code that runs this repository is in **scrap.py**. this repository will eventually power the **neko** package, which aims to make accessing all pulsar and radio transient related catalogues easier.
