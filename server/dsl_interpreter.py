from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import re

# ANTLR runtime imports
from antlr4 import InputStream, CommonTokenStream
from parser.grammar.AlgoDSLLexer import AlgoDSLLexer
from parser.grammar.AlgoDSLParser import AlgoDSLParser


@dataclass
class BubbleSortState:
    array: List[int]
    i: int = 0  # outer pass
    j: int = 0  # inner index
    swapped_in_pass: bool = False
    completed: bool = False

    def step(self) -> Dict[str, Any]:
        if self.completed:
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Bubble Sort",
                "step": -1,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(len(self.array))),
                },
                "explanation": "Sorting complete.",
            }

        n = len(self.array)
        if n <= 1:
            self.completed = True
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Bubble Sort",
                "step": 0,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(n)),
                },
                "explanation": "Array of length 0 or 1 is already sorted.",
            }

        # If inner loop finished, advance outer loop
        if self.j >= n - self.i - 1:
            # If no swaps, early finish
            if not self.swapped_in_pass:
                self.completed = True
                return {
                    "status": "success",
                    "type": "visualization_step",
                    "algorithm": "Bubble Sort",
                    "step": self.i,
                    "data": {
                        "array": self.array,
                        "highlighted_indices": [],
                        "sorted_indices": list(range(n)),
                    },
                    "explanation": "No swaps in the last pass; array is sorted.",
                }
            self.i += 1
            self.j = 0
            self.swapped_in_pass = False

            if self.i >= n - 1:
                self.completed = True
                return {
                    "status": "success",
                    "type": "visualization_step",
                    "algorithm": "Bubble Sort",
                    "step": self.i,
                    "data": {
                        "array": self.array,
                        "highlighted_indices": [],
                        "sorted_indices": list(range(n)),
                    },
                    "explanation": "Sorting complete.",
                }

        idx_a = self.j
        idx_b = self.j + 1
        a = self.array[idx_a]
        b = self.array[idx_b]

        explanation = (
            f"Comparing elements at index {idx_a} ({a}) and index {idx_b} ({b}). "
        )
        if a > b:
            self.array[idx_a], self.array[idx_b] = self.array[idx_b], self.array[idx_a]
            self.swapped_in_pass = True
            explanation += "Since the left is greater, they are swapped."
        else:
            explanation += "No swap needed."

        self.j += 1

        return {
            "status": "success",
            "type": "visualization_step",
            "algorithm": "Bubble Sort",
            "step": self.i + 1,
            "data": {
                "array": list(self.array),
                "highlighted_indices": [idx_a, idx_b],
                "sorted_indices": list(range(len(self.array) - self.i, len(self.array)))
                if self.i > 0
                else [],
            },
            "explanation": explanation,
        }


@dataclass
class SelectionSortState:
    array: List[int]
    i: int = 0  # outer loop index
    min_idx: int = 0  # index of minimum element
    j: int = 0  # inner loop index
    completed: bool = False

    def step(self) -> Dict[str, Any]:
        if self.completed:
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Selection Sort",
                "step": -1,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(len(self.array))),
                },
                "explanation": "Sorting complete.",
            }

        n = len(self.array)
        if n <= 1:
            self.completed = True
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Selection Sort",
                "step": 0,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(n)),
                },
                "explanation": "Array of length 0 or 1 is already sorted.",
            }

        if self.i >= n - 1:
            self.completed = True
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Selection Sort",
                "step": self.i,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(n)),
                },
                "explanation": "Sorting complete.",
            }

        # Initialize min_idx if starting new pass
        if self.j == self.i:
            self.min_idx = self.i

        # Find minimum element in unsorted portion
        if self.j < n:
            if self.array[self.j] < self.array[self.min_idx]:
                self.min_idx = self.j
                explanation = f"Found smaller element at index {self.j} ({self.array[self.j]}). Updating minimum index to {self.j}."
            else:
                explanation = f"Comparing index {self.j} ({self.array[self.j]}) with current minimum at index {self.min_idx} ({self.array[self.min_idx]}). No update needed."

            self.j += 1

            if self.j < n:
                return {
                    "status": "success",
                    "type": "visualization_step",
                    "algorithm": "Selection Sort",
                    "step": self.i + 1,
                    "data": {
                        "array": list(self.array),
                        "highlighted_indices": [self.i, self.j - 1, self.min_idx],
                        "sorted_indices": list(range(self.i)),
                    },
                    "explanation": explanation,
                }

        # Swap minimum with first unsorted element
        if self.min_idx != self.i:
            old_value = self.array[self.i]
            self.array[self.i], self.array[self.min_idx] = self.array[self.min_idx], self.array[self.i]
            explanation = f"Swapping minimum element at index {self.min_idx} (value {old_value}) with element at index {self.i}."
        else:
            explanation = f"Minimum element is already at index {self.i}. No swap needed."

        self.i += 1
        self.j = self.i

        return {
            "status": "success",
            "type": "visualization_step",
            "algorithm": "Selection Sort",
            "step": self.i,
            "data": {
                "array": list(self.array),
                "highlighted_indices": [self.i - 1],
                "sorted_indices": list(range(self.i)),
            },
            "explanation": explanation,
        }


@dataclass
class InsertionSortState:
    array: List[int]
    i: int = 1  # outer loop index (starting from 1)
    j: int = 0  # inner loop index
    key: Optional[int] = None  # current element being inserted
    completed: bool = False

    def step(self) -> Dict[str, Any]:
        if self.completed:
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Insertion Sort",
                "step": -1,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(len(self.array))),
                },
                "explanation": "Sorting complete.",
            }

        n = len(self.array)
        if n <= 1:
            self.completed = True
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Insertion Sort",
                "step": 0,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(n)),
                },
                "explanation": "Array of length 0 or 1 is already sorted.",
            }

        if self.i >= n:
            self.completed = True
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Insertion Sort",
                "step": self.i,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(n)),
                },
                "explanation": "Sorting complete.",
            }

        # Start new element insertion
        if self.key is None and self.i < n:
            self.key = self.array[self.i]
            self.j = self.i - 1
            if self.j < 0 or self.array[self.j] <= self.key:
                # Element is already in correct position
                explanation = f"Element at index {self.i} (value {self.key}) is already in correct position."
                self.i += 1
                self.key = None
                return {
                    "status": "success",
                    "type": "visualization_step",
                    "algorithm": "Insertion Sort",
                    "step": self.i,
                    "data": {
                        "array": list(self.array),
                        "highlighted_indices": [self.i - 1],
                        "sorted_indices": list(range(self.i)),
                    },
                    "explanation": explanation,
                }
            explanation = f"Inserting element at index {self.i} (value {self.key}) into sorted portion."

        # Shift elements to the right
        if self.j >= 0 and self.array[self.j] > self.key:
            self.array[self.j + 1] = self.array[self.j]
            explanation = f"Shifting element at index {self.j} ({self.array[self.j + 1]}) to the right."
            self.j -= 1

            if self.j >= 0 and self.array[self.j] > self.key:
                return {
                    "status": "success",
                    "type": "visualization_step",
                    "algorithm": "Insertion Sort",
                    "step": self.i + 1,
                    "data": {
                        "array": list(self.array),
                        "highlighted_indices": [self.i, self.j + 1],
                        "sorted_indices": list(range(self.i)),
                    },
                    "explanation": explanation,
                }

        # Insert key at correct position
        self.array[self.j + 1] = self.key
        explanation = f"Inserted element {self.key} at index {self.j + 1}."

        self.i += 1
        self.key = None
        self.j = 0

        return {
            "status": "success",
            "type": "visualization_step",
            "algorithm": "Insertion Sort",
            "step": self.i,
            "data": {
                "array": list(self.array),
                "highlighted_indices": [self.i - 1],
                "sorted_indices": list(range(self.i)),
            },
            "explanation": explanation,
        }


@dataclass
class QuickSortState:
    array: List[int]
    stack: List[Tuple[int, int]] = None  # Stack of (low, high) pairs
    low: int = 0
    high: int = 0
    pivot_idx: int = 0
    i: int = 0  # partition index
    j: int = 0  # current index in partition
    pivot: int = 0
    partitioning: bool = False
    completed: bool = False

    def __post_init__(self):
        if self.stack is None:
            self.stack = [(0, len(self.array) - 1)] if len(self.array) > 1 else []
            if self.stack:
                self.low, self.high = self.stack[0]

    def step(self) -> Dict[str, Any]:
        if self.completed:
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Quick Sort",
                "step": -1,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(len(self.array))),
                },
                "explanation": "Sorting complete.",
            }

        n = len(self.array)
        if n <= 1:
            self.completed = True
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Quick Sort",
                "step": 0,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(n)),
                },
                "explanation": "Array of length 0 or 1 is already sorted.",
            }

        if not self.stack:
            self.completed = True
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Quick Sort",
                "step": -1,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(n)),
                },
                "explanation": "Sorting complete.",
            }

        # Start partitioning
        if not self.partitioning:
            self.low, self.high = self.stack.pop(0)
            if self.low >= self.high:
                if self.stack:
                    return self.step()
                self.completed = True
                return {
                    "status": "success",
                    "type": "visualization_step",
                    "algorithm": "Quick Sort",
                    "step": -1,
                    "data": {
                        "array": self.array,
                        "highlighted_indices": [],
                        "sorted_indices": list(range(n)),
                    },
                    "explanation": "Sorting complete.",
                }

            self.pivot = self.array[self.high]
            self.pivot_idx = self.high
            self.i = self.low - 1
            self.j = self.low
            self.partitioning = True
            explanation = f"Starting partition: pivot = {self.pivot} at index {self.high}, partitioning from {self.low} to {self.high}."

        # Partitioning process
        if self.j < self.high:
            if self.array[self.j] <= self.pivot:
                self.i += 1
                self.array[self.i], self.array[self.j] = self.array[self.j], self.array[self.i]
                explanation = f"Element at index {self.j} ({self.array[self.i]}) <= pivot ({self.pivot}). Swapping with index {self.i}."
            else:
                explanation = f"Element at index {self.j} ({self.array[self.j]}) > pivot ({self.pivot}). No swap."

            self.j += 1

            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Quick Sort",
                "step": self.low + 1,
                "data": {
                    "array": list(self.array),
                    "highlighted_indices": [self.j - 1, self.i, self.pivot_idx],
                    "sorted_indices": [],
                },
                "explanation": explanation,
            }

        # Place pivot in correct position
        self.array[self.i + 1], self.array[self.high] = self.array[self.high], self.array[self.i + 1]
        pivot_pos = self.i + 1

        explanation = f"Partition complete. Pivot {self.pivot} placed at index {pivot_pos}."

        # Add sub-arrays to stack
        if self.low < pivot_pos - 1:
            self.stack.insert(0, (self.low, pivot_pos - 1))
        if pivot_pos + 1 < self.high:
            self.stack.insert(0, (pivot_pos + 1, self.high))

        self.partitioning = False

        return {
            "status": "success",
            "type": "visualization_step",
            "algorithm": "Quick Sort",
            "step": pivot_pos + 1,
            "data": {
                "array": list(self.array),
                "highlighted_indices": [pivot_pos],
                "sorted_indices": [pivot_pos],
            },
            "explanation": explanation,
        }


@dataclass
class MergeSortState:
    array: List[int]
    merge_queue: List[Tuple[int, int]] = None  # Queue of (low, high) pairs to merge
    current_merge: Optional[Tuple[int, int, int]] = None  # (low, mid, high)
    merge_i: int = 0
    merge_j: int = 0
    merge_k: int = 0
    left_arr: List[int] = None
    right_arr: List[int] = None
    completed: bool = False
    step_count: int = 0

    def __post_init__(self):
        if self.merge_queue is None:
            # Build merge queue (bottom-up approach for simplicity)
            n = len(self.array)
            size = 1
            self.merge_queue = []
            while size < n:
                for low in range(0, n, 2 * size):
                    mid = min(low + size - 1, n - 1)
                    high = min(low + 2 * size - 1, n - 1)
                    if mid < high:
                        self.merge_queue.append((low, mid, high))
                size *= 2

    def step(self) -> Dict[str, Any]:
        if self.completed:
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Merge Sort",
                "step": -1,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(len(self.array))),
                },
                "explanation": "Sorting complete.",
            }

        n = len(self.array)
        if n <= 1:
            self.completed = True
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Merge Sort",
                "step": 0,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(n)),
                },
                "explanation": "Array of length 0 or 1 is already sorted.",
            }

        if not self.merge_queue and self.current_merge is None:
            self.completed = True
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Merge Sort",
                "step": self.step_count,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(n)),
                },
                "explanation": "Sorting complete.",
            }

        # Start new merge
        if self.current_merge is None:
            if not self.merge_queue:
                self.completed = True
                return {
                    "status": "success",
                    "type": "visualization_step",
                    "algorithm": "Merge Sort",
                    "step": self.step_count,
                    "data": {
                        "array": self.array,
                        "highlighted_indices": [],
                        "sorted_indices": list(range(n)),
                    },
                    "explanation": "Sorting complete.",
                }

            low, mid, high = self.merge_queue.pop(0)
            self.current_merge = (low, mid, high)
            self.left_arr = self.array[low:mid + 1].copy()
            self.right_arr = self.array[mid + 1:high + 1].copy()
            self.merge_i = 0
            self.merge_j = 0
            self.merge_k = low
            self.step_count += 1
            explanation = f"Merging sub-arrays from index {low} to {mid} and {mid + 1} to {high}."

            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Merge Sort",
                "step": self.step_count,
                "data": {
                    "array": list(self.array),
                    "highlighted_indices": list(range(low, high + 1)),
                    "sorted_indices": [],
                },
                "explanation": explanation,
            }

        # Continue merging
        low, mid, high = self.current_merge

        if self.merge_i < len(self.left_arr) and self.merge_j < len(self.right_arr):
            if self.left_arr[self.merge_i] <= self.right_arr[self.merge_j]:
                self.array[self.merge_k] = self.left_arr[self.merge_i]
                explanation = f"Taking {self.left_arr[self.merge_i]} from left sub-array (index {low + self.merge_i})."
                self.merge_i += 1
            else:
                self.array[self.merge_k] = self.right_arr[self.merge_j]
                explanation = f"Taking {self.right_arr[self.merge_j]} from right sub-array (index {mid + 1 + self.merge_j})."
                self.merge_j += 1
            self.merge_k += 1
            self.step_count += 1

            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Merge Sort",
                "step": self.step_count,
                "data": {
                    "array": list(self.array),
                    "highlighted_indices": [self.merge_k - 1, low + self.merge_i - 1 if self.merge_i > 0 else low, mid + 1 + self.merge_j - 1 if self.merge_j > 0 else mid + 1],
                    "sorted_indices": list(range(low, self.merge_k)),
                },
                "explanation": explanation,
            }

        # Copy remaining elements from left
        if self.merge_i < len(self.left_arr):
            self.array[self.merge_k] = self.left_arr[self.merge_i]
            explanation = f"Copying remaining element {self.left_arr[self.merge_i]} from left sub-array."
            self.merge_i += 1
            self.merge_k += 1
            self.step_count += 1

            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Merge Sort",
                "step": self.step_count,
                "data": {
                    "array": list(self.array),
                    "highlighted_indices": [self.merge_k - 1],
                    "sorted_indices": list(range(low, self.merge_k)),
                },
                "explanation": explanation,
            }

        # Copy remaining elements from right
        if self.merge_j < len(self.right_arr):
            self.array[self.merge_k] = self.right_arr[self.merge_j]
            explanation = f"Copying remaining element {self.right_arr[self.merge_j]} from right sub-array."
            self.merge_j += 1
            self.merge_k += 1
            self.step_count += 1

            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Merge Sort",
                "step": self.step_count,
                "data": {
                    "array": list(self.array),
                    "highlighted_indices": [self.merge_k - 1],
                    "sorted_indices": list(range(low, self.merge_k)),
                },
                "explanation": explanation,
            }

        # Merge complete
        explanation = f"Merge complete for range {low} to {high}."
        self.current_merge = None
        self.step_count += 1

        return {
            "status": "success",
            "type": "visualization_step",
            "algorithm": "Merge Sort",
            "step": self.step_count,
            "data": {
                "array": list(self.array),
                "highlighted_indices": list(range(low, high + 1)),
                "sorted_indices": list(range(low, high + 1)),
            },
            "explanation": explanation,
        }


@dataclass
class HeapSortState:
    array: List[int]
    heap_size: int = 0
    building_heap: bool = True
    i: int = 0  # current index for heap building/extraction
    extracting: bool = False
    completed: bool = False

    def __post_init__(self):
        self.heap_size = len(self.array)
        self.i = (self.heap_size // 2) - 1  # Start from last non-leaf node

    def _heapify(self, arr: List[int], n: int, i: int) -> None:
        """Helper to maintain heap property."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)

    def step(self) -> Dict[str, Any]:
        if self.completed:
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Heap Sort",
                "step": -1,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(len(self.array))),
                },
                "explanation": "Sorting complete.",
            }

        n = len(self.array)
        if n <= 1:
            self.completed = True
            return {
                "status": "success",
                "type": "visualization_step",
                "algorithm": "Heap Sort",
                "step": 0,
                "data": {
                    "array": self.array,
                    "highlighted_indices": [],
                    "sorted_indices": list(range(n)),
                },
                "explanation": "Array of length 0 or 1 is already sorted.",
            }

        # Build max heap
        if self.building_heap:
            if self.i >= 0:
                left = 2 * self.i + 1
                right = 2 * self.i + 2
                largest = self.i

                if left < self.heap_size and self.array[left] > self.array[largest]:
                    largest = left
                if right < self.heap_size and self.array[right] > self.array[largest]:
                    largest = right

                if largest != self.i:
                    self.array[self.i], self.array[largest] = self.array[largest], self.array[self.i]
                    explanation = f"Heapifying node at index {self.i}. Swapping with child at index {largest}."
                    self._heapify(self.array, self.heap_size, largest)
                else:
                    explanation = f"Node at index {self.i} already satisfies heap property."

                self.i -= 1

                if self.i >= 0:
                    return {
                        "status": "success",
                        "type": "visualization_step",
                        "algorithm": "Heap Sort",
                        "step": self.i + 2,
                        "data": {
                            "array": list(self.array),
                            "highlighted_indices": [self.i + 1, 2 * (self.i + 1) + 1, 2 * (self.i + 1) + 2],
                            "sorted_indices": [],
                        },
                        "explanation": explanation,
                    }

            # Heap built, start extraction
            self.building_heap = False
            self.extracting = True
            self.i = self.heap_size - 1
            explanation = "Max heap built. Starting to extract elements."

        # Extract elements from heap
        if self.extracting and self.i > 0:
            # Swap root with last element
            self.array[0], self.array[self.i] = self.array[self.i], self.array[0]
            explanation = f"Swapping root (max element) with element at index {self.i}. Element at index {self.i} is now in sorted position."

            self.heap_size -= 1
            self._heapify(self.array, self.heap_size, 0)

            self.i -= 1

            if self.i > 0:
                return {
                    "status": "success",
                    "type": "visualization_step",
                    "algorithm": "Heap Sort",
                    "step": len(self.array) - self.i,
                    "data": {
                        "array": list(self.array),
                        "highlighted_indices": [0, self.i + 1],
                        "sorted_indices": list(range(self.i + 1, len(self.array))),
                    },
                    "explanation": explanation,
                }

        self.completed = True
        return {
            "status": "success",
            "type": "visualization_step",
            "algorithm": "Heap Sort",
            "step": len(self.array),
            "data": {
                "array": list(self.array),
                "highlighted_indices": [],
                "sorted_indices": list(range(len(self.array))),
            },
            "explanation": "Sorting complete.",
        }


class AlgorithmSession:
    def __init__(self) -> None:
        self.algorithm: Optional[str] = None
        self.state: Optional[Any] = None  # Can be any sorting algorithm state
        self.menu_state: Optional[str] = None  # 'sorting', 'pathfinding', 'structures'
        self.waiting_for_array: bool = False  # True when waiting for array input
        self.selected_algorithm: Optional[str] = None  # Store selected algorithm name

    def reset(self) -> None:
        self.algorithm = None
        self.state = None
        self.menu_state = None
        self.waiting_for_array = False
        self.selected_algorithm = None


class AlgorithmSessionManager:
    VISUALIZE_RE = re.compile(
        r"^\s*visualize\s+(?P<algo>[a-zA-Z ]+)\s+on\s*\[(?P<array>[^\]]*)\]\s*$",
        re.IGNORECASE,
    )

    EXPLAIN_RE = re.compile(r"^\s*explain\s*$", re.IGNORECASE)
    NEXT_RE = re.compile(r"^\s*next\s*$", re.IGNORECASE)
    RESET_RE = re.compile(r"^\s*reset\s*$", re.IGNORECASE)

    # Available sorting algorithms
    SORTING_ALGORITHMS = [
        ("1", "Bubble Sort", "bubble"),
        ("2", "Merge Sort", "merge"),
        ("3", "Selection Sort", "selection"),
        ("4", "Insertion Sort", "insertion"),
        ("5", "Quick Sort", "quick"),
        ("6", "Heap Sort", "heap")
    ]

    def __init__(self) -> None:
        self.sessions: Dict[str, AlgorithmSession] = {}

    def _get_or_create(self, session_id: str) -> AlgorithmSession:
        if session_id not in self.sessions:
            self.sessions[session_id] = AlgorithmSession()
        return self.sessions[session_id]

    def handle_command(self, session_id: str, command: str) -> Dict[str, Any]:
        session = self._get_or_create(session_id)

        # Handle array input if waiting for array
        if session.waiting_for_array:
            return self._handle_array_input(session, command)

        # Handle sorting algorithm selection if in sorting menu
        if session.menu_state == "sort":
            algo_selection = self._try_parse_sorting_algorithm(command)
            if algo_selection is not None:
                return self._handle_sorting_algorithm_selection(session, algo_selection)
            else:
                # If in sorting menu but no valid selection, show menu again
                return self._get_sorting_menu()

        # First try ANTLR to detect top-level menu selections
        menu = self._try_parse_menu(command)
        if menu is not None:
            # Set menu state and return appropriate sub-menu
            session.menu_state = menu
            if menu == "sort":
                return self._get_sorting_menu()
            elif menu == "path":
                session.menu_state = None  # Reset for now
                return {
                    "status": "success",
                    "type": "info",
                    "message": "Got pathfinding command",
                }
            elif menu == "struct":
                session.menu_state = None  # Reset for now
                return {
                    "status": "success",
                    "type": "info", 
                    "message": "Got structure command",
                }

        # visualize command
        m = self.VISUALIZE_RE.match(command)
        if m:
            algo = m.group("algo").strip().lower()
            array_str = m.group("array").strip()
            try:
                arr = self._parse_array(array_str)
            except ValueError:
                raise ValueError(
                    "Unknown command or invalid syntax. Try something like: 'visualize bubble sort on [1, 2, 3]'"
                )

            if algo in ("bubble sort", "bubblesort"):
                session.algorithm = "Bubble Sort"
                session.state = BubbleSortState(array=arr)
                # Return first step immediately
                return session.state.step()
            else:
                raise ValueError(
                    "Unknown algorithm. Supported: Bubble Sort."
                )

        # next command
        if self.NEXT_RE.match(command):
            if not session.state:
                raise ValueError(
                    "No active algorithm. Start with: 'visualize bubble sort on [5, 2, 8, 1, 9]'"
                )
            return session.state.step()

        # explain command
        if self.EXPLAIN_RE.match(command):
            if session.algorithm == "Bubble Sort":
                return {
                    "status": "success",
                    "type": "explanation",
                    "algorithm": "Bubble Sort",
                    "explanation": (
                        "Bubble Sort has worst and average time complexity O(n^2), "
                        "best case O(n) when the array is already sorted."
                    ),
                }
            raise ValueError("No active algorithm to explain.")

        # reset command
        if self.RESET_RE.match(command):
            session.reset()
            return {
                "status": "success",
                "type": "info",
                "message": "Session reset.",
            }

        raise ValueError(
            "Unknown command or invalid syntax. Try something like: 'visualize bubble sort on [1, 2, 3]'"
        )

    @staticmethod
    def _parse_array(array_literal: str) -> List[int]:
        # Accept commas and spaces, ignore empty tokens
        tokens = [t.strip() for t in array_literal.split(",")]
        result: List[int] = []
        for tok in tokens:
            if tok == "":
                continue
            result.append(int(tok))
        return result

    @staticmethod
    def _try_parse_menu(command: str) -> Optional[str]:
        """Return one of 'sort' | 'path' | 'struct' if the input contains menu keywords; otherwise None."""
        cmd_lower = command.strip().lower()
        
        # Check for sorting keywords
        sort_keywords = ['sort', 'sorting', '1']
        if any(keyword in cmd_lower for keyword in sort_keywords):
            return "sort"
            
        # Check for pathfinding keywords  
        path_keywords = ['path', 'pathfinding', '2']
        if any(keyword in cmd_lower for keyword in path_keywords):
            return "path"
            
        # Check for data structure keywords
        struct_keywords = ['data', 'structure', 'structures', '3']
        if any(keyword in cmd_lower for keyword in struct_keywords):
            return "struct"
            
        return None

    def _get_sorting_menu(self) -> Dict[str, Any]:
        """Return the sorting algorithms menu."""
        menu_text = "Currently we have these algorithms for sorting, please select an algorithm that you want to explore:\n\n"
        for num, name, keyword in self.SORTING_ALGORITHMS:
            menu_text += f"{num}. {name}\n"
        menu_text += "\nYou can type a number (1-6) or part of the algorithm name (e.g., 'bubble', 'quick')."
        
        return {
            "status": "success",
            "type": "menu",
            "message": menu_text,
        }

    def _try_parse_sorting_algorithm(self, command: str) -> Optional[str]:
        """Parse sorting algorithm selection from command."""
        cmd_lower = command.strip().lower()
        
        # Check for number selection (1-6)
        if cmd_lower in ["1", "2", "3", "4", "5", "6"]:
            return cmd_lower
            
        # Check for keyword matches
        for num, name, keyword in self.SORTING_ALGORITHMS:
            if keyword in cmd_lower or name.lower() in cmd_lower:
                return num
                
        return None

    def _handle_sorting_algorithm_selection(self, session: AlgorithmSession, selection: str) -> Dict[str, Any]:
        """Handle sorting algorithm selection and return appropriate response."""
        # Find the algorithm by number
        algo_info = None
        for num, name, keyword in self.SORTING_ALGORITHMS:
            if num == selection:
                algo_info = (num, name, keyword)
                break
                
        if algo_info is None:
            return {
                "status": "error",
                "message": "Invalid algorithm selection. Please choose 1-6 or type part of the algorithm name."
            }
            
        num, name, keyword = algo_info
        
        # Store selected algorithm and prompt for array input
        session.selected_algorithm = name
        session.waiting_for_array = True
        session.menu_state = None  # Exit menu state
        
        return {
            "status": "success",
            "type": "prompt",
            "message": f"Great! You selected {name}. Now please enter an array of numbers to sort. Separate each number with a comma (e.g., 5,2,8,1,9):"
        }

    def _handle_array_input(self, session: AlgorithmSession, command: str) -> Dict[str, Any]:
        """Handle array input and start algorithm visualization."""
        try:
            # Parse the array from user input
            array = self._parse_array(command.strip())
            
            # Reset waiting state
            session.waiting_for_array = False
            
            # Start the appropriate algorithm
            algorithm = session.selected_algorithm
            
            if algorithm == "Bubble Sort":
                session.algorithm = "Bubble Sort"
                session.state = BubbleSortState(array=array)
            elif algorithm == "Selection Sort":
                session.algorithm = "Selection Sort"
                session.state = SelectionSortState(array=array)
            elif algorithm == "Insertion Sort":
                session.algorithm = "Insertion Sort"
                session.state = InsertionSortState(array=array)
            elif algorithm == "Quick Sort":
                session.algorithm = "Quick Sort"
                session.state = QuickSortState(array=array)
            elif algorithm == "Merge Sort":
                session.algorithm = "Merge Sort"
                session.state = MergeSortState(array=array)
            elif algorithm == "Heap Sort":
                session.algorithm = "Heap Sort"
                session.state = HeapSortState(array=array)
            else:
                return {
                    "status": "error",
                    "message": f"Unknown algorithm: {algorithm}"
                }
            
            # Return first step immediately
            return session.state.step()
                
        except ValueError as e:
            return {
                "status": "error",
                "message": "Invalid array format. Please enter numbers separated by commas (e.g., 5,2,8,1,9)."
            }


