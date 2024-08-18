def twoStacks(maxSum, a, b):
    # Write your code here
    count = 0
    temp_arr = []

    max_a = 0
    while a:
        if (max_a + a[0]) <= maxSum:
            temp = a.pop(0)
            max_a += temp
            temp_arr.append(temp)
            count += 1
        else:
            break
    
    max_b = 0
    while b:
        if (max_b + b[0]) <= maxSum:
            if (max_a + b[0]) <= maxSum:
                count += 1
                temp = b.pop(0)
                max_a += temp
                max_b += temp
                temp_arr.append(temp)
            else:
                temp = b.pop(0)
                max_a = max_a - temp_arr.pop() + temp
                max_b += temp
        else:
            break

    return count
    
s2 = [756, 893, 560, 192, 723, 711, 397, 822, 223, 877, 513, 753, 877, 245, 537, 335, 135, 613, 332, 723, 566, 396, 545, 228, 318, 398, 733, 912, 980, 313, 88, 88, 206, 648, 281, 929, 711, 678, 103, 934, 908, 969, 687, 785, 214, 225, 120, 701, 190, 804, 425, 756, 552, 322, 984, 870, 73, 70, 782, 53, 383, 222, 494, 589, 223, 127, 870, 934, 805, 326, 869, 65, 295, 908, 850, 509, 485, 322, 211, 675, 479, 988, 783]
s1 = [383, 310, 120, 254, 383, 190, 388, 789, 573, 963, 283, 514, 186, 410, 736, 472, 567, 62, 693, 633, 357, 602, 835, 219, 439, 510, 782, 115]

print(twoStacks(7176, s1, s2))