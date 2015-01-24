from collections import deque


def process_maze(maze):
    r, c = len(maze), len(maze[0])
    obstacles, dangers, blockers = set(), set(), '#><^v'
    for i in range(r):
        for j in range(c):
            cell = maze[i][j]
            if cell == '#':
                obstacles.add((i, j))
            elif cell == 'S':
                start = (i, j)
            elif cell == 'G':
                goal = (i, j)
            elif cell in '<>^v':
                obstacles.add((i, j))
                # to the left
                for b in range(j - 1, -1, -1):
                    if maze[i][b] in "#<^>v":
                        break
                    dangers.add((i, b, "<v>^".find(cell)))
                # to the right
                for b in range(j + 1, c, +1):
                    if maze[i][b] in "#<^>v":
                        break
                    dangers.add((i, b, ">^<v".find(cell)))
                # to the top
                for a in range(i - 1, -1, -1):
                    if maze[a][j] in "#<^>v":
                        break
                    dangers.add((a, j, "^<v>".find(cell)))
                # to the bottom
                for a in range(i + 1, r, +1):
                    if maze[a][j] in "#<^>v":
                        break
                    dangers.add((a, j, "v>^<".find(cell)))

    # print (r, c, start, goal, obstacles, dangers)
    return (r, c, start, goal, obstacles, dangers)


def bfs(r, c, start, goal, obstacles, dangers):
    visited = set()
    visited.add((start[0], start[1], 0))
    nodes = deque([(start[0], start[1], 0)])
    count = 0
    done = {(start[0], start[1], 0): 0}
    while nodes:
        i, j, stepmod4 = nodes.popleft()
        if (i, j) == goal:
            return count
            return done[(i, j, stepmod4)]
        for di, dj in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
            new_i = i + di
            new_j = j + dj
            new_step = (stepmod4 + 1) % 4
            # if (new_i, new_j, new_step) in zip(visited, dangers):
            # if (new_i, new_j, new_step) in zip(done, dangers):
            #     continue
            if (new_i, new_j, new_step) in done:
                continue
            if (new_i, new_j, new_step) in dangers:
                continue
            if (new_i, new_j) in obstacles:
                continue
            if new_i < 0 or new_j < 0 or new_i >= r or new_j >= c:
                continue
            count += 1
            done[(new_i, new_j, new_step)] = done[(i, j, stepmod4)] + 1
            nodes.append((new_i, new_j, new_step))
            visited.add((new_i, new_j, new_step))
    return None


def solve_maze(maze):
    return bfs(*process_maze(maze))


def main():
    t = int(raw_input())
    for i in range(t):
        r, c = map(int, raw_input().split())
        maze = []
        for _ in range(r):
            maze.append(raw_input().strip())
        #print maze
        result = solve_maze(maze)
        if result:
            print 'Case #{}: {} '.format(i+1, result)
        else:
            print 'Case #{}: {} '.format(i+1, 'impossible')
main()
