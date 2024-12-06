import time

start = time.time()

datas_day_5 = datas.strip().splitlines()
separator_index = datas_day_5.index("")
rules: List[Tuple[int, ...]] = [tuple(map(int, el.split("|"))) for el in datas_day_5[:separator_index]]
updates: List[List[int]] = [list(map(int, el.split(","))) for el in datas_day_5[separator_index + 1:]]

struct_time = time.time() - start


def get_center_page(u: List[int]) -> int:
    return u[len(u) // 2]


def is_update_ordered(tmp_update: List[int], list_rules: List[Tuple[int, ...]]) -> bool:
    for r in list_rules:
        if r[0] in tmp_update and r[1] in tmp_update:
            if tmp_update.index(r[0]) > tmp_update.index(r[1]):
                return False
    return True


total: int = 0
for update in updates:
    if is_update_ordered(update, rules):
        total += get_center_page(update)

print(f"Total part 1 : {total}")
end = time.time()
print(end - start)

total_2: int = 0


def build_graph(tmp_rulers: List[Tuple[int, ...]]) -> Dict[int, List[int]]:
    tmp_graph: Dict[int, List[int]] = defaultdict(list)
    for a, b in tmp_rulers:
        tmp_graph[a].append(b)
    return tmp_graph


def topological_sort(tmp_graph: Dict[int, List[int]], update: List[int]) -> List[int]:
    in_degree = {u: 0 for u in update}
    for u in update:
        if u in tmp_graph:
            for v in graph[u]:
                if v in update:
                    in_degree[v] += 1

    result = []
    queue = [n for n in update if in_degree[n] == 0]

    while queue:
        tmp = queue.pop(0)
        result.append(tmp)
        if tmp in tmp_graph:
            for v in tmp_graph[tmp]:
                if v in update:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)

    return result


graph = build_graph(rules)

for update in updates:
    if not is_update_ordered(update, rules):
        sorted_update = topological_sort(graph, update)
        total_2 += get_center_page(sorted_update)

print(f"Total part 2 : {total_2}")
end_2 = time.time()
print((end_2 - end) + struct_time)