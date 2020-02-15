import unicodedata
import os

def main():
    for i in range(0, 128):
        print('\n')
        print(chr(i)+':')
        for j in range(128, 0x10000):
            if unicodedata.normalize('NFKC',chr(j)) == chr(i):
                print(chr(j),end=' ')

if __name__ == "__main__":
    main()