from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional

import re

MENU_SORTING_KEYWORDS = {
    "sorting algorithms",
    "sorting algorithm",
    "sort algorithms",
    "sort algorithm",
    "sorting",
    "sort",
}
MENU_PATHFINDING_KEYWORDS = {
    "pathfinding algorithms",
    "pathfinding algorithm",
    "path algorithms",
    "path algorithm",
    "pathfinding",
    "path finding",
    "path",
    "finding",
}
MENU_DATA_STRUCTURE_KEYWORDS = {
    "data structures",
    "data structure",
    "structures",
    "structure",
    "data",
}

MENU_SELECTION_NUMBERS = {
    "sorting": {"1"},
    "pathfinding": {"2"},
    "data_structures": {"3"},
}

SORTING_NUMBER_TO_ALGORITHM = {
    "1": "Bubble Sort",
    "2": "Merge Sort",
    "3": "Selection Sort",
    "4": "Insertion Sort",
    "5": "Quick Sort",
    "6": "Heap Sort",
}

SORTING_SELECTION_KEYWORDS = {
    "bubble sort": "Bubble Sort",
    "bubblesort": "Bubble Sort",
    "bubble": "Bubble Sort",
    "merge sort": "Merge Sort",
    "mergesort": "Merge Sort",
    "merge": "Merge Sort",
    "selection sort": "Selection Sort",
    "selectionsort": "Selection Sort",
    "selection": "Selection Sort",
    "insertion sort": "Insertion Sort",
    "insertionsort": "Insertion Sort",
    "insertion": "Insertion Sort",
    "quick sort": "Quick Sort",
    "quicksort": "Quick Sort",
    "quick": "Quick Sort",
    "heap sort": "Heap Sort",
    "heapsort": "Heap Sort",
    "heap": "Heap Sort",
}

MAIN_MENU_MESSAGE = (
    "Hi, what are you going to explore today?\n\n"
    "1. Sorting algorithms\n"
    "2. Pathfinding algorithms\n"
    "3. Data structures\n\n"
    "Please select one of these algorithms!"
)

SORTING_MENU_MESSAGE = (
    "Sorting Algorithms:\n"
    "1. Bubble Sort\n"
    "2. Merge Sort\n"
    "3. Selection Sort\n"
    "4. Insertion Sort\n"
    "5. Quick Sort\n"
    "6. Heap Sort\n"
    "Reply with the algorithm name or number, or type 'menu' to go back."
)

PATHFINDING_NUMBER_TO_ALGORITHM = {
    "1": "Dijkstra's Algorithm",
    "2": "A* (A-Star)",
    "3": "Breadth-First Search (BFS)",
    "4": "Depth-First Search (DFS)",
}

PATHFINDING_SELECTION_KEYWORDS = {
    # Dijkstra's Algorithm - longer/more specific keywords first for substring matching
    "dijkstra's algorithm": "Dijkstra's Algorithm",
    "dijkstras algorithm": "Dijkstra's Algorithm",
    "dijkstra algorithm": "Dijkstra's Algorithm",
    'dijkstra"s algorithm': "Dijkstra's Algorithm",
    "dijkstra s algorithm": "Dijkstra's Algorithm",
    "the first": "Dijkstra's Algorithm",
    "dijkstra's": "Dijkstra's Algorithm",
    "dijkstras": "Dijkstra's Algorithm",
    "dijkstra": "Dijkstra's Algorithm",
    "first": "Dijkstra's Algorithm",
    "1": "Dijkstra's Algorithm",
    # Common misspellings of Dijkstra (longer first)
    "dijikstra's": "Dijkstra's Algorithm",
    "dijikstras": "Dijkstra's Algorithm",
    "dijikstra": "Dijkstra's Algorithm",
    "dijkstar's": "Dijkstra's Algorithm",
    "dijkstars": "Dijkstra's Algorithm",
    "dijkstar": "Dijkstra's Algorithm",
    "dijstra's": "Dijkstra's Algorithm",
    "dijstras": "Dijkstra's Algorithm",
    "dijstra": "Dijkstra's Algorithm",
    "dikstra's": "Dijkstra's Algorithm",
    "dikstras": "Dijkstra's Algorithm",
    "dikstra": "Dijkstra's Algorithm",
    # A* (A-Star) - longer/more specific keywords first
    "a-star algorithm": "A* (A-Star)",
    "a star algorithm": "A* (A-Star)",
    "astar algorithm": "A* (A-Star)",
    "a* algorithm": "A* (A-Star)",
    "a-star search": "A* (A-Star)",
    "a star search": "A* (A-Star)",
    "a* search": "A* (A-Star)",
    "astar search": "A* (A-Star)",
    "the second": "A* (A-Star)",
    "a-star": "A* (A-Star)",
    "a star": "A* (A-Star)",
    "astar": "A* (A-Star)",
    "a*": "A* (A-Star)",
    "second": "A* (A-Star)",
    "2": "A* (A-Star)",
    # Breadth-First Search (BFS) - longer/more specific keywords first
    "breadth-first search algorithm": "Breadth-First Search (BFS)",
    "breadth first search algorithm": "Breadth-First Search (BFS)",
    "breadth-first search": "Breadth-First Search (BFS)",
    "breadth first search": "Breadth-First Search (BFS)",
    "breadth first traversal": "Breadth-First Search (BFS)",
    "breadth-first traversal": "Breadth-First Search (BFS)",
    "bfs traversal": "Breadth-First Search (BFS)",
    "bfs algorithm": "Breadth-First Search (BFS)",
    "breadth-first": "Breadth-First Search (BFS)",
    "breadth first": "Breadth-First Search (BFS)",
    "the third": "Breadth-First Search (BFS)",
    "breadth": "Breadth-First Search (BFS)",
    "bfs": "Breadth-First Search (BFS)",
    "third": "Breadth-First Search (BFS)",
    "3": "Breadth-First Search (BFS)",
    # Depth-First Search (DFS) - longer/more specific keywords first
    "depth-first search algorithm": "Depth-First Search (DFS)",
    "depth first search algorithm": "Depth-First Search (DFS)",
    "depth-first search": "Depth-First Search (DFS)",
    "depth first search": "Depth-First Search (DFS)",
    "depth first traversal": "Depth-First Search (DFS)",
    "depth-first traversal": "Depth-First Search (DFS)",
    "dfs traversal": "Depth-First Search (DFS)",
    "dfs algorithm": "Depth-First Search (DFS)",
    "depth-first": "Depth-First Search (DFS)",
    "depth first": "Depth-First Search (DFS)",
    "the fourth": "Depth-First Search (DFS)",
    "depth": "Depth-First Search (DFS)",
    "dfs": "Depth-First Search (DFS)",
    "fourth": "Depth-First Search (DFS)",
    "4": "Depth-First Search (DFS)",
}

PATHFINDING_MENU_MESSAGE = (
    "Pathfinding Algorithms:\n"
    "1. Dijkstra's Algorithm\n"
    "2. A* (A-Star)\n"
    "3. Breadth-First Search (BFS)\n"
    "4. Depth-First Search (DFS)\n"
    "Reply with the algorithm name or number, or type 'menu' to go back."
)

ARRAY_INPUT_RE = re.compile(r"^\s*-?\d+(?:\s*,\s*-?\d+)*\s*$")


def _make_step(
    algorithm: str,
    array: List[int],
    highlighted: Optional[List[int]],
    sorted_indices: Optional[List[int]],
    explanation: str,
    step_number: int,
) -> Dict[str, Any]:
    return {
        "status": "success",
        "type": "visualization_step",
        "algorithm": algorithm,
        "step": step_number,
        "data": {
            "array": list(array),
            "highlighted_indices": highlighted or [],
            "sorted_indices": sorted_indices or [],
        },
        "explanation": explanation,
    }


def _complete_step(algorithm: str, array: List[int], step_number: int) -> Dict[str, Any]:
    return _make_step(
        algorithm=algorithm,
        array=array,
        highlighted=[],
        sorted_indices=list(range(len(array))),
        explanation="Sorting complete.",
        step_number=step_number,
    )


# -------- Pathfinding utilities --------
GridPoint = tuple[int, int]


def _in_bounds(point: GridPoint, rows: int, cols: int) -> bool:
    r, c = point
    return 0 <= r < rows and 0 <= c < cols


def _neighbors(point: GridPoint, rows: int, cols: int) -> List[GridPoint]:
    r, c = point
    candidates = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    return [(nr, nc) for nr, nc in candidates if _in_bounds((nr, nc), rows, cols)]


def _reconstruct_path(
    parents: Dict[GridPoint, GridPoint], end: GridPoint
) -> List[GridPoint]:
    if end not in parents:
        return []
    path: List[GridPoint] = [end]
    cur = end
    while cur in parents:
        cur = parents[cur]
        path.append(cur)
        if parents[cur] == cur:
            break
    path.reverse()
    return path


def generate_bubble_sort_steps(values: List[int]) -> List[Dict[str, Any]]:
    arr = list(values)
    steps: List[Dict[str, Any]] = []
    n = len(arr)
    step = 1
    if n <= 1:
        steps.append(
            _make_step(
                "Bubble Sort",
                arr,
                [],
                list(range(n)),
                "Array of length 0 or 1 is already sorted.",
                step,
            )
        )
        return steps

    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            explanation = (
                f"Comparing index {j} ({arr[j]}) with index {j + 1} ({arr[j + 1]})."
            )
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                explanation += " Swapped to ensure the greater value bubbles right."
            else:
                explanation += " Already in order."

            sorted_part = list(range(n - i, n)) if i > 0 else []
            steps.append(
                _make_step(
                    "Bubble Sort",
                    arr,
                    [j, j + 1],
                    sorted_part,
                    explanation,
                    step,
                )
            )
            step += 1
        if not swapped:
            break

    steps.append(_complete_step("Bubble Sort", arr, step))
    return steps


def generate_selection_sort_steps(values: List[int]) -> List[Dict[str, Any]]:
    arr = list(values)
    n = len(arr)
    steps: List[Dict[str, Any]] = []
    step = 1
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            explanation = (
                f"Comparing index {j} ({arr[j]}) with current minimum at index {min_idx} ({arr[min_idx]})."
            )
            if arr[j] < arr[min_idx]:
                min_idx = j
                explanation += " New minimum found."
            steps.append(
                _make_step(
                    "Selection Sort",
                    arr,
                    [min_idx, j],
                    list(range(i)),
                    explanation,
                    step,
                )
            )
            step += 1
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            explanation = f"Swapping index {i} with minimum index {min_idx}."
            highlight = [i, min_idx]
        else:
            explanation = f"Element at index {i} is already the smallest in the remaining array."
            highlight = [i]
        steps.append(
            _make_step(
                "Selection Sort",
                arr,
                highlight,
                list(range(i + 1)),
                explanation,
                step,
            )
        )
        step += 1
    steps.append(_complete_step("Selection Sort", arr, step))
    return steps


def generate_insertion_sort_steps(values: List[int]) -> List[Dict[str, Any]]:
    arr = list(values)
    steps: List[Dict[str, Any]] = []
    n = len(arr)
    step = 1
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        steps.append(
            _make_step(
                "Insertion Sort",
                arr,
                [i],
                list(range(i)),
                f"Preparing to insert value {key} from index {i} into the sorted left portion.",
                step,
            )
        )
        step += 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            steps.append(
                _make_step(
                    "Insertion Sort",
                    arr,
                    [j, j + 1],
                    list(range(i + 1)),
                    f"Shifted {arr[j]} right to make room for {key}.",
                    step,
                )
            )
            step += 1
            j -= 1
        arr[j + 1] = key
        steps.append(
            _make_step(
                "Insertion Sort",
                arr,
                [j + 1],
                list(range(i + 1)),
                f"Placed {key} at index {j + 1}. Left portion remains sorted.",
                step,
            )
        )
        step += 1
    steps.append(_complete_step("Insertion Sort", arr, step))
    return steps


def generate_merge_sort_steps(values: List[int]) -> List[Dict[str, Any]]:
    arr = list(values)
    steps: List[Dict[str, Any]] = []
    step = 1

    def merge(l: int, m: int, r: int) -> None:
        nonlocal step
        left = arr[l : m + 1]
        right = arr[m + 1 : r + 1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                explanation = (
                    f"Placed {left[i]} from left half into position {k}."
                )
                i += 1
            else:
                arr[k] = right[j]
                explanation = (
                    f"Placed {right[j]} from right half into position {k}."
                )
                j += 1
            steps.append(
                _make_step(
                    "Merge Sort",
                    arr,
                    list(range(l, r + 1)),
                    list(range(l, k + 1)),
                    explanation,
                    step,
                )
            )
            step += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            steps.append(
                _make_step(
                    "Merge Sort",
                    arr,
                    list(range(l, r + 1)),
                    list(range(l, k + 1)),
                    f"Copy remaining left value {left[i]} to index {k}.",
                    step,
                )
            )
            step += 1
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            steps.append(
                _make_step(
                    "Merge Sort",
                    arr,
                    list(range(l, r + 1)),
                    list(range(l, k + 1)),
                    f"Copy remaining right value {right[j]} to index {k}.",
                    step,
                )
            )
            step += 1
            j += 1
            k += 1

    def merge_sort(l: int, r: int) -> None:
        if l >= r:
            return
        m = (l + r) // 2
        merge_sort(l, m)
        merge_sort(m + 1, r)
        merge(l, m, r)

    merge_sort(0, len(arr) - 1)
    steps.append(_complete_step("Merge Sort", arr, step))
    return steps


def generate_quick_sort_steps(values: List[int]) -> List[Dict[str, Any]]:
    arr = list(values)
    steps: List[Dict[str, Any]] = []
    n = len(arr)
    step = 1
    sorted_positions: set[int] = set()

    stack: List[tuple[int, int]] = [(0, n - 1)]
    while stack:
        low, high = stack.pop()
        if low >= high:
            sorted_positions.update(range(low, high + 1))
            continue
        pivot = arr[high]
        steps.append(
            _make_step(
                "Quick Sort",
                arr,
                list(range(low, high + 1)),
                sorted(sorted_positions),
                f"Partitioning range [{low}, {high}] using pivot {pivot} (index {high}).",
                step,
            )
        )
        step += 1
        i = low - 1
        for j in range(low, high):
            explanation = f"Compare index {j} ({arr[j]}) to pivot {pivot}."
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                explanation += f" Move value {arr[i]} to the left partition."
            else:
                explanation += " Keep it in the right partition."
            steps.append(
                _make_step(
                    "Quick Sort",
                    arr,
                    [j, high],
                    sorted(sorted_positions),
                    explanation,
                    step,
                )
            )
            step += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_index = i + 1
        sorted_positions.add(pivot_index)
        steps.append(
            _make_step(
                "Quick Sort",
                arr,
                [pivot_index],
                sorted(sorted_positions),
                f"Placed pivot {arr[pivot_index]} at index {pivot_index}. Left partition < pivot, right >= pivot.",
                step,
            )
        )
        step += 1
        stack.append((low, pivot_index - 1))
        stack.append((pivot_index + 1, high))

    steps.append(_complete_step("Quick Sort", arr, step))
    return steps


def generate_heap_sort_steps(values: List[int]) -> List[Dict[str, Any]]:
    arr = list(values)
    n = len(arr)
    steps: List[Dict[str, Any]] = []
    step = 1
    sorted_positions: set[int] = set()

    def record(explanation: str, highlights: List[int]) -> None:
        nonlocal step
        steps.append(
            _make_step(
                "Heap Sort",
                arr,
                highlights,
                sorted(sorted_positions),
                explanation,
                step,
            )
        )
        step += 1

    def heapify(heap_size: int, root: int) -> None:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < heap_size:
            explanation = (
                f"Compare left child index {left} ({arr[left]}) with root index {root} ({arr[largest]})."
            )
            if arr[left] > arr[largest]:
                largest = left
                explanation += " Left child is larger."
            else:
                explanation += " Root stays larger."
            record(explanation, [root, left])

        if right < heap_size:
            explanation = (
                f"Compare right child index {right} ({arr[right]}) with current largest index {largest} ({arr[largest]})."
            )
            if arr[right] > arr[largest]:
                largest = right
                explanation += " Right child becomes new largest."
            else:
                explanation += " Largest remains unchanged."
            record(explanation, [largest, right])

        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]
            record(
                f"Swapped index {root} with child index {largest} to maintain heap property.",
                [root, largest],
            )
            heapify(heap_size, largest)

    # Build max heap
    for idx in range(n // 2 - 1, -1, -1):
        heapify(n, idx)

    # Extract elements
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sorted_positions.add(end)
        record(
            f"Move current max {arr[end]} to index {end}; heap size reduces to {end}.",
            [0, end],
        )
        heapify(end, 0)

    sorted_positions.update(range(n))
    steps.append(_complete_step("Heap Sort", arr, step))
    return steps


def _make_grid_step(
    algorithm: str,
    step_number: int,
    start: GridPoint,
    end: GridPoint,
    barriers: List[GridPoint],
    grid_size: Dict[str, int],
    visited: List[GridPoint],
    path: List[GridPoint],
    frontier: Optional[List[GridPoint]] = None,
    explanation: str = "",
    is_final: bool = False,
) -> Dict[str, Any]:
    return {
        "status": "success",
        "type": "visualization_step",
        "algorithm": algorithm,
        "step": step_number,
        "isFinal": is_final,
        "data": {
            "grid": {
                "start": list(start),
                "end": list(end),
                "barriers": [list(b) for b in barriers],
                "grid_size": grid_size,
                "visited": [list(v) for v in visited],
                "path": [list(p) for p in path],
                "frontier": [list(f) for f in frontier] if frontier else [],
            }
        },
        "explanation": explanation,
    }


def _grid_search(
    graph_data: Dict[str, Any], algorithm: str
) -> List[Dict[str, Any]]:
    # Default to a 10x10 grid if not explicitly specified
    rows = graph_data.get("grid_size", {}).get("rows", 10)
    cols = graph_data.get("grid_size", {}).get("cols", 10)
    start_list = graph_data.get("start", [0, 0])
    end_list = graph_data.get("end", [0, 0])
    start = (int(start_list[0]), int(start_list[1]))
    end = (int(end_list[0]), int(end_list[1]))
    barriers_set = {
        (int(b[0]), int(b[1])) for b in graph_data.get("barriers", [])
    }

    steps: List[Dict[str, Any]] = []
    visited: List[GridPoint] = []
    parents: Dict[GridPoint, GridPoint] = {}
    step_num = 1

    def record_state(current: GridPoint, frontier: List[GridPoint], note: str) -> None:
        nonlocal step_num
        path = _reconstruct_path(parents, current) if current in parents or current == start else []
        steps.append(
            _make_grid_step(
                algorithm=algorithm,
                step_number=step_num,
                start=start,
                end=end,
                barriers=list(barriers_set),
                grid_size={"rows": rows, "cols": cols},
                visited=list(visited),
                path=path,
                frontier=list(frontier),
                explanation=note,
                is_final=False,
            )
        )
        step_num += 1

    if algorithm.lower().startswith("breadth-first") or algorithm.lower().startswith("bfs"):
        from collections import deque

        queue: deque[GridPoint] = deque()
        queue.append(start)
        parents[start] = start
        # Show start as visited for the first render, but don't block expansion
        visited.append(start)
        record_state(start, list(queue), "Initialize BFS with start node.")

        while queue:
            current = queue.popleft()
            if current == end:
                visited.append(current)
                record_state(current, list(queue), "Reached the target. Reconstructing path.")
                break
            if current not in visited:
                visited.append(current)
            for nb in _neighbors(current, rows, cols):
                if nb in barriers_set or nb in visited or nb in queue:
                    continue
                parents[nb] = current
                queue.append(nb)
            record_state(current, list(queue), f"Exploring neighbors of {current}.")

    elif algorithm.lower().startswith("depth-first") or algorithm.lower().startswith("dfs"):
        stack: List[GridPoint] = [start]
        parents[start] = start
        visited.append(start)
        record_state(start, list(stack), "Initialize DFS with start node.")

        while stack:
            current = stack.pop()
            if current == end:
                visited.append(current)
                record_state(current, list(stack), "Reached the target. Reconstructing path.")
                break
            if current not in visited:
                visited.append(current)
            neighbors = _neighbors(current, rows, cols)
            for nb in neighbors:
                if nb in barriers_set or nb in visited or nb in stack:
                    continue
                parents[nb] = current
                stack.append(nb)
            record_state(current, list(stack), f"Exploring neighbors of {current}.")

    else:
        # Dijkstra and A* use a priority queue; heuristic only for A*
        import heapq
        use_heuristic = "a*" in algorithm.lower() or "a-star" in algorithm.lower()

        def heuristic(p: GridPoint, q: GridPoint) -> int:
            return abs(p[0] - q[0]) + abs(p[1] - q[1])

        pq: List[tuple[int, GridPoint]] = []
        dist: Dict[GridPoint, int] = {start: 0}
        parents[start] = start
        heapq.heappush(pq, (0, start))
        visited.append(start)
        record_state(start, [start], "Initialize search with start node.")

        while pq:
            _, current = heapq.heappop(pq)
            visited.append(current)

            if current == end:
                record_state(current, [], "Reached the target. Reconstructing path.")
                break

            for nb in _neighbors(current, rows, cols):
                if nb in barriers_set:
                    continue
                new_cost = dist[current] + 1
                if nb not in dist or new_cost < dist[nb]:
                    dist[nb] = new_cost
                    priority = new_cost + (heuristic(nb, end) if use_heuristic else 0)
                    parents[nb] = current
                    heapq.heappush(pq, (priority, nb))
            frontier = [pt for _, pt in pq]
            record_state(current, frontier, f"Exploring neighbors of {current}.")

    # Final step with full path highlighted (if reachable)
    final_path = _reconstruct_path(parents, end)
    steps.append(
        _make_grid_step(
            algorithm=algorithm,
            step_number=step_num,
            start=start,
            end=end,
            barriers=list(barriers_set),
            grid_size={"rows": rows, "cols": cols},
            visited=list(visited),
            path=final_path,
            frontier=[],
            explanation="Path reconstruction complete." if final_path else "No path found.",
            is_final=True,
        )
    )
    return steps


def generate_dijkstra_steps(graph_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return _grid_search(graph_data, "Dijkstra's Algorithm")


def generate_astar_steps(graph_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return _grid_search(graph_data, "A* (A-Star)")


def generate_bfs_steps(graph_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return _grid_search(graph_data, "Breadth-First Search (BFS)")


def generate_dfs_steps(graph_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return _grid_search(graph_data, "Depth-First Search (DFS)")


ALGORITHM_BUILDERS: Dict[str, Callable[[List[int]], List[Dict[str, Any]]]] = {
    "Bubble Sort": generate_bubble_sort_steps,
    "Selection Sort": generate_selection_sort_steps,
    "Insertion Sort": generate_insertion_sort_steps,
    "Merge Sort": generate_merge_sort_steps,
    "Quick Sort": generate_quick_sort_steps,
    "Heap Sort": generate_heap_sort_steps,
}

PATHFINDING_BUILDERS: Dict[str, Callable[[Dict[str, Any]], List[Dict[str, Any]]]] = {
    "Dijkstra's Algorithm": generate_dijkstra_steps,
    "A* (A-Star)": generate_astar_steps,
    "Breadth-First Search (BFS)": generate_bfs_steps,
    "Depth-First Search (DFS)": generate_dfs_steps,
}

ALGORITHM_ALIASES: Dict[str, str] = dict(SORTING_SELECTION_KEYWORDS)
PATHFINDING_ALIASES: Dict[str, str] = dict(PATHFINDING_SELECTION_KEYWORDS)

ALGORITHM_EXPLANATIONS: Dict[str, str] = {
    "Bubble Sort": (
        "THEORY:\n"
        "Bubble Sort works by repeatedly stepping through the list, comparing adjacent elements and swapping them if they are in the wrong order. "
        "The algorithm gets its name because smaller elements 'bubble' to the top of the list with each pass. "
        "In each iteration, the largest unsorted element moves to its correct position at the end of the array.\n\n"
        "HOW IT WORKS:\n"
        "1. Start from the first element and compare it with the next element\n"
        "2. If the first element is greater than the second, swap them\n"
        "3. Move to the next pair and repeat\n"
        "4. After one complete pass, the largest element is in its final position\n"
        "5. Repeat the process for the remaining unsorted portion\n"
        "6. Continue until no swaps are needed in a complete pass\n\n"
        "STATISTICS:\n"
        "• Time Complexity: Best O(n), Average O(n²), Worst O(n²)\n"
        "• Space Complexity: O(1) - in-place sorting\n"
        "• Stability: Stable (maintains relative order of equal elements)\n"
        "• Adaptive: Yes (can detect if array is already sorted)\n"
        "• In-place: Yes\n"
        "• Use Case: Educational purposes, small datasets, or when simplicity is preferred"
    ),
    "Selection Sort": (
        "THEORY:\n"
        "Selection Sort divides the input list into two parts: a sorted sublist at the beginning and an unsorted sublist at the end. "
        "The algorithm repeatedly finds the minimum element from the unsorted portion and places it at the end of the sorted portion.\n\n"
        "HOW IT WORKS:\n"
        "1. Find the minimum element in the unsorted portion of the array\n"
        "2. Swap it with the first element of the unsorted portion\n"
        "3. The sorted portion grows by one element\n"
        "4. Repeat steps 1-3 for the remaining unsorted portion\n"
        "5. Continue until the entire array is sorted\n\n"
        "STATISTICS:\n"
        "• Time Complexity: Best O(n²), Average O(n²), Worst O(n²)\n"
        "• Space Complexity: O(1) - in-place sorting\n"
        "• Stability: Not stable (may change relative order of equal elements)\n"
        "• Adaptive: No (always performs the same number of comparisons)\n"
        "• In-place: Yes\n"
        "• Use Case: Small datasets, when memory writes are expensive, or when simplicity is needed"
    ),
    "Insertion Sort": (
        "THEORY:\n"
        "Insertion Sort builds the sorted array one element at a time, similar to how you might sort playing cards in your hands. "
        "It takes each element from the unsorted portion and inserts it into its correct position in the sorted portion.\n\n"
        "HOW IT WORKS:\n"
        "1. Start with the second element (index 1) as the key\n"
        "2. Compare the key with elements in the sorted portion (to its left)\n"
        "3. Shift all elements greater than the key one position to the right\n"
        "4. Insert the key into its correct position\n"
        "5. Move to the next element and repeat\n"
        "6. Continue until all elements are processed\n\n"
        "STATISTICS:\n"
        "• Time Complexity: Best O(n), Average O(n²), Worst O(n²)\n"
        "• Space Complexity: O(1) - in-place sorting\n"
        "• Stability: Stable (maintains relative order of equal elements)\n"
        "• Adaptive: Yes (efficient for nearly sorted arrays)\n"
        "• In-place: Yes\n"
        "• Use Case: Small datasets, nearly sorted arrays, or as part of hybrid sorting algorithms"
    ),
    "Merge Sort": (
        "THEORY:\n"
        "Merge Sort is a divide-and-conquer algorithm that divides the array into two halves, sorts each half recursively, "
        "and then merges the two sorted halves back together. It's one of the most efficient sorting algorithms.\n\n"
        "HOW IT WORKS:\n"
        "1. Divide the array into two halves\n"
        "2. Recursively sort the left half\n"
        "3. Recursively sort the right half\n"
        "4. Merge the two sorted halves:\n"
        "   - Compare elements from both halves\n"
        "   - Take the smaller element and place it in the result\n"
        "   - Continue until one half is exhausted\n"
        "   - Copy remaining elements from the other half\n"
        "5. The merged result is the sorted array\n\n"
        "STATISTICS:\n"
        "• Time Complexity: Best O(n log n), Average O(n log n), Worst O(n log n)\n"
        "• Space Complexity: O(n) - requires additional memory for merging\n"
        "• Stability: Stable (maintains relative order of equal elements)\n"
        "• Adaptive: No (always performs the same operations regardless of input)\n"
        "• In-place: No (requires O(n) extra space)\n"
        "• Use Case: Large datasets, when stability is required, external sorting, or when consistent performance is needed"
    ),
    "Quick Sort": (
        "THEORY:\n"
        "Quick Sort is a divide-and-conquer algorithm that picks a 'pivot' element and partitions the array around the pivot. "
        "Elements smaller than the pivot go to the left, and elements greater go to the right. "
        "The process is repeated recursively for the sub-arrays.\n\n"
        "HOW IT WORKS:\n"
        "1. Choose a pivot element (commonly the last element)\n"
        "2. Partition the array:\n"
        "   - Rearrange elements so all elements < pivot are on the left\n"
        "   - All elements > pivot are on the right\n"
        "   - Place the pivot in its correct sorted position\n"
        "3. Recursively apply Quick Sort to the left sub-array\n"
        "4. Recursively apply Quick Sort to the right sub-array\n"
        "5. Base case: arrays of size 0 or 1 are already sorted\n\n"
        "STATISTICS:\n"
        "• Time Complexity: Best O(n log n), Average O(n log n), Worst O(n²)\n"
        "• Space Complexity: O(log n) average, O(n) worst case (due to recursion stack)\n"
        "• Stability: Not stable (may change relative order of equal elements)\n"
        "• Adaptive: Yes (efficient for many real-world data distributions)\n"
        "• In-place: Yes (with proper implementation)\n"
        "• Use Case: General-purpose sorting, large datasets, when average-case performance matters more than worst-case"
    ),
    "Heap Sort": (
        "THEORY:\n"
        "Heap Sort uses a binary heap data structure to sort elements. It first builds a max heap from the input array, "
        "then repeatedly extracts the maximum element from the heap and places it at the end of the sorted portion.\n\n"
        "HOW IT WORKS:\n"
        "1. Build a max heap from the input array:\n"
        "   - Start from the last non-leaf node\n"
        "   - Heapify each node to maintain heap property\n"
        "2. Extract elements from the heap:\n"
        "   - Swap the root (max element) with the last element\n"
        "   - Reduce heap size by one\n"
        "   - Heapify the root to restore heap property\n"
        "3. Repeat step 2 until the heap is empty\n"
        "4. The array is now sorted in ascending order\n\n"
        "STATISTICS:\n"
        "• Time Complexity: Best O(n log n), Average O(n log n), Worst O(n log n)\n"
        "• Space Complexity: O(1) - in-place sorting (if heapify is done in-place)\n"
        "• Stability: Not stable (may change relative order of equal elements)\n"
        "• Adaptive: No (always performs the same operations)\n"
        "• In-place: Yes\n"
        "• Use Case: When guaranteed O(n log n) performance is needed, embedded systems, or when worst-case O(n²) of Quick Sort is unacceptable"
    ),
}

PATHFINDING_EXPLANATIONS: Dict[str, str] = {
    "Dijkstra's Algorithm": (
        "THEORY:\n"
        "Dijkstra's Algorithm is a graph search algorithm that finds the shortest path from a source node to all other nodes "
        "in a weighted graph with non-negative edge weights. It uses a greedy approach, always selecting the unvisited node "
        "with the smallest known distance.\n\n"
        "HOW IT WORKS:\n"
        "1. Initialize distances: set source distance to 0, all others to infinity\n"
        "2. Mark all nodes as unvisited\n"
        "3. Select the unvisited node with the smallest distance\n"
        "4. For each neighbor of the current node, calculate tentative distance\n"
        "5. If tentative distance is smaller, update the neighbor's distance\n"
        "6. Mark current node as visited\n"
        "7. Repeat steps 3-6 until all nodes are visited or target is reached\n\n"
        "STATISTICS:\n"
        "• Time Complexity: O(V²) for simple implementation, O((V + E) log V) with priority queue\n"
        "• Space Complexity: O(V) for distance and visited arrays\n"
        "• Optimal: Yes (finds shortest path in weighted graphs)\n"
        "• Use Case: GPS navigation, network routing, social network analysis, game pathfinding"
    ),
    "A* (A-Star)": (
        "THEORY:\n"
        "A* is an informed search algorithm that finds the shortest path from a start node to a goal node. "
        "It combines the benefits of Dijkstra's algorithm (optimal path) with a heuristic function that estimates "
        "the distance to the goal, making it more efficient than Dijkstra's for single-target searches.\n\n"
        "HOW IT WORKS:\n"
        "1. Initialize: add start node to open set with f(n) = g(n) + h(n)\n"
        "2. While open set is not empty:\n"
        "   - Select node with lowest f(n) from open set\n"
        "   - If this is the goal, reconstruct and return path\n"
        "   - Move current node to closed set\n"
        "   - For each neighbor:\n"
        "     * Calculate tentative g(n) = current g(n) + edge cost\n"
        "     * If neighbor not in open/closed or new path is better, update\n"
        "     * Calculate f(n) = g(n) + h(n) where h(n) is heuristic\n"
        "3. Return failure if goal not reached\n\n"
        "STATISTICS:\n"
        "• Time Complexity: O(b^d) worst case, but much better with good heuristic\n"
        "• Space Complexity: O(b^d) for storing all nodes\n"
        "• Optimal: Yes (with admissible heuristic)\n"
        "• Use Case: Game AI pathfinding, robotics navigation, puzzle solving, route planning"
    ),
    "Breadth-First Search (BFS)": (
        "THEORY:\n"
        "Breadth-First Search is a graph traversal algorithm that explores all nodes at the current depth level "
        "before moving to nodes at the next depth level. It uses a queue data structure and guarantees finding "
        "the shortest path in unweighted graphs.\n\n"
        "HOW IT WORKS:\n"
        "1. Start from the source node, mark it as visited\n"
        "2. Add source node to a queue\n"
        "3. While queue is not empty:\n"
        "   - Dequeue a node from the front\n"
        "   - Visit all unvisited neighbors of this node\n"
        "   - Mark neighbors as visited and enqueue them\n"
        "   - Record parent/previous node for path reconstruction\n"
        "4. Continue until queue is empty or target is found\n"
        "5. Reconstruct path by following parent pointers\n\n"
        "STATISTICS:\n"
        "• Time Complexity: O(V + E) where V is vertices, E is edges\n"
        "• Space Complexity: O(V) for queue and visited tracking\n"
        "• Optimal: Yes (for unweighted graphs, finds shortest path)\n"
        "• Use Case: Shortest path in unweighted graphs, level-order tree traversal, social network analysis, puzzle solving"
    ),
    "Depth-First Search (DFS)": (
        "THEORY:\n"
        "Depth-First Search is a graph traversal algorithm that explores as far as possible along each branch "
        "before backtracking. It uses a stack (recursion or explicit stack) and is useful for exploring all "
        "possible paths or detecting cycles.\n\n"
        "HOW IT WORKS:\n"
        "1. Start from the source node, mark it as visited\n"
        "2. For each unvisited neighbor:\n"
        "   - Recursively visit the neighbor\n"
        "   - Mark as visited before recursion\n"
        "   - Record parent/previous node\n"
        "3. Backtrack when no more unvisited neighbors exist\n"
        "4. Continue until all reachable nodes are visited\n"
        "5. Reconstruct path if target was found\n\n"
        "STATISTICS:\n"
        "• Time Complexity: O(V + E) where V is vertices, E is edges\n"
        "• Space Complexity: O(V) for recursion stack or explicit stack\n"
        "• Optimal: No (does not guarantee shortest path)\n"
        "• Use Case: Maze solving, cycle detection, topological sorting, connected components, backtracking problems"
    ),
}


@dataclass
class AlgorithmRunner:
    algorithm: str
    steps: List[Dict[str, Any]]
    index: int = 0

    def step(self) -> Dict[str, Any]:
        if not self.steps:
            return _make_step(
                self.algorithm,
                [],
                [],
                [],
                "No steps available.",
                0,
            )
        result = self.steps[self.index]
        if self.index < len(self.steps) - 1:
            self.index += 1
        return result


@dataclass
class AlgorithmSession:
    algorithm: Optional[str] = None
    state: Optional[AlgorithmRunner] = None
    stage: str = "idle"
    pending_algorithm: Optional[str] = None

    def reset(self) -> None:
        self.algorithm = None
        self.state = None
        self.stage = "idle"
        self.pending_algorithm = None


class AlgorithmSessionManager:
    VISUALIZE_RE = re.compile(
        r"^\s*visualize\s+(?P<algo>[a-zA-Z ]+)\s+on\s*\[(?P<array>[^\]]*)\]\s*$",
        re.IGNORECASE,
    )

    EXPLAIN_RE = re.compile(r"^\s*explain\s*$", re.IGNORECASE)
    NEXT_RE = re.compile(r"^\s*next\s*$", re.IGNORECASE)
    RESET_RE = re.compile(r"^\s*reset\s*$", re.IGNORECASE)

    def __init__(self) -> None:
        self.sessions: Dict[str, AlgorithmSession] = {}

    def _get_or_create(self, session_id: str) -> AlgorithmSession:
        if session_id not in self.sessions:
            self.sessions[session_id] = AlgorithmSession()
        return self.sessions[session_id]

    def handle_command(self, session_id: str, command: str) -> Dict[str, Any]:
        import logging
        logger = logging.getLogger(__name__)
        
        session = self._get_or_create(session_id)
        stripped = command.strip()
        lowered = stripped.lower()

        log_msg = (f"[Command Handler] Received command: session_id={session_id}, "
                  f"stage={session.stage}, pending_algorithm={session.pending_algorithm}, "
                  f"command_length={len(stripped)}, command_preview={stripped[:100]}")
        logger.info(log_msg)
        print(log_msg)  # Also print for immediate visibility

        if not stripped:
            raise ValueError(
                "Unknown command or invalid syntax. Type 'menu' to see available options."
            )

        if lowered == "menu":
            session.reset()
            session.stage = "menu"
            return _menu_payload()

        # If in sorting_menu stage, prioritize algorithm selection over menu selection
        if session.stage == "sorting_menu":
            selection_algorithm = _match_sorting_selection(lowered)
            if not selection_algorithm:
                # Try to find algorithm keywords within the input
                for keyword, algo_name in SORTING_SELECTION_KEYWORDS.items():
                    if keyword in lowered:
                        selection_algorithm = algo_name
                        break
            
            if selection_algorithm:
                session.pending_algorithm = selection_algorithm
                session.stage = "await_array"
                return _prompt_array_payload(selection_algorithm)

        # If in pathfinding_menu stage, prioritize algorithm selection over menu selection
        if session.stage == "pathfinding_menu":
            selection_algorithm = _match_pathfinding_selection(lowered)
            if not selection_algorithm:
                # Try to find algorithm keywords within the input
                for keyword, algo_name in PATHFINDING_SELECTION_KEYWORDS.items():
                    if keyword in lowered:
                        selection_algorithm = algo_name
                        break
            
            if selection_algorithm:
                session.pending_algorithm = selection_algorithm
                session.stage = "await_grid"
                return _prompt_graph_payload(selection_algorithm)

        stripped_clean_for_grid = stripped.strip()
        looks_like_json_grid = (
            stripped_clean_for_grid.startswith("{")
            and ("\"start\"" in stripped_clean_for_grid or "'start'" in stripped_clean_for_grid)
        )

        # Handle duplicate grid config submission when already visualizing
        if session.stage == "visualizing" and session.algorithm and session.state and looks_like_json_grid:
            import logging
            logger = logging.getLogger(__name__)
            log_msg = "[Grid Handler] Already visualizing, returning current step"
            logger.info(log_msg)
            print(log_msg)
            if session.state.steps:
                current_idx = session.state.index if session.state.index < len(session.state.steps) else len(session.state.steps) - 1
                return session.state.steps[current_idx]

        # Handle grid configuration for pathfinding algorithms (check early to avoid conflicts)
        if session.stage == "await_grid" or (looks_like_json_grid and (session.pending_algorithm or session.algorithm)):
            import logging
            logger = logging.getLogger(__name__)
            log_msg = (f"[Grid Handler] Processing grid config: stage=await_grid, "
                      f"pending_algorithm={session.pending_algorithm}, "
                      f"command_preview={stripped[:200]}")
            logger.info(log_msg)
            print(log_msg)  # Also print for immediate visibility
            
            lowered_for_map = lowered.strip()
            
            # Check for default map selection
            if lowered_for_map in {"easy", "medium", "hard"}:
                log_msg = f"[Grid Handler] Default map requested: {lowered_for_map}"
                logger.info(log_msg)
                print(log_msg)
                if not session.pending_algorithm:
                    error_msg = "[Grid Handler] No pending algorithm for default map"
                    logger.error(error_msg)
                    print(error_msg)
                    raise ValueError("Select a pathfinding algorithm first.")
                
                grid_config = _generate_default_map(lowered_for_map)
                log_msg = (f"[Grid Handler] Generated default map: {lowered_for_map}, "
                          f"start={grid_config['start']}, end={grid_config['end']}, "
                          f"barriers_count={len(grid_config['barriers'])}")
                logger.info(log_msg)
                print(log_msg)
                builder = PATHFINDING_BUILDERS[session.pending_algorithm]
                steps = builder(grid_config)
                session.algorithm = session.pending_algorithm
                session.state = AlgorithmRunner(session.algorithm, steps)
                session.pending_algorithm = None
                session.stage = "visualizing"
                log_msg = (f"[Grid Handler] Default map processed successfully, "
                          f"algorithm={session.algorithm}, steps_count={len(steps)}")
                logger.info(log_msg)
                print(log_msg)
                return session.state.step()
            
            # Check for grid configuration JSON input
            # Format: {"start": [row, col], "end": [row, col], "barriers": [[row, col], ...]}
            # Try to parse as JSON - check if it looks like JSON first
            stripped_clean = stripped_clean_for_grid
            log_msg = (f"[Grid Handler] Checking for JSON: starts_with_brace={stripped_clean.startswith('{')}, "
                      f"starts_with_bracket={stripped_clean.startswith('[')}")
            logger.info(log_msg)
            print(log_msg)
            
            if stripped_clean.startswith("{") or stripped_clean.startswith("["):
                try:
                    import json
                    log_msg = f"[Grid Handler] Attempting to parse JSON: {stripped_clean[:200]}"
                    logger.info(log_msg)
                    print(log_msg)
                    grid_config = json.loads(stripped_clean)
                    log_msg = f"[Grid Handler] JSON parsed successfully: {grid_config}"
                    logger.info(log_msg)
                    print(log_msg)
                    
                    # Resolve algorithm
                    algo_from_payload = grid_config.get("algorithm")
                    algo_candidate = algo_from_payload or session.pending_algorithm or session.algorithm

                    if not algo_candidate:
                        error_msg = "[Grid Handler] No pending algorithm for grid config"
                        logger.error(error_msg)
                        print(error_msg)
                        raise ValueError("Select a pathfinding algorithm first.")

                    algo_key = _normalize_algo_token(str(algo_candidate))
                    canonical_algo = PATHFINDING_ALIASES.get(algo_key, None)
                    if not canonical_algo and algo_candidate in PATHFINDING_BUILDERS:
                        canonical_algo = algo_candidate
                    if not canonical_algo:
                        error_msg = f"[Grid Handler] Unknown pathfinding algorithm: {algo_candidate}"
                        logger.error(error_msg)
                        print(error_msg)
                        raise ValueError(f"Unknown algorithm. Supported: {', '.join(sorted(PATHFINDING_BUILDERS.keys()))}.")
                    
                    # Validate grid config - check if it's a dict with expected keys
                    if isinstance(grid_config, dict):
                        log_msg = f"[Grid Handler] Grid config is dict, checking keys: {list(grid_config.keys())}"
                        logger.info(log_msg)
                        print(log_msg)
                        if "start" not in grid_config or "end" not in grid_config:
                            error_msg = f"[Grid Handler] Missing start/end: keys={list(grid_config.keys())}"
                            logger.error(error_msg)
                            print(error_msg)
                            raise ValueError("Grid configuration must include 'start' and 'end' points.")
                        
                        if "barriers" not in grid_config:
                            grid_config["barriers"] = []
                        
                        log_msg = (f"[Grid Handler] Grid config validated: "
                                  f"start={grid_config['start']}, end={grid_config['end']}, "
                                  f"barriers_count={len(grid_config['barriers'])}")
                        logger.info(log_msg)
                        print(log_msg)
                        
                        builder = PATHFINDING_BUILDERS[canonical_algo]
                        log_msg = f"[Grid Handler] Calling builder for {canonical_algo}"
                        logger.info(log_msg)
                        print(log_msg)
                        steps = builder(grid_config)
                        session.algorithm = canonical_algo
                        session.state = AlgorithmRunner(session.algorithm, steps)
                        session.pending_algorithm = None
                        session.stage = "visualizing"
                        log_msg = (f"[Grid Handler] Grid config processed successfully, "
                                  f"algorithm={session.algorithm}, steps_count={len(steps)}")
                        logger.info(log_msg)
                        print(log_msg)
                        return session.state.step()
                    else:
                        warn_msg = f"[Grid Handler] Grid config is not a dict: type={type(grid_config)}"
                        logger.warning(warn_msg)
                        print(warn_msg)
                except json.JSONDecodeError as e:
                    error_msg = f"[Grid Handler] JSON decode error: {e}, input={stripped_clean[:200]}"
                    logger.error(error_msg)
                    print(error_msg)
                    # If JSON parsing fails, continue to other handlers
                    pass
                except Exception as e:
                    error_msg = f"[Grid Handler] Error processing grid config: {e}"
                    logger.error(error_msg, exc_info=True)
                    print(error_msg)
                    import traceback
                    print(traceback.format_exc())
                    # Re-raise other exceptions
                    raise ValueError(f"Error processing grid configuration: {str(e)}")
            else:
                warn_msg = f"[Grid Handler] Command doesn't look like JSON: {stripped_clean[:100]}"
                logger.warning(warn_msg)
                print(warn_msg)
            
            # If we're in await_grid stage but didn't match anything, provide helpful error
            error_msg = f"[Grid Handler] No match found for grid config: command={stripped[:200]}"
            logger.error(error_msg)
            print(error_msg)
            raise ValueError(
                "Invalid grid configuration. "
                "Send JSON with 'start', 'end', and 'barriers', or use 'easy', 'medium', or 'hard' for preset maps."
            )

        # Check for menu selection keywords within the input (not just exact match)
        # First check for numbers (only if not in sorting_menu or pathfinding_menu)
        if lowered in MENU_SELECTION_NUMBERS["sorting"]:
            session.stage = "sorting_menu"
            session.pending_algorithm = None
            return _sorting_menu_payload()
        
        if lowered in MENU_SELECTION_NUMBERS["pathfinding"]:
            session.stage = "pathfinding_menu"
            session.pending_algorithm = None
            return _pathfinding_menu_payload()
        
        if lowered in MENU_SELECTION_NUMBERS["data_structures"]:
            session.stage = "menu"
            return _coming_soon_payload("Data Structures")

        # Check if any sorting keyword appears in the input
        if any(keyword in lowered for keyword in MENU_SORTING_KEYWORDS):
            session.stage = "sorting_menu"
            session.pending_algorithm = None
            return _sorting_menu_payload()

        # Check if any pathfinding keyword appears in the input
        if any(keyword in lowered for keyword in MENU_PATHFINDING_KEYWORDS):
            session.stage = "pathfinding_menu"
            session.pending_algorithm = None
            return _pathfinding_menu_payload()

        # Check if any data structure keyword appears in the input
        if any(keyword in lowered for keyword in MENU_DATA_STRUCTURE_KEYWORDS):
            session.stage = "menu"
            return _coming_soon_payload("Data Structures")

        # Check for algorithm selection - try exact match first, then search within input
        selection_algorithm = _match_sorting_selection(lowered)
        if not selection_algorithm:
            # Try to find algorithm keywords within the input
            for keyword, algo_name in SORTING_SELECTION_KEYWORDS.items():
                if keyword in lowered:
                    selection_algorithm = algo_name
                    break
        
        if selection_algorithm:
            session.pending_algorithm = selection_algorithm
            session.stage = "await_array"
            return _prompt_array_payload(selection_algorithm)

        if session.stage == "await_array" and _is_array_literal(stripped):
            if not session.pending_algorithm:
                raise ValueError(
                    "Select a sorting algorithm before entering the array."
                )
            array_values = _parse_array(stripped)
            builder = ALGORITHM_BUILDERS[session.pending_algorithm]
            steps = builder(array_values)
            session.algorithm = session.pending_algorithm
            session.state = AlgorithmRunner(session.algorithm, steps)
            session.pending_algorithm = None
            session.stage = "visualizing"
            return session.state.step()

        visualize_match = self.VISUALIZE_RE.match(command)
        if visualize_match:
            algo_key = visualize_match.group("algo").strip().lower()
            canonical = ALGORITHM_ALIASES.get(algo_key)
            if not canonical:
                raise ValueError(
                    f"Unknown algorithm. Supported: {', '.join(sorted(ALGORITHM_BUILDERS.keys()))}."
                )
            array_literal = visualize_match.group("array").strip()
            try:
                array_values = _parse_array(array_literal)
            except ValueError:
                raise ValueError(
                    "Invalid array literal. Use comma-separated integers inside brackets, e.g. [5, 2, 1]."
                )

            builder = ALGORITHM_BUILDERS[canonical]
            steps = builder(array_values)
            session.algorithm = canonical
            session.state = AlgorithmRunner(canonical, steps)
            session.pending_algorithm = None
            session.stage = "visualizing"
            return session.state.step()

        if self.NEXT_RE.match(command):
            if not session.state:
                raise ValueError(
                    "No active algorithm. Select one from the menu or use the visualize command."
                )
            return session.state.step()

        # Check for explain command - match "explain" anywhere in the input
        if "explain" in lowered:
            # Try to find which algorithm to explain from the input
            algorithm_to_explain = None
            
            # First check if there's an active algorithm
            if session.algorithm:
                algorithm_to_explain = session.algorithm
            
            # If no active algorithm, try to find algorithm name in the input
            if not algorithm_to_explain:
                # Check sorting algorithms
                for keyword, algo_name in SORTING_SELECTION_KEYWORDS.items():
                    if keyword in lowered:
                        algorithm_to_explain = algo_name
                        break
                
                # Check pathfinding algorithms if not found
                if not algorithm_to_explain:
                    for keyword, algo_name in PATHFINDING_SELECTION_KEYWORDS.items():
                        if keyword in lowered:
                            algorithm_to_explain = algo_name
                            break
            
            if not algorithm_to_explain:
                raise ValueError(
                    "No algorithm specified. Either select an algorithm first, or include the algorithm name in your request (e.g., 'explain bubble sort' or 'explain dijkstra')."
                )
            
            # Check both sorting and pathfinding explanations
            explanation = ALGORITHM_EXPLANATIONS.get(
                algorithm_to_explain, None
            )
            if not explanation:
                explanation = PATHFINDING_EXPLANATIONS.get(
                    algorithm_to_explain, "Explanation unavailable."
                )
            return {
                "status": "success",
                "type": "explanation",
                "algorithm": algorithm_to_explain,
                "explanation": explanation,
            }

        if self.RESET_RE.match(command):
            session.reset()
            return {
                "status": "success",
                "type": "info",
                "message": "Session reset.",
            }

        raise ValueError(
            "Unknown command or invalid syntax. Type 'menu' to restart or 'visualize bubble sort on [5,2,1]'."
        )


def _match_sorting_selection(token: str) -> Optional[str]:
    if token in SORTING_NUMBER_TO_ALGORITHM:
        return SORTING_NUMBER_TO_ALGORITHM[token]
    return SORTING_SELECTION_KEYWORDS.get(token)


def _normalize_algo_token(token: str) -> str:
    return token.strip().lower().replace('"', "'").replace("’", "'")


def _match_pathfinding_selection(token: str) -> Optional[str]:
    normalized = _normalize_algo_token(token)
    if normalized in PATHFINDING_NUMBER_TO_ALGORITHM:
        return PATHFINDING_NUMBER_TO_ALGORITHM[normalized]
    if normalized in PATHFINDING_ALIASES:
        return PATHFINDING_ALIASES[normalized]
    return None
 

def _menu_payload() -> Dict[str, Any]:
    return {
        "status": "success",
        "type": "menu",
        "message": MAIN_MENU_MESSAGE,
        "options": [
            {"id": "1", "label": "Sorting Algorithms"},
            {"id": "2", "label": "Pathfinding Algorithms"},
            {"id": "3", "label": "Data Structures (coming soon)"},
        ],
    }


def _sorting_menu_payload() -> Dict[str, Any]:
    return {
        "status": "success",
        "type": "sorting_menu",
        "message": SORTING_MENU_MESSAGE,
        "options": [
            {"id": "1", "label": "Bubble Sort"},
            {"id": "2", "label": "Merge Sort"},
            {"id": "3", "label": "Selection Sort"},
            {"id": "4", "label": "Insertion Sort"},
            {"id": "5", "label": "Quick Sort"},
            {"id": "6", "label": "Heap Sort"},
        ],
    }


def _pathfinding_menu_payload() -> Dict[str, Any]:
    return {
        "status": "success",
        "type": "pathfinding_menu",
        "message": PATHFINDING_MENU_MESSAGE,
        "options": [
            {"id": "1", "label": "Dijkstra's Algorithm"},
            {"id": "2", "label": "A* (A-Star)"},
            {"id": "3", "label": "Breadth-First Search (BFS)"},
            {"id": "4", "label": "Depth-First Search (DFS)"},
        ],
    }


def _prompt_array_payload(algorithm: str) -> Dict[str, Any]:
    return {
        "status": "success",
        "type": "await_array",
        "algorithm": algorithm,
        "message": (
            f"Enter the array for {algorithm} as comma-separated integers. "
            "Example: 5, 2, 9, 1. Type 'menu' to go back."
        ),
    }


def _prompt_graph_payload(algorithm: str) -> Dict[str, Any]:
    return {
        "status": "success",
        "type": "await_grid",
        "algorithm": algorithm,
        "grid_size": {"rows": 10, "cols": 10},
        "message": (
            f"Configure the grid for {algorithm}. "
            "You can:\n"
            "- Select start and end points\n"
            "- Draw barriers/walls\n"
            "- Or use preset maps: 'easy', 'medium', or 'hard'\n"
            "Type 'menu' to go back."
        ),
    }


def _generate_default_map(difficulty: str) -> Dict[str, Any]:
    """Generate default grid maps for easy, medium, and hard difficulty levels."""
    rows, cols = 10, 10
    barriers: List[List[int]] = []

    if difficulty == "easy":
        # Easy: few barriers, mostly open path
        barriers = [
            [2, 3],
            [2, 4],
            [2, 5],
            [5, 6],
            [6, 6],
            [7, 6],
        ]
        start = [0, 0]
        end = [9, 9]

    elif difficulty == "medium":
        # Medium: some maze-like structure
        barriers = [
            # Horizontal walls
            [1, 1],
            [1, 2],
            [1, 3],
            [3, 5],
            [3, 6],
            [3, 7],
            [6, 2],
            [6, 3],
            [6, 4],
            # Vertical walls
            [2, 4],
            [3, 4],
            [4, 4],
            [5, 7],
            [6, 7],
            [7, 7],
        ]
        start = [0, 0]
        end = [9, 9]

    elif difficulty == "hard":
        # Hard: denser maze with multiple paths
        barriers = [
            # Outer-ish ring
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [2, 7],
            [3, 7],
            [4, 7],
            [5, 7],
            [6, 7],
            [7, 7],
            [7, 6],
            [7, 5],
            [7, 4],
            [7, 3],
            [7, 2],
            [7, 1],
            # Inner barriers
            [3, 2],
            [3, 3],
            [3, 4],
            [4, 4],
            [5, 4],
            [5, 5],
            [5, 6],
            [2, 5],
            [4, 2],
            [6, 5],
        ]
        start = [0, 0]
        end = [9, 9]

    return {
        "start": start,
        "end": end,
        "barriers": barriers,
        "grid_size": {"rows": rows, "cols": cols},
    }


def _coming_soon_payload(topic: str) -> Dict[str, Any]:
    return {
        "status": "success",
        "type": "info",
        "message": f"{topic} visualizations are coming soon. Type 'menu' to go back.",
    }


def _is_array_literal(text: str) -> bool:
    stripped = text.strip()
    if stripped.startswith("[") and stripped.endswith("]"):
        inner = stripped[1:-1].strip()
        return True if not inner else bool(ARRAY_INPUT_RE.match(inner))
    return bool(ARRAY_INPUT_RE.match(stripped))


def _parse_array(array_literal: str) -> List[int]:
    cleaned = array_literal.strip()
    if cleaned.startswith("[") and cleaned.endswith("]"):
        cleaned = cleaned[1:-1].strip()
    if not cleaned:
        return []
    tokens = [token.strip() for token in cleaned.split(",")]
    result: List[int] = []
    for token in tokens:
        if token == "":
            continue
        result.append(int(token))
    return result


