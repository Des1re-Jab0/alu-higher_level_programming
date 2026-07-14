#!/usr/bin/python3
"""Module that defines a Node and a SinglyLinkedList class."""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data: the integer stored in the node.
            next_node: the next node in the list, or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data stored in this node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of this node after validating it.

        Args:
            value: the new integer to store.

        Raises:
            TypeError: if value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node of the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node after validating it.

        Args:
            value: the next Node object, or None.

        Raises:
            TypeError: if value is not a Node object nor None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list kept in increasing order."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node at the correct sorted position.

        Args:
            value: the integer to insert into the list.
        """
        new = Node(value)
        if self.__head is None or self.__head.data >= value:
            new.next_node = self.__head
            self.__head = new
            return
        current = self.__head
        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new

    def __str__(self):
        """Return the whole list as a string, one number per line."""
        numbers = []
        current = self.__head
        while current is not None:
            numbers.append(str(current.data))
            current = current.next_node
        return "\n".join(numbers)
