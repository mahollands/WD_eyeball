# WD Eyeball

A tool for classifying white dwarf spectra from a directory of figures.

# Features
* Classify spectra based on spectral type
* Add secondary classification for some objects such as WDs
* Fully configurable keyboard options for different categories
* Easily modifiable to add new classification options
* Automatic backups
* Option to start at the first unclassified spectrum
* Option to skip to next unclassified spectrum
* Progress bar

# Dependencies
* Python >= 3.6
* numpy
* pygame

# Installation and setup
The only non-standard python module is *pygame* for drawing the UI. The most
recent version is most easily installed using pip, i.e.
```pip install pygame```
The configuration can be updated by editing *config.py*, including most
key-bindings, as well as setting the directory where your spectra images are
located (and their size). Then it is as simple as running the executable
*eyeball.py*.
