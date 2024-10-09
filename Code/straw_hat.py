import crewmate
import heap
import treasure
from custom import Bigtr

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''

    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat treasury with m crewmates.
        Time Complexity:
            O(m)
        '''
        # Initialize a heap of m CrewMate objects with load 0 for each crewmate.
        # The heap's comparison function ensures the crewmate with the least load is prioritized.
       
        self.crewmateheap = heap.Heap(self.compare_crewmates, [crewmate.CrewMate() for _ in range(m)])
        self.validcrewmates=[]
        
        
    
    def compare_crewmates(self, crewmate1, crewmate2):
        '''
        Custom comparison function for the heap based on crewmate load.
        Arguments:
            crewmate1, crewmate2 : CrewMate objects to compare
        Returns:
            bool : True if crewmate1's load is less than crewmate2's load, False otherwise
        '''
        return crewmate1.load < crewmate2.load

    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the crewmate with the least load.
        Time Complexity:
            O(log(m)) where m is the number of Crew Mates
        '''
        # Extract the crewmate with the least load from the heap.
        
        tempcrewmate = self.crewmateheap.extract()
        if(tempcrewmate is None):
            return 
        if(tempcrewmate.load == 0):
            self.validcrewmates.append(tempcrewmate)
        # If the crewmate's load is less than or equal to the treasure's arrival time,
        # set the load to arrival_time + treasure size. Otherwise, just add the treasure's size.
        if tempcrewmate.load <= treasure.arrival_time:
            tempcrewmate.load = treasure.arrival_time + treasure.size
        else:
            tempcrewmate.load += treasure.size

        # Add the treasure to the crewmate's list of treasures.
        tempcrewmate.treasures.append(treasure)

        # Insert the updated crewmate back into the heap.
        self.crewmateheap.insert(tempcrewmate)

    
    def get_completion_time(self):
    
    
        answer_array = []

        # Loop through all crewmates in the crewmate heap
        for crewmate in self.validcrewmates:
            # Initialize the big_heap for handling treasures with the custom comparator
            big_heap = heap.Heap(self.compare_bigtreasures, [])
            
            # Check if the crewmate has treasures
            if crewmate.treasures:
                old_time = crewmate.treasures[0].arrival_time
                # Insert the first treasure into the big_heap
                big_heap.insert(Bigtr(crewmate.treasures[0]))

                # Process the rest of the treasures
                for treasure in crewmate.treasures[1:]:
                    # Time difference between new treasure arrival and previous treasure completion
                    new_time = treasure.arrival_time
                    time_lag = new_time - old_time

                    # Process treasures based on the time lag
                    while time_lag > 0 and len(big_heap.heap) > 0:
                        top_bigtr = big_heap.extract()
                        remains = top_bigtr.priority - top_bigtr.mytreasure.arrival_time

                        if remains > time_lag:
                            # If the remains exceed the time lag, update priority and break out
                            top_bigtr.priority -= time_lag
                            big_heap.insert(top_bigtr)
                            time_lag = 0
                        else:
                            # Complete the treasure and adjust the time lag
                            completion_time = remains + old_time
                            fin_tr=top_bigtr.mytreasure
                            fin_tr.completion_time = completion_time
                            answer_array.append(top_bigtr.mytreasure)
                            time_lag -= remains
                            old_time=completion_time

                    # Update old_time for the next treasure
                    old_time = new_time

                    # Insert the new treasure into the big_heap
                    big_heap.insert(Bigtr(treasure))

                # After processing all treasures, process the remaining in the big_heap
                while len(big_heap.heap) > 0:
                    top_bigtr = big_heap.extract()
                    remains=(top_bigtr.priority - top_bigtr.mytreasure.arrival_time)
                    completion_time = old_time + remains
                    fin_treas=top_bigtr.mytreasure
                    fin_treas.completion_time = completion_time
                    answer_array.append(top_bigtr.mytreasure)
                    old_time=completion_time
        answer_array = sorted(answer_array, key=lambda treasure: treasure.id)
        return answer_array
    
    def compare_bigtreasures(self, bigtr1, bigtr2):
        '''
        Custom comparison function for Bigtr objects based on their priority.
        Arguments:
            bigtr1, bigtr2 : Bigtr objects to compare
        Returns:
            bool : True if bigtr1 has a lower priority (i.e., higher priority for extraction)
        '''
        # Compare by priority first
        if bigtr1.priority != bigtr2.priority:
            return bigtr1.priority < bigtr2.priority
        # If priorities are the same, compare by treasure ID (smallest ID has higher priority)
        return bigtr1.mytreasure.id < bigtr2.mytreasure.id

