1.  create a table that will save the bookmark from the user , what ever the type of the
    content it is should save it against the id , I had doubt of the data retrieval that if
    i keep calling all the bookmarks realted to user against the id it would take lot of time but in sql it log(n) time based on hashing , so I can have a table against which in any order and then use the to call it after some time I will store all the revelant data in Redis for easer hasing
    i

DB schema

1. put logic layer / repo layer afterwards
   2.in bookmark table, tags = Column(ARRAY(String), nullable=False), Might be better to use nullable=True with a default empty list in Python/repository layer.
