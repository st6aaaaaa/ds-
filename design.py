'''You are given two integer arrays persons and times. In an election,
the ith vote was cast for persons[i] at time times[i].
For each query at a time t, find the person that was leading
the election at time t. Votes cast at time t will count towards our query. In the case of a tie,
the most recent vote (among tied candidates) wins.
Implement the TopVotedCandidate class:
TopVotedCandidate(int[] persons, int[] times) Initializes the object
with the persons and times arrays. int q(int t) Returns the number of the person that was
leading the election at time t according to the mentioned rules'''


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.array = []
        cnt = Counter()
        m = 0
        lead = None
        for p, t in zip(persons, times):
            cnt[p] += 1
            c = cnt[p]
            if c >= m:
                if p != lead:
                    lead = p
                    self.array.append([p, t])
                m = c

    def q(self, t: int) -> int:
        ans = self.func(self.array, t)
        return ans

    @staticmethod
    def func(array, t):
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = low + (-low + high) // 2
            if array[mid][1] == t:
                return array[mid][0]
            elif array[mid][1] < t:
                low = mid + 1
            else:
                high = mid - 1
        return array[high][0]

'''Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a normal queue 
(push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.'''


class MyQueue:

    def __init__(self):
        self.size = 0
        self.array = []

    def push(self, x: int) -> None:
        self.size += 1
        self.array.append(x)

    def pop(self) -> int:
        if self.size == 0:
            return None
        self.size -= 1
        return self.array.pop(0)

    def peek(self) -> int:
        if self.size == 0:
            return None
        return self.array[0]

    def empty(self) -> bool:
        return self.size == 0