# NAME: DAREY LEE
# ASSIGNMENT 1

# Consulted Peter Nielson for assistance
# Consulted stackoverflow.com for assistance (https://stackoverflow.com/questions/8611712/
                                        #what-does-objects-init-method-do-in-python)
# Consulted tutorialspoint.com for assistance (https://www.tutorialspoint.com/python/python_tuples.htm)

from __future__ import print_function
import unittest

''' when run with "-m unittest", the following produces:
    FAILED (failures=9, errors=2)
    your task is to fix the failing tests by implementing the necessary
    methods. '''


class LinkedList(object):
    class Node(object):
        # pylint: disable=too-few-public-methods
        ''' no need for get or set, we only access the values inside the
            LinkedList class. and really: never have setters. '''

        def __init__(self, value, next_node):
            self.value = value
            self.next_node = next_node

    def __init__(self, initial=None):
        self.front = self.back = self.current = None

        if type(initial) is tuple:

            if type(initial[0]) is str:
                for i in range(0, len(initial), 1):
                    self.push_front(initial[i])

            else:
                for i in range(0, len(initial), 1):
                    self.push_back(initial[i])

        elif type(initial) is int:
            self.push_front(initial)

    def empty(self):
        return self.front == self.back == None

    def __iter__(self):
        self.current = self.front

        return self

    def __next__(self):
        if self.current:
            tmp = self.current.value
            self.current = self.current.next_node
            return tmp

        else:
            raise StopIteration()

    def push_front(self, value):
        new = self.Node(value, self.front)

        if self.empty():
            self.front = self.back = new

        else:
            self.front = new

    ''' you need to(at least) implement the following three methods'''

    def pop_front(self):
        try:
            num = self.front.value
        except AttributeError:
            raise RuntimeError

        if self.empty():
            return None

        elif self.front == self.back:
            self.front = self.back = None
            return num

        else:
            self.front = self.front.next_node
            return num

    def push_back(self, value):
        new = self.Node(value, self.front)

        if self.empty():
            self.back = self.front = new

        else:
            self.front = new
            self.__iter__()
            temp = new.value

            while self.current.next_node is not None:
                self.current.value = self.current.next_node.value
                self.current.next_node.value = temp
                self.current = self.current.next_node

    def pop_back(self):
        try:
            num = self.back.value
        except AttributeError:
            raise RuntimeError

        if self.empty():
            return None

        elif self.front == self.back:
            self.front = self.back = None
            return num

        else:
            last = self.current = self.front

            while last.next_node.next_node is not None:
                self.current = self.current.next_node
                last = self.current

            last.next_node = None
            self.back = self.current
            return num

    def __str__(self):
        x = ""
        self.__iter__()

        while self.current is not None:
            x = x + str(self.current.value)
            if self.current.next_node is not None:
                x = x + ", "
            self.current = self.current.next_node

        return x

    def __repr__(self):
        x = ""
        self.__iter__()

        while self.current is not None:
            x = x + str(self.current.value)
            if self.current.next_node is not None:
                x = x + ", "
            self.current = self.current.next_node

        return 'LinkedList(({}))'.format(x)

    def num_elements(self):
        count = 0
        self.__iter__()

        while self.current is not None:
            count += 1
            self.current = self.current.next_node

        return count

    def delete_value(self, value):
        self.__iter__()
        counter = 0

        while self.current is not None:
            if self.current.value == value:
                counter += 1
            self.current = self.current.next_node

        self.__iter__()

        while self.current is not None:
            marker = self.current

            if self.current.value == value:
                while marker.value == value and marker.next_node is not None:
                    marker = marker.next_node
                self.current.value = marker.value
                marker.value = value

            self.current = self.current.next_node

        for i in range(counter):
            self.pop_back()

    def order_up(self):
        self.__iter__()

        while self.current is not None:
            marker = self.current

            while marker is not None:
                if self.current.value > marker.value:
                    temp = self.current.value
                    self.current.value = marker.value
                    marker.value = temp
                marker = marker.next_node

            self.current = self.current.next_node

    def middle_element(self):
        #self.current = marker = self.front
        self.__iter__()
        marker = self.current
        counter = 0

        while self.current.next_node is not None:
            self.current = self.current.next_node
            counter += 1

            if counter % 2 == 0:
                marker = marker.next_node

        if counter % 2 == 0:
            return marker.value

        else:
            return marker.value, marker.next_node.value

''' C-level work '''


class TestEmpty(unittest.TestCase):
    def test(self):
        self.assertTrue(LinkedList().empty())


class TestPushFrontPopBack(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_back(), 1)
        self.assertEqual(linked_list.pop_back(), 2)
        self.assertEqual(linked_list.pop_back(), 3)
        self.assertTrue(linked_list.empty())


class TestPushFrontPopFront(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        self.assertEqual(linked_list.pop_front(), 3)
        self.assertEqual(linked_list.pop_front(), 2)
        self.assertEqual(linked_list.pop_front(), 1)
        self.assertTrue(linked_list.empty())


class TestPushBackPopFront(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_front(), 1)
        self.assertEqual(linked_list.pop_front(), 2)
        self.assertEqual(linked_list.pop_front(), 3)
        self.assertTrue(linked_list.empty())


class TestPushBackPopBack(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_back(1)
        linked_list.push_back("foo")
        linked_list.push_back([3, 2, 1])
        self.assertFalse(linked_list.empty())
        self.assertEqual(linked_list.pop_back(), [3, 2, 1])
        self.assertEqual(linked_list.pop_back(), "foo")
        self.assertEqual(linked_list.pop_back(), 1)
        self.assertTrue(linked_list.empty())


''' B-level work '''


class TestInitialization(unittest.TestCase):
    def test(self):
        linked_list = LinkedList(("one", 2, 3.141592))
        self.assertEqual(linked_list.pop_back(), "one")
        self.assertEqual(linked_list.pop_back(), 2)
        self.assertEqual(linked_list.pop_back(), 3.141592)


class TestStr(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 2, 3))
        self.assertEqual(linked_list.__str__(), '1, 2, 3')


''' A-level work '''


class TestRepr(unittest.TestCase):
    def test(self):
        linked_list = LinkedList((1, 2, 3))
        self.assertEqual(linked_list.__repr__(), 'LinkedList((1, 2, 3))')


class TestErrors(unittest.TestCase):
    def test_pop_front_empty(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_front())

    def test_pop_back_empty(self):
        self.assertRaises(RuntimeError, lambda: LinkedList().pop_back())

''' write some more test cases. '''

#ADDITIONAL TEST CASES

class TestNumberOfElements(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_front(5)
        linked_list.push_front(4)
        linked_list.push_front(3)
        linked_list.push_front(2)
        linked_list.push_front(1)
        self.assertEqual(linked_list.__str__(), '1, 2, 3, 4, 5')
        self.assertEqual(linked_list.num_elements(), 5)

class TestAscendingOrder(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_front(1)
        linked_list.push_front(5)
        linked_list.push_front(3)
        linked_list.push_front(2)
        linked_list.push_front(4)
        self.assertEqual(linked_list.__str__(), '4, 2, 3, 5, 1')
        linked_list.order_up()
        self.assertEqual(linked_list.__str__(), '1, 2, 3, 4, 5')


''' extra credit.
    - write test cases for and implement a delete(value) method.
    - write test cases for and implement a method that finds the middle
      element with only a single traversal.
'''
#EXTRA CREDIT

class TestDeleteNodesWithValue(unittest.TestCase):
    def test(self):
        linked_list = LinkedList()
        linked_list.push_front(2)
        linked_list.push_front(2)
        linked_list.push_front(3)
        linked_list.push_front(2)
        linked_list.push_front(2)
        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(2)
        linked_list.delete_value(2)
        self.assertEqual(linked_list.__str__(), '1, 3')

class TestMiddleElements(unittest.TestCase):
    def test(self):
        linked_list = LinkedList(2)
        self.assertEqual(linked_list.middle_element(), 2)
        linked_list = LinkedList((1, 2, 3, 4, 5, 6, 7))
        self.assertEqual(linked_list.middle_element(), 4)
        linked_list = LinkedList((1, 2, 3, 4, 5, 6))
        self.assertEqual(linked_list.middle_element(), (3, 4))


''' the following is a demonstration that uses our data structure as a
    stack'''


def fact(number):
    '''"Pretend" to do recursion via a stack and iteration'''

    if number < 0:
        raise ValueError("Less than zero")
    if number == 0 or number == 1:
        return 1

    stack = LinkedList()
    while number > 1:
        stack.push_front(number)
        number -= 1

    result = 1
    while not stack.empty():
        result *= stack.pop_front()

    return result


class TestFactorial(unittest.TestCase):
    def test_less_than_zero(self):
        self.assertRaises(ValueError, lambda: fact(-1))

    def test_zero(self):
        self.assertEqual(fact(0), 1)

    def test_one(self):
        self.assertEqual(fact(1), 1)

    def test_two(self):
        self.assertEqual(fact(2), 2)

    def test_10(self):
        self.assertEqual(fact(10), 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)


if '__main__' == __name__:
    unittest.main()