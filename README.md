# PreNUTS - A 🥜 project 
## Pre-requisite Network for Universities (and TooPr System)
### Go [here!](http://itsjustmustafa.github.io/PreNUTS) for the stable version
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

In general, prereqs tend to be OR first then AND in terms of logic

ie 41012 as pictured above has listed preReqs like this
> Requisite(s): (48623 Mechatronics 2 OR (48622 Embedded Mechatronics Systems AND (41039 Programming 1 OR 48430 Fundamentals of C Programming OR 37171 Introduction to Programming OR 48221 Engineering Computations OR 48023 Programming Fundamentals)))

so a more appropriate diagram would look like this
![node graph](nodeGraphs\41012_boolean.jpg)

## Notes/Thoughts/How do uni classes work?
### Antireqs
From my understanding, antireqs aren't reciprocal, ie:
$A \xrightarrow{\text{antiReq}} B $

### Co reqs 
Also not reciprocal

$A \xrightarrow{\text{coReq}} B \text{ doesn't imply }  B \xrightarrow{\text{coReq}} A$


### The silly subjects
This is what i'm calling subjects that don't have preReqs but have other course requirements (ie, cp limits). Haven't implemented yet

## Requirements
Install the requirements[^1] with  
[^1]: not sure i have them all, or that they're all required but just run the code and see what breaks then install that
```
pip install -r requirements.txt
```