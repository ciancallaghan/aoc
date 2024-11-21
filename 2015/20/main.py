def get_factors_sum(n):
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n//i)
    return sum(set(factors))

def get_factors_sum_part2(n, visited, limit):
    factors = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            if i not in visited:
                visited[i] = 1
                factors.append(i)
            else:
                if visited[i] < 50:
                    visited[i] += 1
                    factors.append(i)
            if n//i not in visited:
                visited[n//i] = 1
                factors.append(n//i)
            else:
                if visited[n//i] < 50:
                    visited[n//i] += 1
                    factors.append(n//i)
    return sum(set(factors)), visited

goal = 29000000
# Part 1
val, house = 0, 0
while val < goal:
    house += 1
    val = get_factors_sum(house) * 10
print(house)

# Part 2
val, house = 0, 0
visited = dict()
while val < goal:
    house += 1
    val,visited = get_factors_sum_part2(house, visited, 50)
    val = val * 11
print(house)
