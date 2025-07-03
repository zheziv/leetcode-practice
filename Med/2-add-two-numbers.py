class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lt1 = self.reverse_list(l1)
        lt2 = self.reverse_list(l2)
        # You cannot directly map str over linked list like this.
        # You need to traverse the list and collect the digits into a list.
        num1 = int(''.join(map(str, self.linked_list_to_list(lt1))))
        num2 = int(''.join(map(str, self.linked_list_to_list(lt2))))
        total = num1 + num2
        result_list = [int(d) for d in str(total)]
        return self.list_to_linked_list(result_list)  # Reverse for correct order if needed like result_list[::-1].

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    def linked_list_to_list(self, head: Optional[ListNode]) -> list:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums
    
    def list_to_linked_list(self, nums: list) -> Optional[ListNode]:
        head = None
        for num in nums:
            node = ListNode(num)
            node.next = head
            head = node
        return head
