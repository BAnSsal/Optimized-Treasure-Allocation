from straw_hat import StrawHatTreasury
from treasure import Treasure

def main():
    # Number of crewmates
    num_crewmates = 1

    # Initialize the StrawHat treasury with the given number of crewmates
    treasury = StrawHatTreasury(num_crewmates)

    # List of treasures with strictly increasing arrival times
    treasures = [
        Treasure(id=0, size=4, arrival_time=0),
        Treasure(id=1, size=50, arrival_time=3),
        Treasure(id=2, size=48, arrival_time=4)]

    # Add treasures to the treasury
    for treasure in treasures:
        treasury.add_treasure(treasure)

    # Get the completion times of the treasures
       
    
    completed_treasures = treasury.get_completion_time()
    # Print the treasures and their completion times
    print
    
if __name__ == "__main__":
    main()