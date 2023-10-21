from island import Island
from data_structures.heap import MaxHeap

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        self.Num_Pirates = n_pirates
        self.Islands = MaxHeap(0)
        self.Key = 0

    def add_islands(self, islands: list[Island]):
        """
        Student-TODO: Best/Worst Case
        """

        NewHeap = MaxHeap(self.Islands.length + len(islands))

        while self.Islands.length != 0:

            NewHeap.add(self.Islands.get_max())
        
        self.Islands = NewHeap

        for Islands in islands:

            self.Key += 1
           
            self.Islands.add(((self.Key,Islands.name),Islands))
            

    def simulate_day(self, crew: int) -> list[tuple[Island|None, int]]:
        """
        Student-TODO: Best/Worst Case
        """
        
        NewHeap = MaxHeap(self.Islands.length)
        Tuple_List = []


        while self.Islands.length != 0:

            Islands = self.Islands.get_max()[1]
            try:
                Received = min(Islands.money, Islands.money * crew / Islands.marines)

                if Islands.marines >= crew:
                    Key = Received
                else:
                    Key = 2 * (crew - Islands.marines) + Received

                NewHeap.add(((Key,Islands.name),Islands))
            except:
                Key = 0
                NewHeap.add(((Key,Islands.name),Islands))
        
        self.Islands = NewHeap

        for i in range(0,self.Num_Pirates):
            Islands = self.Islands.get_max()[1]

            
            Money = Islands.money
            Marines = Islands.marines
            Name = Islands.name
            
            if Islands.money == 0:
                Tuple_List.append((None,0))
            else:

                Crew_Number = crew
                Money_Taken = min(Islands.money, Islands.money * crew / Islands.marines)

                Islands.money -= Money_Taken

                if Islands.marines > Crew_Number:
                    Crew_Number = 0
                    Tuple_List.append((Island(Name,Money,Marines),crew-Crew_Number))
                    Islands.marines -= crew
                    Key = min(Islands.money, Islands.money * crew / Islands.marines)
                else:
                    Crew_Number -= Islands.marines
                    Tuple_List.append((Island(Name,Money,Marines),crew-Crew_Number))
                    Islands.marines = 0
                    Key = 0

                self.Islands.add(((Key,Islands.name),Islands))
        
        return Tuple_List
            


            


