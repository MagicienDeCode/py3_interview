class Solution:
    def checkValidString(self, s: str) -> bool:
        # store s'index
        # declare two stacks
        stack = []
        stars = []
        # * ( * (  False
        # ( * ( *  True
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                # verify stack is empty
                # if empty
                if not stack:
                    # verify is there a star
                    # if there is not star, return F
                    if not stars:
                        return False
                    else: # if a star, pop its index
                        stars.pop()
                else: # not empty pop left ( 'index
                    stack.pop()
            else:
                stars.append(i)
        # verify stars can match left (
        while stack:
            if not stars:
                return False
            # left ( position
            lp = stack.pop()
            # stars' postion
            sp = stars.pop()
            # * ( * (  False
            # ( * ( *  True
            if lp > sp:
                return False

        return True