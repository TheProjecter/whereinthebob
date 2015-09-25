# Application architecture #

## N-tier ##
[Data flow diagram](https://cacoo.com/diagrams/lwlcAnup20fD4KM4)

![https://lh6.googleusercontent.com/-qX25Mx6wlZU/TyhkGwsSMaI/AAAAAAAAJqM/TLMP_PNrPS0/s595/n-tier-architecture.png](https://lh6.googleusercontent.com/-qX25Mx6wlZU/TyhkGwsSMaI/AAAAAAAAJqM/TLMP_PNrPS0/s595/n-tier-architecture.png)

The **presentation tier** is the topmost layer of the application, represented by the user interface. It translates user actions into commands for the application and it presents the information retrieved by the app in a way that the user can understand.

**Logic/application tier**

**Data tier**


## Data model ##

### ERD ###
[ERDiagram](https://cacoo.com/diagrams/tcKNzBvkoZxgroTx)

![https://lh5.googleusercontent.com/-VGkahxmu49c/TzFO8G7XCrI/AAAAAAAAJrk/PpbeSPK7KB4/s396/DBDiagram.png](https://lh5.googleusercontent.com/-VGkahxmu49c/TzFO8G7XCrI/AAAAAAAAJrk/PpbeSPK7KB4/s396/DBDiagram.png)


### ERD2 ###
[ERDiagram2](https://cacoo.com/diagrams/8MK4qtW8kNgxZlUr)

![https://cacoo.com/diagrams/8MK4qtW8kNgxZlUr-87ED5.png](https://cacoo.com/diagrams/8MK4qtW8kNgxZlUr-87ED5.png)

### Description ###

#### Floor ####
| **Attribute** | **Type** | **Rationale** |
|:--------------|:---------|:--------------|
| floor\_id     | Integer  | Unique ID to identify each floor |
| description   | String   | A short description of the room used to supply some info and to optimize the search. |
| date\_created | Date     | The floor plan was added to the system |
| date\_updated | Date     | The last modifications occurred |
| level         | Integer  | Used to optimize the search and to reduce the time used to fetch the info |
| rating        | Integer  | Improve the search by popularity |
| GUID          | GENERATED? | Unique ID for the comment |

#### Room ####
| **Attribute** | **Type** | **Rationale** |
|:--------------|:---------|:--------------|
| room\_id      | Integer  | Unique ID to identify each room |
| floor\_id     | Integer  | This is a foreign key to link the room to the floor |
| room\_name    | Integer  | FK referencing table `Name` |
| type          | Integer  | `FK` referencing the table `Room_Type` |
| description   | String   | Info about the room |
| rating        | Integer  | For popularity purposes and to sort the results. |
| GUID          | GENERATED? | Unique ID for the comment |

#### Comment ####
| **Attribute** | **Type** | **Rationale** |
|:--------------|:---------|:--------------|
| GUID          | GENERATED? | Unique ID for the comment |
| Comment       | String   | To content of the comment. |
| Date          | Date     | The comment was posted.|

#### `Room_Type` ####
| **Attribute** | **Type** | **Rationale** |
|:--------------|:---------|:--------------|
| type\_id      | `Integer` | Unique ID     |
| type          | `String` | Type of the room, e.g.: Lab, Lecture Theatre, etc. |

#### `Room_Name` ####
| **Attribute** | **Type** | **Rationale** |
|:--------------|:---------|:--------------|
| room\_id      | `Integer` | FK referencing `Room.room_id` |
| name          | `String` | The name for the room |

### SQL ###