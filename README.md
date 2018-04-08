# Decis: Make decisions based on requirements and markdown files.

## Features
- Collect data using .md files
- Specify requirements with their priority
- Calculate best choice

## Prerequisites
To run Restbot, you will need the following:
- git
- python

## Installation
```
git clone [this repository]
```

## Example
```
$ python decis/decis.py decis/example/
name: machine1
=========================================
price: cheap (90)
looks: Very professional  (90)
quality: not tested (0)
=========================================
outcome: 67.50

name: machine2
=========================================
price: average (50)
looks: Amazing  (100)
quality: Certified (100)
=========================================
outcome: 75.00
```

## Usage
```
usage: decis.py [folder]
```

## Folder structure
A folder should contain requirements and choices. 

Example folder structure:
- requirements.txt
- choices
  - machine1.md
  - machine2.md

## How to write a requirements (.txt) file?
A requirements file needs the following:

| | |
|-|-|
| **requirement** | name of requirement |
| **importance** (int) | value between 0-100, where higher is more important |

### Format
Each requirement must start on a new line and use the following format:
[requirement][[importance]]

#### Example
```
price[90]
looks[25]
quality[25]
```

(see also ./decis/examples)

## How to write a choice (.md) file?
A choice file needs the following:

| | |
|-|-|
| **requirement** | name of requirement (from requirements.txt) |
| **short** | 1-2 words review |
| **satisfaction** (int) | value between 0-100, where higher is better |
| **description** | arguments for review |

### Format
Each review must start on a new line and use the following format:
[requirement]: [short][[satisfaction]]. [description].

#### Example
```
# Machine 1
price: cheap[90]. Cheap compared with others 
looks: Very professional [90]. Professionaldesigned user interface, nice minimal layout.
quality: not tested[0]. Not yet tested for production.

```

(see also ./decis/examples)

## License
Licensed under AGPL3.
