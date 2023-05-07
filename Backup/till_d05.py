dirty_spaces_not_cleaned = []
possible_positions =[]

def problems_a_to_f():
    #print('Hi, I am going to solve Problems One by One')
    for i in range(6):
        if i == 0:
            problem_path = "./problems/problem_a_"
            #print(problem_path)
            #solve_problem(problem_path)
        elif i == 1:
            problem_path = "./problems/problem_b_"
            #print(problem_path)
            #solve_problem(problem_path)
        elif i == 2:
            problem_path = "./problems/problem_c_"
            #print(problem_path)
            #solve_problem(problem_path)
        elif i == 3:
            problem_path = "./example-problems/problem_d_"
            print(problem_path)
            solve_problem(problem_path)
        elif i == 4:
            problem_path = "./problems/problem_e_"
            print(problem_path)
            #solve_problem(problem_path)
        elif i == 5:
            problem_path = "./problems/problem_f_"
            print(problem_path)
            #solve_problem(problem_path)


def solve_problem(problem_path):
    increment = 0
    zeros = 0
    completed = 0
  #  while completed < 20:
        #file_path = str(problem_path) + str(zeros)+str(increment)+".txt"
        #file_path ="./example-problems/problem_c_" + str(zeros)+str(increment)+".txt"
        #print(file_path)
        #if increment == 9:
        #    increment = 0
        #    zeros += 1
        #else:
        #    increment +=1
        #print(file_path)
#        completed = int(str(zeros)+str(increment))

    file_path ="./example-problems/problem_d_06.txt"

    with open(file_path, 'r') as f:
        lines = "garbage"
        counter = 0
        problem_list = []
        while lines != "":
            # Read lines one by one:
            lines = f.readline()
            counter += 1
            problem_list.append(lines)
            #print(counter, ":   ", lines)

            #The list items contain \n at the end as file contains end of line characters so to replace them:
        problem_list = [s.replace('\n', '') for s in problem_list]
            #print(problem_list)

        if problem_list[0] == "CHECK PLAN":
            check_plan(problem_list)
            pass
        elif problem_list[0] == "FIND PLAN":
                find_plan(problem_list)


def find_plan(problem_list):
    print("I am going to find plan:")
    # removing the first line and getting the map of problem:
    map_list = []
    index = 1
    for i in range(len(problem_list) - 2):
        map_list.append(problem_list[i + 1])
        index += 1
    final_map = []
    # print(map_list)

    # converting to a 2d array or a list of lists which can be accessed with 2d indexes
    for i in map_list:
        # print(i)
        to_array = list(i)
        final_map.append(to_array)
    print(final_map)
    orientation, x, y = get_starting_position(final_map)
    print(orientation)
    print(x,":", y)
    plan = " "
    plan = create_plan(orientation, x, y, plan, final_map)
    print("End Resulted Plan: ", plan)

def create_plan(orientation, x, y, plan, final_map):
    solution=""
    #print("Orientation: ", orientation)
    dirty_spaces = find_dirty_spaces(final_map)
    #print("dirty Spaces:", dirty_spaces)
    if orientation == "S":
        dirty_spaces_not_cleaned = " " #move_for_unknown_orientation(orientation, x, y, plan, final_map)
        return dirty_spaces_not_cleaned
    elif orientation is None:
        final_dirty_spaces_not_cleaned=[]
        #dirty_spaces_not_cleaned = unknown_orientation_and_position(plan, final_map, dirty_spaces)
        #for s in dirty_spaces_not_cleaned:
        #    for a in s:
        #        final_dirty_spaces_not_cleaned.append(a)
        return final_dirty_spaces_not_cleaned
    else:
        print("coming into the problem")
        complete_plan = ""
        origin = (x, y)
        cleaned_spaces = []
        cleaned_spaces_visited=[]
        possible_positions=[]
        while dirty_spaces != []:
            print("Orientation: ", orientation)
            dirty_spaces, x, y, orientation, sequence, cleaned_spaces, cleaned_spaces_visited = clean_spaces(dirty_spaces, x, y, orientation, final_map, origin, cleaned_spaces, cleaned_spaces_visited)
            complete_plan += sequence
            print("complete sequence:", complete_plan)
                    #dirty_spaces = []
                #if final_map[x-1][y] == "X":
                #    pass
                #else:
                #    x -= 1
                #    if [x, y] in dirty_spaces:
                #        dirty_spaces.remove([x, y])
        return complete_plan
def manhattan_distance():
    dis = 0

    #for i in range(len(A)):
    #    dis += abs(A[i] - B[i])

def clean_spaces(dirty_spaces, x, y, orientation, final_map, origin, cleaned_spaces, cleaned_spaces_visited):
    print("finding plan:")
    flag = bool
    sub_plan = ""
    possible_positions = get_neighbours(x, y, final_map)
    print("x:",x)
    print("y:",y)
    print("Possible positions: andar janay se pehlay", possible_positions )
    count = 0
    print(cleaned_spaces_visited)
    print(origin)
    for i in possible_positions:
        if final_map[i[0]][i[1]] != "X" and [i[0], i[1]] in dirty_spaces and [i[0], i[1]] not in cleaned_spaces:
            print("dirty Spaces", dirty_spaces)
            print([i[0], i[1]])
            orientation, instruction, x, y = next_move(orientation, x, y, i[0], i[1], final_map)
            print(orientation)
            sub_plan += instruction
            print(sub_plan)
            print(possible_positions)
            print("Cleaning: ", x, ":", y)
            if [x, y] in dirty_spaces:
                dirty_spaces.remove([x, y])
                print("After removing", x, " and", y, dirty_spaces)
                cleaned_spaces.append([x, y])
                check_if_blocked = is_blocked(final_map, x, y)
                print(check_if_blocked)
                if cleaned_spaces_visited != []:
                    cleaned_spaces_visited[0] = [x, y]
                else:
                    cleaned_spaces_visited.append([x, y])
                flag = True
                break
        else:
            count += 1
    if count == 4:
        for i in possible_positions:
            if final_map[i[0]][i[1]] != "X" and [i[0], i[1]] not in dirty_spaces and [i[0], i[1]] in cleaned_spaces and [i[0], i[1]] not in cleaned_spaces_visited:
                print("already cleaned spaces ")
                if cleaned_spaces_visited != []:
                    cleaned_spaces_visited[0] = [x, y]
                else:
                    cleaned_spaces_visited.append([x, y])
                orientation, instruction, x, y = next_move(orientation, x, y, i[0], i[1], final_map)
                print(orientation)
                sub_plan += instruction
                print(sub_plan)
                flag = True
                break
    if flag != True:
        for i in possible_positions:
            if final_map[i[0]][i[1]] != "X" and [i[0], i[1]] not in dirty_spaces and [i[0], i[1]] not in cleaned_spaces and origin == (i[0], i[1]):
                print("origin wali", dirty_spaces)
                print([i[0], i[1]])
                orientation, instruction, x, y = next_move(orientation, x, y, i[0], i[1], final_map)
                print(orientation)
                sub_plan += instruction
                print(sub_plan)
                print(possible_positions)
                print("Cleaning: ", x, ":", y)
                if [x, y] in dirty_spaces:
                    dirty_spaces.remove([x, y])
                    print("After removing", x, " and", y, dirty_spaces)
                    cleaned_spaces.append([x, y])
                    flag = True
                    break
            #return dirty_spaces, x, y, orientation, sub_plan, cleaned_spaces
    return dirty_spaces, x, y, orientation, sub_plan, cleaned_spaces, cleaned_spaces_visited


def next_move(orientation, x, y, x1, y1, final_map):
    print("checking the next move")
    print("x:", x)
    print("x1:", x1)
    print("y:", y)
    print("y1:", y1)

    if ((int(x1) > int(x) and int(y1) > int(y)) or (int(x) > int(x1) and int(y) > int(y1))):
        print("Move not possible")
        instruction = ""
        return orientation, instruction, x, y

    if orientation == "^":
        if x < x1 and y == y1:
            print(x+1, "", y)
            instruction = "LLM"
            orientation = "v"
            x += 1
            return orientation, instruction, x, y
        elif x > x1 and y == y1:
            print(x - 1, "", y)
            instruction = "M"
            x-=1
            return orientation, instruction, x, y
        elif x == x1 and y < y1:
            print(x, "", y+1)
            orientation = ">"
            instruction = "RM"
            y+=1
            return orientation, instruction, x, y
        elif x == x1 and y > y1:
            print(x, "", y-1)
            orientation = "<"
            instruction = "LM"
            y-=1
            return orientation, instruction, x, y
    elif orientation == "<":
        if x < x1 and y == y1:
            print(x + 1, "", y)
            orientation = "v"
            instruction = "LM"
            x+=1
            return orientation, instruction, x, y
        elif x > x1 and y == y1:
            print(x - 1, "", y)
            orientation = "^"
            instruction = "RM"
            x-=1
            return orientation, instruction, x, y
        elif x == x1 and y < y1:
            print(x, "", y + 1)
            orientation = ">"
            instruction = "LLM"
            y+=1
            return orientation, instruction, x, y
        elif x == x1 and y > y1:
            print(x, "", y - 1)
            instruction = "M"
            y-=1

            return orientation, instruction, x, y
    elif orientation == ">":
        if x < x1 and y == y1:
            print(x + 1, "", y)
            orientation = "v"
            instruction = "RM"
            x+=1
            return orientation, instruction, x, y
        elif x > x1 and y == y1:
            print(x - 1, "", y)
            orientation = "^"
            instruction = "LM"
            x-=1
            return orientation, instruction, x, y
        elif x == x1 and y < y1:
            print(x, "", y + 1)
            instruction = "M"
            y+=1
            return orientation, instruction, x, y
        elif x == x1 and y > y1:
            print(x, "", y - 1)
            orientation = "<"
            instruction = "LLM"
            y-=1
            return orientation, instruction, x, y
    elif orientation == "v":
        if x < x1 and y == y1:
            print(x + 1, "", y)
            instruction = "M"
            x+=1
            return orientation, instruction, x, y
        elif x > x1 and y == y1:
            print(x - 1, "", y)
            orientation = "^"
            instruction = "LLM"
            x-=1
            return orientation, instruction, x, y
        elif x == x1 and y < y1:
            print(x, "", y + 1)
            orientation = ">"
            instruction = "LM"
            y+=1
            return orientation, instruction, x, y
        elif x == x1 and y > y1:
            print(x, "", y - 1)
            orientation = "<"
            instruction = "RM"
            y-=1
            return orientation, instruction,  x, y
        possible_positions = get_neighbours(x, y)
        print(possible_positions)
        return orientation, "", possible_positions, x, y
def check_plan(problem_list):
    #print("I am going to check the given plan:")
    plan = problem_list[1]
    dirty_spaces_not_cleaned=[]
    #print("Here is the plan:  ", plan)

    # removing the first two lines and getting the map of problem:
    map_list = []
    index = 2
    length_of_list = len(problem_list) - 2
    for i in range(len(problem_list) - 3):
        map_list.append(problem_list[i + 2])
        index += 1
    final_map =[]
    #print(map_list)

#converting to a 2d array or a list of lists which can be accessed with 2d indexes
    for i in map_list:
        #print(i)
        to_array = list(i)
        final_map.append(to_array)
    #print(final_map_list)
    #check_if_blocked=is_blocked(final_map_list,7,4)
    #print(check_if_blocked)
    orientation, x, y = get_starting_position(final_map)
    #print("Orientation: ", orientation)
    #print("i: ", x)
    #print("j: ", y)
    dirty_spaces = try_plan(orientation, x, y, plan, final_map)

    for s in dirty_spaces:
        dirty_spaces_not_cleaned.append(s)

    if dirty_spaces_not_cleaned == []:
        print("GOOD PLAN")
    else:
        print("BAD PLAN")
        #print(dirty_spaces_not_cleaned)
        dirty_spaces_not_cleaned= set(tuple(element) for element in dirty_spaces_not_cleaned)
        for x in dirty_spaces_not_cleaned:
            print(x[1], ",", x[0])


def get_neighbours(x, y, final_map):
    if x == 0 and y == 0:
        return [(x+1, y), (x, y+1)]
    elif x == 0 and y != 0:
        return [(x+1, y), (x, y+1), (x, y-1)]
    elif x != 0 and y == 0:
        return [(x+1, y), (x, y+1), (x-1, y)]
    elif x != 0 and y != 0:
        return [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]
    elif x == len(final_map) and y != len(final_map[1]):
        return [(x - 1, y), (x, y - 1), (x, y+1)]
    elif x != len(final_map) and y == len(final_map[1]):
        return [(x+1, y), (x - 1, y), (x, y - 1)]
    elif x != len(final_map) and y == len(final_map[1]):
        return [(x - 1, y), (x, y - 1)]


#    print(get_neighbours(3, 5))


def is_blocked(map_list, x, y):
    neighbours = get_neighbours(x, y, map_list)
    blocked = bool
    count = 0
    for n in neighbours:
        if map_list[int(n[0])][int(n[1])] == "X":
            count += 1
    if count == 3:
        blocked = True
    return blocked


def get_starting_position(map_list):
    #print("starting position finding")
    orientation = ""
    for i in range(len(map_list)):
        for j in range(len(map_list[0])):
            if map_list[i][j] == "S":
                orientation = "S"
                return orientation, i, j
            if map_list[i][j] == "v" or map_list[i][j] == "<" or map_list[i][j] == ">" or map_list[i][j] == "^":
                #print("found the starting orientation")
                orientation = map_list[i][j]
                return orientation, i, j
    orientation = None
    i = None
    j = None
    return orientation, i, j


def find_dirty_spaces(final_map):
    dirty_spaces = []
    for i in range(len(final_map)):
        for j in range(len(final_map[0])):
            if final_map[i][j] == "X":
                continue
            if final_map[i][j] == "S" or final_map[i][j] == "v" or final_map[i][j] == "<" or final_map[i][j] == ">" or final_map[i][j] == "^":
                continue
            if final_map[i][j] == " ":
                dirty_spaces.append([i, j])
    return dirty_spaces

# 1. What square do I land on if I walk one square (action M) from square ⟨2, 8⟩ when if I
# initially face up? (Try this with other directions and make sure there are no bugs.)


def try_plan(orientation, x, y, plan, final_map):
    #print("Orientation: ", orientation)
    dirty_spaces = find_dirty_spaces(final_map)
    #print("dirty Spaces:", dirty_spaces)
    if orientation == "S":
        dirty_spaces_not_cleaned = move_for_unknown_orientation(orientation, x, y, plan, final_map)
        return dirty_spaces_not_cleaned
    elif orientation is None:
        final_dirty_spaces_not_cleaned=[]
        dirty_spaces_not_cleaned = unknown_orientation_and_position(plan, final_map, dirty_spaces)
        for s in dirty_spaces_not_cleaned:
            for a in s:
                final_dirty_spaces_not_cleaned.append(a)
        return final_dirty_spaces_not_cleaned
    else:
        for instruction in plan:
            if instruction == "R":
                orientation, x, y = move_to_r(orientation, x, y, plan, final_map)
            elif instruction == "L":
                orientation, x, y = move_to_l(orientation, x, y, plan, final_map)
            elif instruction == "M":
                orientation, x, y, dirty_spaces = move_to_m(orientation, x, y, plan, final_map, dirty_spaces)
        return dirty_spaces
    return []


def unknown_orientation_and_position(plan, final_map, dirty_spaces):
    dirty_spaces_not_cleaned = []
    new_dirty_spaces = dirty_spaces
    for position in dirty_spaces:
        x = position[0]
        y = position[1]
        orientation = "S"
        new_dirty_spaces.remove(position)
        dirty_spaces_not_cleaned.append(try_plan(orientation, x, y, plan, final_map))
    return dirty_spaces_not_cleaned


def move_to_r(orientation, x, y, plan, final_map):
    if orientation == "^":
        orientation = ">"
    elif orientation == "<":
        orientation = "^"
    elif orientation == ">":
        orientation = "v"
    elif orientation == "v":
        orientation = "<"
    return orientation, x, y


def move_to_l(orientation, x, y, plan, final_map):
    if orientation == "^":
        orientation = "<"
    elif orientation == "<":
        orientation = "v"
    elif orientation == ">":
        orientation = "^"
    elif orientation == "v":
        orientation = ">"
    return orientation, x, y


def move_to_m(orientation, x, y, plan, final_map, dirty_spaces):
    if orientation == "^":
        if final_map[x-1][y] == "X":
            pass
        else:
            x -= 1
            if [x, y] in dirty_spaces:
                dirty_spaces.remove([x, y])
    elif orientation == "<":
        if final_map[x][y-1] == "X":
            pass
        else:
            y -= 1
            if [x, y] in dirty_spaces:
                dirty_spaces.remove([x, y])
    elif orientation == ">":
        if final_map[x][y+1] == "X":
            pass
        else:
            y += 1
            if [x, y] in dirty_spaces:
                dirty_spaces.remove([x, y])
    elif orientation == "v":
        if final_map[x+1][y] == "X":
            pass
        else:
            x += 1
            if [x, y] in dirty_spaces:
                dirty_spaces.remove([x, y])
    return orientation, x, y, dirty_spaces


def move_for_unknown_orientation(orientation, x, y, plan, final_map):
    dirty_spaces_not_cleaned= []
    for direction in ["^", "<", ">", "v"]:
        if direction == "^":
            orientation = direction
            dirty_spaces = try_plan(orientation, x, y, plan, final_map)
            for s in dirty_spaces:
                dirty_spaces_not_cleaned.append(s)
        elif direction == "<":
            orientation = direction
            dirty_spaces = try_plan(orientation, x, y, plan, final_map)
            for s in dirty_spaces:
                dirty_spaces_not_cleaned.append(s)
        elif direction == ">":
            orientation = direction
            dirty_spaces = try_plan(orientation, x, y, plan, final_map)
            for s in dirty_spaces:
                dirty_spaces_not_cleaned.append(s)
        elif direction == "v":
            orientation = direction
            dirty_spaces = try_plan(orientation, x, y, plan, final_map)
            for s in dirty_spaces:
                dirty_spaces_not_cleaned.append(s)
    return dirty_spaces_not_cleaned


if __name__ == '__main__':
    #mylist = [["a","b"], ["b","a"], ["a","b"], ["c","d"], ["c","d"]]
    #print(set(tuple(element) for element in mylist))
    problems_a_to_f()
#    a= {(6, 12)}
#    for x in a:
#        print(x[0])
#        print(x[1])

