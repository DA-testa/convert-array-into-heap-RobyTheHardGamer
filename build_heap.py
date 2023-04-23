def sift_down(arr, i, swaps):
    n = len(arr)
    min_index = i
    left_child = 2*i + 1
    right_child = 2*i + 2

    if left_child < n and arr[left_child] < arr[min_index]:
        min_index = left_child

    if right_child < n and arr[right_child] < arr[min_index]:
        min_index = right_child

    if i != min_index:
        swaps.append((i, min_index))
        arr[i], arr[min_index] = arr[min_index], arr[i]
        sift_down(arr, min_index, swaps)

def build_heap(arr):
    swaps = []
    n = len(arr)

    for i in range(n//2, -1, -1):
        sift_down(arr, i, swaps)

    return swaps

# Example usage:

def main():


    input1 = input()
    if (input1 == "F"):
        lines = []
        input2 = input()
        with open(input2, 'r') as file:
            for line in file:
             # Do something with the current line
                lines.append(line.strip())  # Add the line to the list

        #print(lines)  # Print the list of lines

        swaps = build_heap(lines)

        print(len(swaps))
        for swap in swaps:
            print(swap[0], swap[1])

    elif (input1 == "I"): #ja I


        n = int(input()) #nolasīta pirmā rinda
        arr = list(map(int, input().split())) #nolasīta otrā rinda

        swaps = build_heap(arr)

        print(len(swaps))
        for swap in swaps:
            print(swap[0], swap[1])
    else:
        print() #ja nav ievadīts ne F ne I, nepieņem ievadīto
        

##n = int(input()) ##Ievadīt par 'cik'?
##arr = list(map(int, input().split())) ##Ievadīt skaitļus, pēc 'cik'?

if __name__ == "__main__":
    main()