# Python Tuples

## Objectives

- Learn proper use of tuple data types
- How to work with tuples
- Learn the limitations of tuples

## What Are Tuples

A tuple is a collection of objects which ordered and immutable. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

Unfortunately `javascript` does not have a tuple equivalent as of this writing.

A tuple is declared by using `()` or the `tuple` constructor, example:

```py
tuppy = ()

new_tup = tuple()
```

Here's an example of a tuple:

```py
my_tup = (1,3,4)
```

Tuples can have a mixture of data types:

```py
mixed_tup = (1,'String',False, None)
```

A tuple cannot be modified in any way, it's best used for data that you do not want to be modified. For example if you look at the sequelize insert queries, you'll see that they are using something similar to `tuples`:

```sql
INSERT INTO "task" ("id","created_at","updated_at","name","status") VALUES (DEFAULT,'2018-10-23 13:58:05.380 +00:00','2018-10-23 13:58:05.380 +00:00','First task',1) RETURNING *
```

## Accessing Tuple Values

Accessing values in tuples is performed the same way we access items in a list:

```py
my_tup = (1,2,3,4)
print(my_tup[1]) # Returns 2
print(my_tup[1:4]) # Returns 2,3
```

We can also iterate through tuples:

```py
my_tup = ('Hello', 'World')

for word in my_tup:
    print(word) # Prinst Hello, World
```

## Tuple Methods

Python has the ability to read tuple values:

- Finding Tuples Max Value:
  - ```py
      tup = (1,2,3)
      max(tup) # Returns 3
    ```
- Finding Tuples Min Value:
  - ```py
      tup = (1,34,21)
      min(tup) # returns 1
    ```
- Converting Lists Into Tuples:
  - ```py
      my_list = [1,2,3,4]
      new_tup = tuple(my_list)
    ```
- Deleting Tuples:
  - ```py
      my_tup = (1,2,3,4)
      del my_tup
      print(my_tup) # my_tup is undefined
    ```

## You Do

Follow the directions in `main.py`, test your code with `python3 tuple_test.py`.
