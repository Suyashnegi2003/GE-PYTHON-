def main():
    text = input('Enter a sentence:')
    freq = {}
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print("Frequency of each letter are as follows:", freq)
if __name__=='__main__':
    main()
