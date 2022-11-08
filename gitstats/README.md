Purpose
===========
gitstats is a statistics generator for git repositories.  It is mostly intended
for developers, as a way to check some development statistics for a project.

Currently it produces only HTML output with tables and graphs.

Authors
===========
Original author can be reached by sending e-mail to <hoxu@users.sf.net>. Also thanks to the following people: Alexander Botero-Lowry. All credit goes to Heikki Hokkanen. Thank you. 

Currently, code is being modified to fit with python3 and his own usage of the data, which will be shown in a json data object for web consumption. 

License
===========
* gitstats license is GPLv2/GPLv3, see doc/GPLv2 and doc/GPLv3 respectively.
* sortable.js, contained in gitstats, is licensed under the MIT license. See the
file itself for details.

Requirements
============
- Python (>= 3)
- Git (>= 1.5.2.4)
- Gnuplot (>= 4.0.0)
- a git repository (bare clone will work as well)


Newbie Python Concepts
============
* Integrating `make` with project to automate the installation of dependencies and running the app. A `Makefile` needs to be at the roo of the project, this file instructs `make` on what to do, consisting of a set of rules - 3 parts with a target, prereq and a recipe. 
* `sys` - system specific parameters, can attain version info
* `os` - operating system interfaces, can attain environment info
* `platform` - provides system information, check whether program is compatible with python version
* `time` - timestamp is in milliseconds since the epoch

Python Issues
============
* [bytes to string](https://stackoverflow.com/questions/606191/convert-bytes-to-a-string)

Generated Output
============
This is a [sample](https://github.com/irbull/gitscripts/blob/master/yearly_stats) of the data and the GNU plots that will be generated. 

Running
=============
```./gitstatslite /Users/${user_pwd}/jessewoo.github.io/ ~/Documents/${user_pwd}/stats/jessewoo```