# Frequency Analysis of Words

Script to print 10 most frequent words from text file.

# Quickstart

This was tested on windows, python 3.5+.
You can just type in command console: 
```
python lang_frequency.py <file name>
```

# Output example

From text file which contains something like:
```
раз два два три три три четыре четыре четыре четыре one two десять десять десять десять пять шесть шесть
двадцать двадцать двадцать двадцать forty forty forty forty forty forty forty
```

Output will be:
```
>forty
>двадцать
>десять
>четыре
>три
>два
>шесть
>one
>two
>пять
```

# Functions

As alternative, you can import functions from this script to use in your project:
```python
load_data(file_path) # just loads data from text file.
```

```python
get_most_frequent_words(text) # returns list which contains words ordered from most frequent to least frequent with quantity.
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
