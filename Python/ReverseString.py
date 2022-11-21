def reverseString(s):
    right = len(s) - 1
    left = 0
    while (right > left):
        temp = s[right]
        s[right] = s[left]
        s[left] = temp
        right -= 1
        left += 1

if __name__ == "__main__":
    
    s = ["h","e","l","l","o"]
    s = reverseString(s)
    
    