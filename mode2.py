from island import Island
from data_structures.heap import MaxHeap

class Mode2Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, n_pirates: int) -> None:
        """
        Worst case: O( 1 )
        Best Case: O( 1 )

        datastructure:
        Maxheap

        example:
        if we create this class, we get a max heap.

        complexity reasoning:
        we only initialise 3 things.
        """
        self.Num_Pirates = n_pirates
        self.Islands = MaxHeap(0)
        self.Key = 0

    def add_islands(self, islands: list[Island]):
        """
        Worst Case: O( N + I )
        Best Case: O( N + I )

        where N is the number of island we have already. 
        where I is the islands being added.

        data structure:
        Max heap was used for this function. the max heap is perfect for this
        scenerio as we need to prioritise elements and pull from the
        data sturcture inorder.

        example: 
        if we have islands:
        [
        'A','B','C',
        ]

        they will be inSersted 'A','B','C' as for now, we dont care about key.

        The function goes through every island given I and adds it to a new heap before 
        going over all the islands N and adding those islands to the new heap as well before 
        saving the new heap. This is because the heap is an array based structure and cant 
        extend its length so we need to create a new heap every time to have enough space.

        complexity reasoning:
        every time this function is called, we insert all the new islands
        and then all the old islands no matter what. therefore, the complexity will always be 
        O( N + I ).
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
        Best Case: O( N + C )
        Worst Case: O( N + C )
        
        Where N is the amount of islands.
        C is the number of pirates and 
        K is the compelxity of get_max()

        Data Structure:
        This function uses a heap as intialised in the setup and alway uses a list 
        as the data structure used to return

        The function will go over every Island and reinsert them with the correct 
        key calculated. Then for every crew member, 
        we get the top element with get_max() and calculate the money and crew sent
        before re inserting.

        Example:
        if we have 3 islands in the heap, then all 3 islands will be reinserted with new 
        heaps and then calcualted over.

        complexity analysis:
        We can have a worst case of O( N + C*log(N) ). We have O( N + C ).
        This is because we only have 2 loops and do 2 things. First we
        reinsert every island with a new updated key making O( N ). 
        Then for every crew member, we get the top element and get the
        crew sent and money earned before reinserting it back into the heap.

        therefore only O( N + C )
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
            


            


