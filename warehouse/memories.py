import random
from collections import deque
from abc import abstractmethod


class Memory:
    """
    Memory abstract class
    """
    _counter = 0

    @property
    def counter(self):
        return self._counter

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def append(self, element):
        pass

    @abstractmethod
    def sample(self, n, or_less):
        pass


class ExperienceReplayMemory(Memory):
    """
    A cyclic Experience Replay memory buffer
    """
    memory: deque = None

    def __init__(self, size, seed=None):
        """
        Create a new Experience Replay Memory
        :param size: memory size
        :param seed: random seed to be used (will override random.seed)
        """
        super(ExperienceReplayMemory, self).__init__()
        self.memory = deque(maxlen=size)
        if seed is not None:
            random.seed(seed)

    def __len__(self):
        return len(self.memory)

    def append(self, element):
        self.memory.append(element)
        self._counter += 1

    def sample(self, n, or_less=False):
        if or_less and n > self._counter:
            n = self._counter
        return random.sample(self.memory, n)