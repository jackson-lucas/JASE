# source: http://www.geekviewpoint.com/python/sorting/heapsort
def heapify( aList ):
  # convert aList to heap
  length = len( aList ) - 1
  leastParent = length / 2
  for i in range ( leastParent, -1, -1 ):
    moveDown( aList, i, length )

def moveDown( aList, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    # right child exists and is larger than left child
    if ( largest < last ) and ( aList[largest][1] < aList[largest + 1][1] ):
      largest += 1

    # right child is larger than parent
    if aList[largest][1] > aList[first][1]:
      swap( aList, largest, first )
      # move down to largest child
      first = largest;
      largest = 2 * first + 1
    else:
      return # force exit


def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

def main():
    numbers = [
        [2,0.5],[5,0.7],[3,0.4],[1,0.67],
        [9,0.43],[6,0.55],[0,0.557],[7,0.65],[4,0.52]
    ]
    heapify(numbers)
    print(numbers)

if __name__ == '__main__':
    main()
