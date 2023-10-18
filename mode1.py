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
        Hold_Island = (0)

        for Island in self.Islands:
            Current_island = Island
            Current_island = Current_island.item

            if Current_Crew_Num >= Current_island.marines:
                Current_Crew_Num -= Current_island.marines
                print(Current_Crew_Num)
                List_Of_Islands.append((Current_island,Current_island.marines))
        
        return List_Of_Islands
            
            

    def select_islands_from_crew_numbers(self, crew_numbers: list[int]) -> list[float]:
        """
        Student-TODO: Best/Worst Case
        """
        raise NotImplementedError()

    def update_island(self, island: Island, new_money: float, new_marines: int) -> None:
        """
        Student-TODO: Best/Worst Case
        """
        raise NotImplementedError()
