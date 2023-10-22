from island import Island
from data_structures.heap import MaxHeap
from data_structures.bst import BinarySearchTree
from data_structures.node import TreeNode

class Mode1Navigator:
    """
    Student-TODO: short paragraph as per https://edstem.org/au/courses/12108/lessons/42810/slides/294117
    """

    def __init__(self, islands: list[Island], crew: int) -> None:
        """
        Worst Case O( N * comp )
        Best Case: O( N * comp )
        where N is the number of islands given in island.

        Data Structure:
        The data structure used in the function was a binary tree.
        This was, firstly, because the assignment outlined that the
        best and worst case of using the class function would be 
        O( LogN ) and O( N ) which indicates a balanced and unbalanced
        tree. Moreover, The BST is very cheap to serach for something
        compared to other data structures.

        The intialisation works by going over every island from the
        list given and putting it through a formula to find its designated key.
        Then it is inserted into a binary tree.

        Example:
        For example, if we had 3 islands ['a', 100, 300] ['b', 200, 200] ['c' 300, 200,]
        it would be saved onto the BST in the order of 'c','b','a'.

        Complexity Reasoning:
        We needed a worst Case of O( N(LogN) ). The complexity of the code is 
        O( N * comp ). This is because when going over N islands, we make 
        a comparison to determine where the element should be placed which comes out
        to O( Comp ) + O( 1 ) as shown in week 10. However getting rid of the O( 1 ),
        we end up with O( N * comp )
        """

        self.Islands = BinarySearchTree()

        for Island in islands:
            Current_island = Island

            Key = (min(Current_island.money * crew / Current_island.marines, Current_island.money)*-1,Current_island.name)
            
            self.Islands[Key] = Island
        

        self.crew = crew 

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Worst Case: O( N )
        Best Case: O( N )
        
        where N is the number of elements in the BST.

        Data Structure:
        The data structure, as implemented in initialisation, was
        a BST with hints of a priority sort. This is because all the
        elements in the BST are ordered from the top priority or the
        element to be selected first, to the least.

        The function works by first creating the list of tuples that 
        will be returned. Then we go over every island in the BST to ensure that 
        we are only sending crew members to the top most priorirty islands.

        for every island welook at, the number of crew to be sent
        is decided. unless we dont have enough crew, we send all the ones we need.
        however if we dont have enough, then we iterate through the list and find the 
        island that would give us the most money.

        Example:
        for example if we had 200 crew memebers and the sorted BST of:
        
        [ Island("A", 400, 100)
        Island("D", 350, 90)
        Island("E", 300, 100)
        Island("B", 300, 150)
        Island("C", 100, 5) ]

        the function will send 100 to the first island, 90 to the second island and then serach for 
        the next best island to send to.

        Complexity reasoning:
        The best and worst cases need to be O( N ) and O( LogN ). However the best and worst cases
        of the function is both O( N ). This is because no matter what, the function will always 
        look at every element to ensure that the best islands are found.
        """

        Current_Crew_Num = self.crew
        List_Of_Islands = []
        Hold_Island = None
        Hold_Money = 0

        for Island in self.Islands:
            Current_island = Island
            Current_island = Current_island.item

            if Current_Crew_Num >= Current_island.marines:
                Current_Crew_Num -= Current_island.marines

                List_Of_Islands.append((Current_island,Current_island.marines))
            
            elif Current_Crew_Num < Current_island.marines:
                
                Current_Money = Current_island.money * Current_Crew_Num / Current_island.marines
                
                if Current_Money > Hold_Money:
                    Hold_Island = Current_island
                
        if Hold_Island is not None:
            List_Of_Islands.append((Hold_Island,Current_Crew_Num))


        return List_Of_Islands
            
            

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Worst Case: O( C * N )
        Best Case: O( C * N )
        
        Where C is the number of elements in crew_numbers
        and N is the number of elements in the BST.

        Data structure:
        There are 2 datastructures used in the function, A BST containing all the
        islands and a list containing all the crew numbers. 

        For every crew number, we essentially rerun the select_islands(self) however 
        instead of only running it 1 time, we run it C times where C is the 
        number of elements in crew_numbers. We go in order of the top priority to the
        least and send crew members accordingly.

        Example:
        if we had the crew members [ 200, 500, 5] for a sorted BST:
        
        [ Island("A", 400, 100)
        Island("D", 350, 90)
        Island("E", 300, 100)
        Island("B", 300, 150)
        Island("C", 100, 5) ]

        we would end up with [865, 1450, 100]

        Complexity Reasoning:
        We needed to have a worst case of O( C * N ). the worst case for the function is 
        O( C * N ) as for every crew member C, we go over every island N making it C * N.

        """
        counter = 0
        Crew_Numbers = crew_numbers
        Money_List = []

        for Number in crew_numbers:
            counter += 1
            Current_Crew_Num = Number
            Total_Money = 0
            Hold_Island = None
            Hold_Money = 0

            for Island in self.Islands:
                Current_island = Island
                Current_island = Current_island.item
                if Current_Crew_Num >= Current_island.marines:
                    Current_Crew_Num -= Current_island.marines

                    Total_Money += Current_island.money
                
                elif Current_Crew_Num < Current_island.marines:
                    
                    Current_Money = Current_island.money * Current_Crew_Num / Current_island.marines
                    
                    if Current_Money > Hold_Money:

                        Hold_Island = Current_island
                        Hold_Money = Current_Money


            if Hold_Island is not None:
                Total_Money += min(Hold_Island.money * Current_Crew_Num / Hold_Island.marines, Hold_Island.money)
            

            Money_List.append(Total_Money)
        
        return Money_List


    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Worst case: O(1)
        Best Case: O(1)

        data structure:
        none

        example:
        if we update island1 with new money and marines,
        then it will be updated.

        complexity reasoning:
        because we change an object, everything that
        refers to that object will be effected as well.
        """
        Island = island
        Island.money = new_money
        Island.marines = new_marines


