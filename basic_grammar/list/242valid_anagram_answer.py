# Initialize an empty string.
my_str = ""

# Verify if str is empty, not "" will return True
print(not my_str)

# Create a list containing 7 elements, all initialized to 0.
my_list = [0]*7

# Print the length of the list 'my_list'.
print(len(my_list))
# Print the contents of the list 'my_list'.
print(my_list)

# Initialize two strings with specific content.
str1 = "Long distance travel (Life) can be boring,"
str2 = "but I'm glad we're doing it together."

# Print the boolean value of the expression 'not str1'.
print(not str1)
# Print the length of the string 'str1'.
print(len(str1))

# Initialize a string 'str3'.
str3 = "Xiang"

# Iterate over each character in 'str3' and print the character along with its Unicode code point.
for i in str3:
    print(i, ord(i))

# Print the character at index 2 in 'str3'.
print(str3[2])
# Print the Unicode code point of the character at index 2 in 'str3'.
print(ord(str3[2]))

# Define a class named Solution.
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		hash_list = [0]*26
		for i in range(len(s)):
			hash_list[ord(s[i])-97] += 1
			hash_list[ord(t[i])-97] -= 1
		for count in hash_list:
			if count != 0:
				return False
		return True