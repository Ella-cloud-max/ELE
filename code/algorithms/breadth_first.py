from .depth_first import DepthFirst

class BreadthFirst(DepthFirst):
    def get_next_state(self):
        return self.states.pop(0)