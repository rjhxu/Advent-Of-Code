line = open("2024/day9/input.txt", "r").readline().strip()
blocks = []
current_id = 0
pos = 0

# Create initial block representation
while pos < len(line):
    # Read file length
    file_length = int(line[pos])
    blocks.extend([current_id] * file_length)
    current_id += 1
    pos += 1
    
    # Read space length if there is one
    if pos < len(line):
        space_length = int(line[pos])
        blocks.extend([-1] * space_length)
        pos += 1

# Process files from highest ID to lowest
max_id = max(x for x in blocks if x != -1)
for file_id in range(max_id, -1, -1):
    if file_id not in blocks:
        continue
        
    # Get file details
    file_size = blocks.count(file_id)
    file_start = blocks.index(file_id)
    
    # Find leftmost space that can fit the file
    best_space_start = -1
    best_space_size = 0
    current_space_start = -1
    current_space_size = 0
    
    # Look through all positions before the file
    for i in range(file_start):
        if blocks[i] == -1:
            if current_space_start == -1:
                current_space_start = i
            current_space_size += 1
        else:
            current_space_start = -1
            current_space_size = 0
            
        # If we found a valid space and it's better than our previous best
        if current_space_size == file_size:
            best_space_start = current_space_start
            best_space_size = current_space_size
            break
    
    # If we found a valid space, move the file
    if best_space_start != -1:
        # Clear old position
        for i in range(len(blocks)):
            if blocks[i] == file_id:
                blocks[i] = -1
        # Place in new position
        for i in range(file_size):
            blocks[best_space_start + i] = file_id

checksum = sum(i * id for i, id in enumerate(blocks) if id != -1)
print("Final checksum:", checksum)