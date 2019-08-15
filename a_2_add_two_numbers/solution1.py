# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def single_list_generate(l: list):
    rootnode = ListNode(0)
    lastnode = rootnode
    # print(id(rootnode))
    # print(id(lastnode))
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
        # print(id(lastnode))
    # print(id(rootnode))
    return rootnode.next


def print_single_list(l: ListNode):
    while l:
        print(l.val, end=' ')
        l = l.next


class Solution:
    @classmethod
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rootnode = ListNode(0)
        lastnode = rootnode
        carry_num = 0
        while carry_num or l1 or l2:
            carry_num, remainder_num = divmod(
                carry_num +
                (l1.val if l1 else 0) +
                (l2.val if l2 else 0), 10)
            lastnode.next = ListNode(remainder_num)
            lastnode = lastnode.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return rootnode.next


if __name__ == '__main__':
    l1 = single_list_generate([1, 2, 3, 4])
    l2 = single_list_generate([99, 55, 33, 12])
    l3 = Solution.addTwoNumbers(l1, l2)
    print_single_list(l3)
