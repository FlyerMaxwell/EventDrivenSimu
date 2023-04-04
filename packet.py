class Packet:
    """
    Represents a pkt
    """
    def __init__(self, clock, src, dst, data) -> None:
        self.timestamp = clock
        self.src = src
        self.dst = dst
        self.data = data
        
    def __lt__(self,other):
        return self.timestamp < other.timestamp
