"""
 public static boolean isPalindrome(int x) {
        // Convert the integer to a string and split it into an array of characters
        String str = Integer.toString(x);
        char[] charArray = str.toCharArray();
        // Initialize pointers to the start and end of the array
        int start = 0;
        int end = charArray.length - 1;
        // Compare the characters at the start and end of the array
        while (start < end) {
            if (charArray[start] != charArray[end]) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
}
"""


def is_palindrome(x) -> bool:
    # char_array = str(x)
    start = 0
    end = len(x) - 1
    while start < end:
        if x[start] != x[end]:
            return False
        start += 1
        end -= 1
    return True


num = input("Enter some numbers or words to check if ita a palindrome: ")
print(is_palindrome(num))
