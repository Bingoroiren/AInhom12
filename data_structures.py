
from __future__ import annotations
from typing import TypeVar, Generic, List, Deque, Optional

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self.container  # not is true for empty container

    def push(self, item: T) -> None:
        self.container.append(item)

    def pop(self) -> T:
        return self.container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self.container)


class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]
    # work backwards from end to front
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.container: Deque[T] = Deque()

    @property
    def empty(self) -> bool:
        return not self.container  # not is true for empty container

    def push(self, item: T) -> None:
        self.container.append(item)

    def pop(self) -> T:
        return self.container.popleft()  # FIFO

    def __repr__(self) -> str:
        return repr(self.container)