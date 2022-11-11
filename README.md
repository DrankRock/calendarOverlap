# Calendar Overlap

Check if activities with precise schedule are overlapping, in general or a selection of them, with python3.

## Installing

To install this project, simply copy and paste these in the console :

```
git clone https://github.com/DrankRock/calendarOverlap.git
cd calendarOverlap
```
There are no specific requirements for this project.

## Example : 
```console
matvei@BigDen:$ python calendarOverlap.py -n Math Monday 8:00 9:30
matvei@BigDen:$ python calendarOverlap.py -n Science Monday 9:45 11:15
matvei@BigDen:$ python calendarOverlap.py -n History Tuesday 17:00 18:00
matvei@BigDen:$ python calendarOverlap.py -n French Tuesday 13:00 14:00
matvei@BigDen:$ python calendarOverlap.py -n English Monday 11:00 13:00
matvei@BigDen:$ python calendarOverlap.py -r History
matvei@BigDen:$ python calendarOverlap.py -s
Content of the config File (.calConfig) :
| - Math : Monday, 8:00, 9:30
| - Science : Monday, 9:45, 11:15
| - French : Tuesday, 13:00, 14:00
| - English : Monday, 11:00, 13:00
Overlapping Activities : 
| - Science ; English
matvei@BigDen:$ python calendarOverlap.py -c English Science Math
[['Science', 'English']]
```

## Usage
### Show the help : 
```
python3 calendarOverlap.py -h
```
This command will show : 
```
usage: calendarOverlap.py [-h] [-n NEWACTIVITY NEWACTIVITY NEWACTIVITY NEWACTIVITY] [-d DELETE] [-i [INPUT]] [-s] [-c CHECKOVERLAP [CHECKOVERLAP ...]]

Check if a set of weekly activities would overlap if put together.

options:
  -h, --help            show this help message and exit
  -n NEWACTIVITY NEWACTIVITY NEWACTIVITY NEWACTIVITY, --newactivity NEWACTIVITY NEWACTIVITY NEWACTIVITY NEWACTIVITY
                        Add an activity to the list.
  -r REMOVE, --remove REMOVE
                        Remove an activity from the list.
  -i [INPUT], --input [INPUT]
                        Use as input another config file (default is .calConfig)
  -s, --show            Show the config data and current overlapping activities
  -c CHECKOVERLAP [CHECKOVERLAP ...], --checkOverlap CHECKOVERLAP [CHECKOVERLAP ...]
                        Check if the activities given as arguments overlap with each other
  ```
### Add an activity :
```
python3 calendarOverlap.py -n Name Day StartTime EndTime
```

* **StartTime and EndTime must respect the format HH:MM (example : 13:30)**
* **Day can have any name, what matters is that two activities on the same day has the same day name**
Not giving a precise day format makes it possible to make bi-weekly schedules or any type of schedule, as in : 
```
python3 calendarOverlap.py -n Math Monday1 8:30 11:00
python3 calendarOverlap.py -n Science Monday2 10:15 12:45
python3 calendarOverlap.py -n French Monday1 10:15 12:45
```
Science overlaps with nothing, but Math and French do.

### Remove an activity
```
python3 calendarOverlap.py -r nameOfTheActivity
```

### Show the content of the config file
```
python3 calendarOverlap.py -s
```

### Check if a set of activities overlap
```
python3 calendarOverlap.py -c Activity1 Activity2 ...
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

