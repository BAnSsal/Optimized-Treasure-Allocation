
---

# Optimized Treasure Allocation

## Approach

In this project, I implemented a treasure management system for the Straw Hat pirates using a scheduling algorithm. The approach ensures efficient handling of treasures by distributing the workload among crewmates based on their current load and processing treasures according to a priority system.

### Treasure Allocation

The key idea for treasure allocation is to assign each new treasure to the crewmate who will finish their current tasks the soonest, which corresponds to the crewmate with the least current load. The load on a crewmate is defined as the total remaining size of all treasures assigned to them.

This can be interpreted as allocating a treasure to the person who will be free first. By continuously assigning treasures to the least loaded crewmate, we balance the workload across the team.

### Treasure Processing

Each crewmate processes one treasure at a time. The treasure is selected based on a priority function:

\[
Priority(j) = (Wait \, Time(j) - Remaining \, Size(j))
\]

Where:
- `Wait Time(j) = t − arrival_j`, which is the time a treasure has been waiting to be processed.
- `Remaining Size(j)` is the unprocessed portion of the treasure.

Thus, the priority is effectively:

\[
Priority = t - arrival_j - Remaining \, Size(j)
\]

Since the current time `t` affects all treasures equally in a relative sense, it is excluded from the actual priority computation. The priority is computed as `arrival_time + remaining_size`, and a min-heap is used to manage the treasures based on this priority.

### Heap Structure

I implemented a custom min-heap that is capable of handling the treasure assignments and scheduling. The heap ensures that treasures with the lowest `arrival_time + remaining_size` are processed first. 

As treasures are processed, their remaining sizes are reduced, and once a treasure is completed, it is removed from the heap, and the next treasure in line is processed. If multiple treasures have the same priority, the treasure with the lower `id` is processed first.

### Time Complexity Analysis

The overall time complexity is driven by two key operations:

1. **Heap Operations**:
    - Inserting a treasure into the min-heap has a time complexity of `O(log n)` where `n` is the number of treasures.
    - Extracting the treasure with the highest priority (lowest `arrival_time + remaining_size`) also takes `O(log n)` time.
    - Since each treasure is inserted and extracted once, the heap operations collectively have a time complexity of `O(n log n)`.

2. **Crewmate Selection**:
    - Assigning a new treasure to the crewmate with the least load is done in `O(log m)`, where `m` is the number of crewmates. This is managed by a secondary heap that tracks the load of each crewmate.

Thus, the overall time complexity of the solution is `O(n log n + n log m)` where:
- `n` is the number of treasures.
- `m` is the number of crewmates.

This approach ensures that both treasure allocation and processing are handled efficiently, even for large inputs.

