import time

def parse_input(filepath):
    diskmap = ""

    with open(filepath) as f:
        diskmap = f.read().strip("\n")

    limit = len(diskmap)
    file_blocks: list[str] = []
    file_id = 0

    for i in range(0, limit):
        if (i % 2) == 0:
            file_blocks += [str(file_id)] * int(diskmap[i])
            file_id += 1
        else:
            file_blocks += '.'  * int(diskmap[i])

    return file_blocks

def parse_input2(filepath):
    diskmap: list[str] = [] #empty space '.' is now noted as -1
    raw_input = ''

    with open(filepath) as f:
        raw_input = f.read().strip("\n")

    file_id = 0
    for i in range(0, len(raw_input)):
        #if raw_input[i] == '0':
        #    continue
        #file = []
        if (i % 2) == 0:
            file = [str(file_id)] * int(raw_input[i])
            file_id += 1
        else:
            file = ['.'] * int(raw_input[i])
        diskmap += file

    return diskmap

def file_compacter(diskmap: list[str]):
    i = 0
    while i < len(diskmap):
        if diskmap[i] == '.':
            for j in range(len(diskmap) - 1, i+1, -1):
                #swap last file to first empty space
                if diskmap[j] != '.':
                    diskmap[i] = diskmap[j]
                    diskmap.pop()
                    break
                diskmap.pop() #last item is irrelevant
        i += 1
    return diskmap

def cont_compacter(diskmap: list[str]): #contiguous compacter
    end = len(diskmap) - 1
    start = 0
    last = -1
    #iterate from the back
    while end > start:
        while diskmap[end] == '.':
            end -= 1
        current = diskmap[end]
        if last == -1:
            last = int(current)
        elif int(current) >= last:
            end -= 1
            continue
        block_start = end - 1
        #find the size of block to move
        while diskmap[block_start] == current:
            block_start -=1
        block_size = end - block_start
        #find first occurrence of empty space
        while diskmap[start] != '.':
            start += 1
        #find big enough empty space
        pointer = start
        is_big_enough = False
        while not is_big_enough and pointer+block_size-1 <= block_start:
            for index in range(pointer, pointer+block_size):
                if diskmap[index] != '.':
                    #this empty space isn't big enough, need to jump to next
                    is_big_enough = False
                    break
                else:
                    is_big_enough = True
            if not is_big_enough:
                #go to end of current empty but too small block
                while diskmap[pointer] == '.':
                    pointer += 1
                #go over the next occupied block
                while diskmap[pointer] != '.':
                    pointer += 1
        #swap values
        if is_big_enough:
            for index in range(pointer, pointer+block_size):
                diskmap[index] = current
            for index in range(block_start+1, end+1):
                diskmap[index] = '.'
        #rearrange pointers
        last = int(current)
        end = block_start

    #remove empty space from the end
    while diskmap[-1] == '.':
        diskmap.pop()

    return diskmap

def filesystem_checksum(diskmap: list[str]):
    checksum = 0
    for i in range(0, len(diskmap)):
        if diskmap[i] == '.':
            break
        checksum += i * int(diskmap[i])

    return checksum

def filesystem_checksum_cont(diskmap: list[str]):
    checksum = 0
    for i in range(0, len(diskmap)):
        if diskmap[i] == '.':
            continue
        checksum += i * int(diskmap[i])

    return checksum

def part_one():
    start_time = time.time()
    #filepath = "example.txt"
    filepath = 'input.txt'
    diskmap: list[str] = parse_input(filepath)
    print(f"Parsing took {time.time() - start_time} seconds")

    start_time = time.time()
    compacted: list[str] = file_compacter(diskmap)
    print(f"Compacting took {time.time() - start_time} seconds")

    start_time = time.time()
    checksum = filesystem_checksum(compacted)
    print(f"Calculating checksum took {time.time() - start_time} seconds")

    print(f"The resulting filesystem checksum is {checksum}")

def part_two():
    start_time = time.time()
    filepath = "input.txt"
    #filepath = "example.txt"
    diskmap: list[str] = parse_input2(filepath)
    print(f"Parsing took {time.time() - start_time} seconds")

    start_time = time.time()
    compacted: list[str] = cont_compacter(diskmap)
    print(f"Compacting took {time.time() - start_time} seconds")

    start_time = time.time()
    checksum = filesystem_checksum_cont(compacted)
    print(f"Calculating checksum took {time.time() - start_time} seconds")

    print(f"The resulting checksum of a defragmented file system is {checksum}")

if __name__ == '__main__':
    part_one()

    print("\n=============== PART 2 ===================\n")

    part_two()

#test case from reddit:
#input 9953877292941
#defragged disk "00000000063333333.11111...22222222................444444444..555555555....."
#checksum 5768 (part 2)