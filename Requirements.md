# Requirements #

## Aims ##
## System overview ##

### User classes ###

This section presents a use case analysis of the website. The use cases presented here model the interaction between users and the website. These use cases will be used to guide usability, to provide a task-oriented documentation system.

There will be 2 user classes:
  * **Visitor** - end users of the system;
  * **Administrator** - techy, but not much

#### Visitor ####
Visitors are the **end-users** of the website. They could be either new students who are not used to the University’s campus yet, or anyone else who can’t find their way through the complex system of hallways and rooms which is the Boyd Orr Building.

_"I’m a level 2 CS student and I can’t find my way to the lab. All I know is I should be in the «Level 2 lab in the Boyd Orr». Now, I’ve managed to find the **floor**, but I’m not sure which room I need to go to. Oh, look! There’s a room directory up on the wall, but it’s not very helpful. I sure wish there was an app for this, lol!"_

His goal is to find information regarding a particular room (e.g.: what floor it is on, where exactly it is on that floor, etc). He might know the room number or some other unofficial name for that room.

They can ask the application about different rooms in the BOB. If that room name exists, the app shows an image with the appropriate floor plan and the searched room is highlighted.

#### Administrator ####
Someone needs to manage all that data, so there will be an administrator. He is responsible for maintaining the database (room labels, floor plans).

### User matrix ###
| **Functionality**     | **Visitor** | **Administrator** |
|:----------------------|:------------|:------------------|
| Browse directory      |  X          |  X                |
| Search for a room     |  X          |  X                |
| Post comment          |  X          |  X                |
| Send feedback         |  X          |  X                |
| Edit/Delete Comment   |             |  X                |
| Add/edit floor        |             |  X                |
| Add/edit room         |             |  X                |
| Add/edit floor plan   |             |  X                |