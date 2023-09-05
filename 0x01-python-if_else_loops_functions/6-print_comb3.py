#!/usr/bin/python3
for i in range(0, 100):
    if i / 10 < i % 10:
        print(f"{i:02d}", end=", ")
        if i == 89:
            print(f"{i:02d}")