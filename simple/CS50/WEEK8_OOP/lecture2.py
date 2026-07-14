import random

"""
On lecture 1, we dealt with individual objects. This one however deals with a 
singular entity which is a Hat. We cant do hat1 = Hat(), hat2 = Hat() with this 

@classmethod = A decorator that tells Python: "
You can run this method directly using the Class name (Hat.sort()) 
without needing to create an object first!"
"""
class Hat:
    # This variable belongs to the WHOLE class, not one specific hat.
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

        """By writing cls.houses, you are explicitly telling Python: 
        "Don't bother looking for a local variable. 
        Go straight to the Class itself (cls), 
        and grab the houses list attached to it."""

Hat.sort("Harry")