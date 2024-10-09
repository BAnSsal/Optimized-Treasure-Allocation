from straw_hat import StrawHatTreasury
from treasure import Treasure
import time

def run_test_case(n):
    # Initialize StrawHatTreasury with m crewmates
    m = 1
    size = 3*n+30
    # Initialize the StrawHatTreasury
    treasury = StrawHatTreasury(m)
    t=1
    # Single loop: from 1 to n
    for i in range(1, 31):
        # Add treasure with size, id, and arrival time
            treasury.add_treasure(Treasure(id=i, size=size, arrival_time=i+t))
            size-=1
            if(i%3==0):
                t=t+1

            
    size-=10
    treasure1=treasury.get_completion_time()
    for treasure in treasure1:
        print(f"Completion Time: {treasure.completion_time} time+size: {treasure.size+treasure.arrival_time}")
    for i in range(31, 34):     
        treasury.add_treasure(Treasure(id=i, size=size, arrival_time=i+t))
        size-=1
    print("treasure2")
    treasure2=treasury.get_completion_time()
    for treasure in treasure2:
        print(f"Completion Time: {treasure.completion_time} time+size: {treasure.size+treasure.arrival_time}")
            #27147.0
    
    for i in range(34, 37):     
        treasury.add_treasure(Treasure(id=i, size=size, arrival_time=i+20000-50))
        print(size+i+20000-50)
        size-=1
        
            #27147.0
    treasure3=treasury.get_completion_time()
    # Get completion times after adding all treasures
    

    print("treasure3 ")
    for treasure in treasure3:
        print(f"Completion Time: {treasure.completion_time} time+size: {treasure.size+treasure.arrival_time}")
        if(treasure.size+treasure.arrival_time > treasure.completion_time):
            print("ERROR")
            exit(1)
    # Return the treasury instance for inspection (if needed)
    return treasury.get_completion_time()


def main():
    # Test with different values of n

        # Run the test case
    completed_treasures=run_test_case(1e3)
    print("COMPLETED")


if __name__ == "__main__":
    main()
