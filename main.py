from itertools import permutations

destination = {}
post = (0, 2)
address = [(2, 5), (5, 2), (6, 6), (8, 3)]


def find_distance(list):
    global destination
    result = f'{post} '
    total_distance = 0
    for n in range(len(list)-1):
        distance = ((list[n+1][0] - list[n][0]) ** 2 + (list[n+1][1] - list[n][1]) ** 2) ** 0.5
        total_distance += distance
        result += f'-> {list[n+1]}[{distance}] '
    destination[result] = total_distance


if __name__ == '__main__':
    routes = [item for item in permutations(address)]
    for e, i in enumerate(routes):
        route = list(i)
        route.append(post)
        route.insert(0, post)
        find_distance(route)

    short_route = min(destination, key=destination.get)

    print(f'''
    Кратчайший путь:
    {short_route}= {destination[short_route]}
          ''')