class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # step 1: store next
            curr.next = prev        # step 2: reverse link
            prev = curr             # step 3: move prev
            curr = next_node        # move curr

        return prev