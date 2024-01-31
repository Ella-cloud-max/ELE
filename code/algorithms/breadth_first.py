from .depth_first import DepthFirst
from code.classes.protein import Protein

class BreadthFirst(DepthFirst):
    """
    A Breadth First algorithm that builds a stack of proteins with a unique assignment of amino acids for each instance.
    """
    def get_next_state(self) -> Protein:
        """
        Returns the next state from the queue of states.
        """
        return self.states.pop(0)