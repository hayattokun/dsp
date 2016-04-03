# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are similar in that they are both a collection of values indexed by integers. They are different in that lists have [] around them and tuples have () (or nothing) around them. Also, lists are mutable but tuples are not. That is why tuples work as keys in dictionaries but lists won't work.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists are an ordered sequence of elements. Sets are an unordered sequence of hashable elements. Sets also cannot contain duplicates and let you do operations such as intersection, union, difference, and symmetric difference. You would use a list to make a sequence of first & last names of guests to a wedding b/c you might have guests with the same names and you might want to sort the sequence alphabetically by first or last name. You would use a set to make a sequence of the words used in a news article since you don't want duplicates. Sets are faster for finding elements because they use hash lookup, which means the time for finding an element basically doesn't change even if you add a huge number of elements. Finding elements in a list will slow down the longer the list.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>>  `lambda` lets you create anonymous, one-time-use functions on the fly. Rather than assigning a function to a name it just returns the function.  It's most commonly used with the map(), reduce(), and filter() functions. Here's an example where we reverse sort a list of colors based on the length of the words: sorted(["blue", "green", "red", "yellow"], key=lambda color: len(color), reverse=True)

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





