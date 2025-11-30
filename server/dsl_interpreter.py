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
    "path",
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


ALGORITHM_BUILDERS: Dict[str, Callable[[List[int]], List[Dict[str, Any]]]] = {
    "Bubble Sort": generate_bubble_sort_steps,
    "Selection Sort": generate_selection_sort_steps,
    "Insertion Sort": generate_insertion_sort_steps,
    "Merge Sort": generate_merge_sort_steps,
    "Quick Sort": generate_quick_sort_steps,
    "Heap Sort": generate_heap_sort_steps,
}

ALGORITHM_ALIASES: Dict[str, str] = dict(SORTING_SELECTION_KEYWORDS)

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
        session = self._get_or_create(session_id)
        stripped = command.strip()
        lowered = stripped.lower()

        if not stripped:
            raise ValueError(
                "Unknown command or invalid syntax. Type 'menu' to see available options."
            )

        if lowered == "menu":
            session.reset()
            session.stage = "menu"
            return self._menu_payload()

        # If in sorting_menu stage, prioritize algorithm selection over menu selection
        if session.stage == "sorting_menu":
            selection_algorithm = self._match_sorting_selection(lowered)
            if not selection_algorithm:
                # Try to find algorithm keywords within the input
                for keyword, algo_name in SORTING_SELECTION_KEYWORDS.items():
                    if keyword in lowered:
                        selection_algorithm = algo_name
                        break
            
            if selection_algorithm:
                session.pending_algorithm = selection_algorithm
                session.stage = "await_array"
                return self._prompt_array_payload(selection_algorithm)

        # Check for menu selection keywords within the input (not just exact match)
        # First check for numbers (only if not in sorting_menu)
        if lowered in MENU_SELECTION_NUMBERS["sorting"]:
            session.stage = "sorting_menu"
            session.pending_algorithm = None
            return self._sorting_menu_payload()
        
        if lowered in MENU_SELECTION_NUMBERS["pathfinding"]:
            session.stage = "menu"
            return self._coming_soon_payload("Pathfinding")
        
        if lowered in MENU_SELECTION_NUMBERS["data_structures"]:
            session.stage = "menu"
            return self._coming_soon_payload("Data Structures")

        # Check if any sorting keyword appears in the input
        if any(keyword in lowered for keyword in MENU_SORTING_KEYWORDS):
            session.stage = "sorting_menu"
            session.pending_algorithm = None
            return self._sorting_menu_payload()

        # Check if any pathfinding keyword appears in the input
        if any(keyword in lowered for keyword in MENU_PATHFINDING_KEYWORDS):
            session.stage = "menu"
            return self._coming_soon_payload("Pathfinding")

        # Check if any data structure keyword appears in the input
        if any(keyword in lowered for keyword in MENU_DATA_STRUCTURE_KEYWORDS):
            session.stage = "menu"
            return self._coming_soon_payload("Data Structures")

        # Check for algorithm selection - try exact match first, then search within input
        selection_algorithm = self._match_sorting_selection(lowered)
        if not selection_algorithm:
            # Try to find algorithm keywords within the input
            for keyword, algo_name in SORTING_SELECTION_KEYWORDS.items():
                if keyword in lowered:
                    selection_algorithm = algo_name
                    break
        
        if selection_algorithm:
            session.pending_algorithm = selection_algorithm
            session.stage = "await_array"
            return self._prompt_array_payload(selection_algorithm)

        if session.stage == "await_array" and self._is_array_literal(stripped):
            if not session.pending_algorithm:
                raise ValueError(
                    "Select a sorting algorithm before entering the array."
                )
            array_values = self._parse_array(stripped)
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
                array_values = self._parse_array(array_literal)
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
                for keyword, algo_name in SORTING_SELECTION_KEYWORDS.items():
                    if keyword in lowered:
                        algorithm_to_explain = algo_name
                        break
            
            if not algorithm_to_explain:
                raise ValueError(
                    "No algorithm specified. Either select an algorithm first, or include the algorithm name in your request (e.g., 'explain bubble sort')."
                )
            
            explanation = ALGORITHM_EXPLANATIONS.get(
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

    @staticmethod
    def _match_sorting_selection(token: str) -> Optional[str]:
        if token in SORTING_NUMBER_TO_ALGORITHM:
            return SORTING_NUMBER_TO_ALGORITHM[token]
        return SORTING_SELECTION_KEYWORDS.get(token)

    @staticmethod
    def _menu_payload() -> Dict[str, Any]:
        return {
            "status": "success",
            "type": "menu",
            "message": MAIN_MENU_MESSAGE,
            "options": [
                {"id": "1", "label": "Sorting Algorithms"},
                {"id": "2", "label": "Pathfinding Algorithms (coming soon)"},
                {"id": "3", "label": "Data Structures (coming soon)"},
            ],
        }

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def _coming_soon_payload(topic: str) -> Dict[str, Any]:
        return {
            "status": "success",
            "type": "info",
            "message": f"{topic} visualizations are coming soon. Type 'menu' to go back.",
        }

    @staticmethod
    def _is_array_literal(text: str) -> bool:
        stripped = text.strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            inner = stripped[1:-1].strip()
            return True if not inner else bool(ARRAY_INPUT_RE.match(inner))
        return bool(ARRAY_INPUT_RE.match(stripped))

    @staticmethod
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


