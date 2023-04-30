# PreNUTS - A 🥜 project 
## Pre-requisite Network for Universities (and TooPr System)
### Go [here!](http://itsjustmustafa.github.io/PreNUTS)
---
### TooPr:
/ˈtuːpə/ - The opposite of Pre-requisite

eg.

> [48023 : Programming Fundamentals](https://itsjustmustafa.github.io/PreNUTS/?currQuery=Programming%20Fundamentals%2048023) is a Pre-requisite to [48024 : Applications Programming](https://itsjustmustafa.github.io/PreNUTS/?currQuery=Applications%20Programming%2048024).
>
> [48024 : Applications Programming](https://itsjustmustafa.github.io/PreNUTS/?currQuery=Applications%20Programming%2048024) is a TooPr to [48023 : Programming Fundamentals](https://itsjustmustafa.github.io/PreNUTS/?currQuery=Programming%20Fundamentals%2048023).

---

Map out your subject options with PreNUTS!

Currently Supported:
- UTS [(handbook)](http://www.handbook.uts.edu.au/)

---

## Future Features

### Node maping for subjects 
WIP! Will have to update after i do something abt codependencies ect. Also could be cool to be able to make a super graph, with an end class and it lists the begining classes ect(?)

![node graph](nodeGraphs\41012_path.png)
Example for 41012 (Programming for Mechatronic Systems)

### Refined logical relations on Prereqisites
- Capacity for coreqs
- conditional relationships on prerequisite


## Notes/Thoughts/How do uni classes work?
### Antireqs
Is it safe to assume all anti reqs of one subject go both ways?
eg 65212 Chemistry 2 has an anti req of 65022 chem 2a (seems to be old)
Ie if 65022 were still active, and you had done 65212 that it would prohibit you from taking 65022? 

As in:
$\text{class A}  \xleftarrow{\text{anti}}\xrightarrow{\text{requisite}} \text{class B} $

### Co reqs

### the silly subjects
w/out prereqs but have cp limits first (could be shown as a tooltip or smthing?)

## Requirements
Install the requirements with  

```
pip install -r requirements.txt
```