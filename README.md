# Char To Int

#### This python module can convert a single character or a string into the ASCII value of that character.

To use it, download the `cti.py` file, make sure it is in the same folder as the project you are working on and write `import cti`

---

#### Functions

`cti.example()` takes nothing; will show the basic functions you can do

`cti.single()` takes a string of one character; if given more it will give 0, and if given less it will give you an error. It will return an integer

`cti.multi()` takes a string of any amount and a boolean. It will return a list (array) if the boolean is `False`, and a more readable string if ` True`

`cti.prtMulti()` takes a string of any amount. It will return a list (array) and print a more readable string to the console.

Neither function takes more than one argument, so any mutilation of the string will have to be done manually.

Note that any characters given for either function that isn't part of the alphabet (or space) will return as 0 (for single) or a blank list (for multi).
For multi, if one such character is mixed in with other characters that do work, these characters will simply not appear, whilst the others (that do work) will.

---

##### For Future Releases
 - [X] Add function to print and assign variable
 - [X] Fix problem with data amount being limited
 - [ ] Add more data
 - [ ] Make a ascii value to binary converter
    - [ ] Make a way to convert the characters straight to binary
