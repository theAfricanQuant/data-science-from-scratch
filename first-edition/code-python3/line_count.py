# line_count.py
import sys

if __name__ == "__main__":

    count = sum(1 for _ in sys.stdin)
    # print goes to sys.stdout
    print(count)
