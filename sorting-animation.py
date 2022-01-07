import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import time 

def swap(A, i, j):
        A[i], A[j] = A[j], A[i]

def bubble_sort_opt(array):  
    isSorted = False
    counter = 0
    sorting_arrays = []
    n_swaps = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1-counter):
            currentElement = array[i]
            nextElement = array[i+1]
            if currentElement > nextElement:
                swap(array,i,i+1)
                isSorted = False
                n_swaps +=1
            sorting_arrays.append(array.copy())
        counter+=1
    return sorting_arrays, n_swaps

def bubble_sort(arr):
    n = len(arr)
    sorting_arrays = []
    n_swaps = 0
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                n_swaps +=1
            sorting_arrays.append(arr.copy())
    return sorting_arrays, n_swaps


def insertion_sort(array):
    sorting_arrays = []
    n_swaps = 0
    for i in range(1,len(array)):
        j = i
        while j>0 and array[j] < array[j-1]:
            arr = []
            swap(array,j,j-1)
            j -= 1
            n_swaps +=1
            sorting_arrays.append(array.copy())
    return sorting_arrays, n_swaps

def selection_sort(array):
    sorting_arrays = []
    n_swaps = 0
    currentIdx = 0
    while currentIdx < len(array)-1:
        smallestIdx = currentIdx
        for i in range(currentIdx+1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
            sorting_arrays.append(array.copy())
        swap(array,currentIdx,smallestIdx)
        n_swaps +=1
        currentIdx +=1
    return sorting_arrays, n_swaps    

def generate_array(N=100):
    array = [x+1 for x in range(N)]
    np.random.seed(42)
    np.random.shuffle(array)
    return array



array = generate_array(25)
print(array)
arrays_bubble, n_swaps_bubble = bubble_sort(array.copy())
arrays_insertion, n_swaps_insertion = insertion_sort(array.copy())
arrays_selection, n_swaps_selection = selection_sort(array.copy())

n_max = max([len(arrays_insertion), len(arrays_bubble), len(arrays_selection)])

#Create new Figure with black background
fig, ax = plt.subplots(1,3,figsize=(15, 5), facecolor='black')

# No ticks
for i in range(3):
    ax[i].set_xticks([])
    ax[i].set_yticks([])
    ax[i].set_facecolor('black')


# 2 part titles to get different font weights
ax[0].text(0.5, 1.05, "BUBBLE ", transform=ax[0].transAxes,
        ha="right", va="bottom", color="w",
        family="sans-serif", fontweight="bold", fontsize=16)
ax[0].text(0.5, 1.05, "SORTING", transform=ax[0].transAxes,
        ha="left", va="bottom", color="w",
        family="sans-serif", fontweight="light", fontsize=16)

ax[1].text(0.5, 1.05, "INSERTION ", transform=ax[1].transAxes,
        ha="right", va="bottom", color="w",
        family="sans-serif", fontweight="bold", fontsize=16)
ax[1].text(0.5, 1.05, "SORTING", transform=ax[1].transAxes,
        ha="left", va="bottom", color="w",
        family="sans-serif", fontweight="light", fontsize=16)

ax[2].text(0.5, 1.05, "SELECTION ", transform=ax[2].transAxes,
        ha="right", va="bottom", color="w",
        family="sans-serif", fontweight="bold", fontsize=16)
ax[2].text(0.5, 1.05, "SORTING", transform=ax[2].transAxes,
        ha="left", va="bottom", color="w",
        family="sans-serif", fontweight="light", fontsize=16)


bars0 = ax[0].bar(range(len(array)), arrays_bubble[0], align='edge',width=0.8, color='lightseagreen')
bars1 = ax[1].bar(range(len(array)), arrays_insertion[0], align='edge',width=0.8, color='tomato')
bars2 = ax[2].bar(range(len(array)), arrays_selection[0], align='edge',width=0.8, color='plum')

text_bar = [0, 0, 0]

text_bar[0] = ax[0].text(0.30, 0.92, "", transform=ax[0].transAxes, ha="left", va="bottom", color="w",
        family="sans-serif", fontweight="light", fontsize=14)
text_bar[1] = ax[1].text(0.30, 0.92, "", transform=ax[1].transAxes, ha="left", va="bottom", color="w",
        family="sans-serif", fontweight="light", fontsize=14)
text_bar[2] = ax[2].text(0.30, 0.92, "", transform=ax[2].transAxes, ha="left", va="bottom", color="w",
        family="sans-serif", fontweight="light", fontsize=14)


iteration = [0, 0, 0]


def update(*args):

    if iteration[0] < len(arrays_bubble)-1:
        iteration[0] +=1
    else:
        iteration[0] = len(arrays_bubble)-1

    if iteration[1] < len(arrays_insertion)-1:
        iteration[1] +=1
    else:
        iteration[1] = len(arrays_insertion)-1

    if iteration[2] < len(arrays_selection)-1:
        iteration[2] +=1
    else:
        iteration[2] = len(arrays_selection)-1

    for bar0, val in zip(bars0, arrays_bubble[iteration[0]]):
        bar0.set_height(val)
    for bar1, val in zip(bars1, arrays_insertion[iteration[1]]):
        bar1.set_height(val)
    for bar2, val in zip(bars2, arrays_selection[iteration[2]]):
        bar2.set_height(val)

    text_bar[0].set_text(f'Iteration: {iteration[0]+1}')
    text_bar[1].set_text(f'Iteration: {iteration[1]+1}')
    text_bar[2].set_text(f'Iteration: {iteration[2]+1}')

    if iteration[0] == len(arrays_bubble)-1:
        text_bar[0].set_text(f'Iteration: {iteration[0]+1}\nSwaps = {n_swaps_bubble}')
    if iteration[1] == len(arrays_insertion)-1:
        text_bar[1].set_text(f'Iteration: {iteration[1]+1}\nSwaps = {n_swaps_insertion}')
    if iteration[2] == len(arrays_selection)-1:
        text_bar[2].set_text(f'Iteration: {iteration[2]+1}\nSwaps = {n_swaps_selection}')

    return bars0, bars1, bars2 


anim = animation.FuncAnimation(fig, func=update,
            fargs=(iteration), frames=n_max, interval=1, repeat=False)

plt.show()
#writervideo = animation.PillowWriter(fps=30)
#anim.save('sorting_animation.gif', writer=writervideo)

















