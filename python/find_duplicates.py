def find_duplicates_nested_loop(l: list) -> list:
    duplicates = []
    
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] == l[j] and l[i] not in duplicates:
                duplicates.append(l[i])
                break
                
    return duplicates

if __name__ == "__main__":
    sample1 = [3, 7, 5, 6, 7, 4, 8, 5, 7, 66]
    sample2 = [3, 5, 6, 4, 4, 5, 66, 6, 7, 6]
    sample3 = [3, 0, 5, 1, 0]
    sample4 = [3]
    
    print("Sample 1:", find_duplicates_nested_loop(sample1))  # Should print [7, 5]
    print("Sample 2:", find_duplicates_nested_loop(sample2))  # Should print [5, 4, 6]
    print("Sample 3:", find_duplicates_nested_loop(sample3))  # Should print [0]
    print("Sample 4:", find_duplicates_nested_loop(sample4))  # Should print []
