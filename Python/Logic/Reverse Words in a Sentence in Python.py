def reverse_words_manual(sentence):
    words = sentence.split()
    print(words)
    left = 0
    right = len(words) - 1
    print(right);

    while left < right:
        print("right=",right)
        print("left=",left)
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
        print("words=",words)
        print("right=",right)
        print("left=",left)

    return " ".join(words)


print(reverse_words_manual("   I love   Python  india "))