# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [-1, -1]
        min_distance = float("inf")

        previous_node = head
        current_node = head.next
        current_ind = 1
        previous_crit_ind = 0
        first_crit_ind = 0

        while current_node.next is not None:
            if (current_node.val < previous_node.val and current_node.val < current_node.next.val) or (current_node.val > previous_node.val and current_node.val > current_node.next.val):
                if previous_crit_ind == 0:
                    previous_crit_ind = current_ind
                    first_crit_ind = current_ind
                else:
                    min_distance = min(min_distance, current_ind - previous_crit_ind)
                    previous_crit_ind = current_ind

            current_ind += 1
            previous_node = current_node
            current_node = current_node.next

        if min_distance != float("inf"):
            max_distance = previous_crit_ind - first_crit_ind
            result = [min_distance, max_distance]

        return result