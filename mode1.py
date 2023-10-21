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
        Student-TODO: Best/Worst Case
        """

        self.Islands = BinarySearchTree()

        for Island in islands:
            Current_island = Island

            Key = (min(Current_island.money * crew / Current_island.marines, Current_island.money)*-1,Current_island.name)
            
            self.Islands[Key] = Island
        

        self.crew = crew 

    def select_islands(self) -> list[tuple[Island, int]]:
        """
        Student-TODO: Best/Worst Case
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
        Student-TODO: Best/Worst Case
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
        Student-TODO: Best/Worst Case
        """
        Island = island
        Island.money = new_money
        Island.marines = new_marines


