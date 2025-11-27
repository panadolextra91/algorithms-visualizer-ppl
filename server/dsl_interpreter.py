from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import re

# ANTLR runtime imports
from antlr4 import InputStream, CommonTokenStream
from parser.grammar.AlgoDSLLexer import AlgoDSLLexer
from parser.grammar.AlgoDSLParser import AlgoDSLParser


@dataclass
class BubbleSortState:
    array: List[int]
    original_array: List[int] = field(default_factory=list)
    i: int = 0  # outer pass
    j: int = 0  # inner index
    swapped_in_pass: bool = False
    completed: bool = False
    history: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.original_array:
            self.original_array = list(self.array)

    def _record_action(self, summary: str) -> None:
        """Store a human-readable description of the latest action."""
        snapshot = f"Array: {self.array}"
        self.history.append(f"{summary} | {snapshot}")

    def step(self) -> Dict[str, Any]:
        if self.completed:
            explanation_text = "Sorting complete."
            self._record_action(explanation_text)
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
                "explanation": explanation_text,
            }

        n = len(self.array)
        if n <= 1:
            self.completed = True
            explanation_text = "Array of length 0 or 1 is already sorted."
            self._record_action(explanation_text)
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
                "explanation": explanation_text,
            }

        # If inner loop finished, advance outer loop
        if self.j >= n - self.i - 1:
            # If no swaps, early finish
            if not self.swapped_in_pass:
                self.completed = True
                explanation_text = "No swaps in the last pass; array is sorted."
                self._record_action(explanation_text)
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
                    "explanation": explanation_text,
                }
            self.i += 1
            self.j = 0
            self.swapped_in_pass = False

            if self.i >= n - 1:
                self.completed = True
                explanation_text = "Sorting complete."
                self._record_action(explanation_text)
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
                    "explanation": explanation_text,
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

        self._record_action(explanation)
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
    def _parse_with_antlr(self, command: str) -> Optional[Dict[str, Any]]:
        """Parse command using ANTLR grammar. Returns command type and extracted data."""
        try:
            input_stream = InputStream(command)
            lexer = AlgoDSLLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = AlgoDSLParser(token_stream)
            
            # Parse the command
            tree = parser.command()
            
            # Check for parse errors
            if parser.getNumberOfSyntaxErrors() > 0:
                return None
            
            if tree.getChildCount() == 0:
                return None
            
            child = tree.getChild(0)
            
            # Menu command
            if isinstance(child, AlgoDSLParser.MenuCommandContext):
                return {"type": "menu"}
            
            # Next command
            if isinstance(child, AlgoDSLParser.NextCommandContext):
                return {"type": "next"}
            
            # Explain command
            if isinstance(child, AlgoDSLParser.ExplainCommandContext):
                return {"type": "explain"}
            
            # Reset command
            if isinstance(child, AlgoDSLParser.ResetCommandContext):
                return {"type": "reset"}
            
            # Menu selection - check for specific alternatives
            if isinstance(child, AlgoDSLParser.MenuSelectionContext):
                # Check specific alternative types (these inherit from MenuSelectionContext)
                if isinstance(child, AlgoDSLParser.MenuSortingContext):
                    return {"type": "menu_selection", "menu": "sort"}
                elif isinstance(child, AlgoDSLParser.MenuPathfindingContext):
                    return {"type": "menu_selection", "menu": "path"}
                elif isinstance(child, AlgoDSLParser.MenuDataStructuresContext):
                    return {"type": "menu_selection", "menu": "struct"}
                else:
                    # Fallback: check token type
                    first_token = child.getStart()
                    if first_token.type == AlgoDSLParser.SORTING_KEYWORDS or first_token.type == AlgoDSLParser.NUMBER_ONE:
                        return {"type": "menu_selection", "menu": "sort"}
                    elif first_token.type == AlgoDSLParser.PATHFINDING_KEYWORDS or first_token.type == AlgoDSLParser.NUMBER_TWO:
                        return {"type": "menu_selection", "menu": "path"}
                    elif first_token.type == AlgoDSLParser.DATA_STRUCTURE_KEYWORDS or first_token.type == AlgoDSLParser.NUMBER_THREE:
                        return {"type": "menu_selection", "menu": "struct"}
            
            # Sorting algorithm selection
            if isinstance(child, AlgoDSLParser.SortingAlgorithmSelectionContext):
                first_token = child.getStart()
                token_type = first_token.type
                # Map token types to algorithm numbers
                algo_map = {
                    AlgoDSLParser.NUMBER_ONE: "1",
                    AlgoDSLParser.NUMBER_TWO: "2",
                    AlgoDSLParser.NUMBER_THREE: "3",
                    AlgoDSLParser.NUMBER_FOUR: "4",
                    AlgoDSLParser.NUMBER_FIVE: "5",
                    AlgoDSLParser.NUMBER_SIX: "6",
                    AlgoDSLParser.BUBBLE_KEYWORDS: "1",
                    AlgoDSLParser.MERGE_KEYWORDS: "2",
                    AlgoDSLParser.SELECTION_KEYWORDS: "3",
                    AlgoDSLParser.INSERTION_KEYWORDS: "4",
                    AlgoDSLParser.QUICK_KEYWORDS: "5",
                    AlgoDSLParser.HEAP_KEYWORDS: "6",
                }
                if token_type in algo_map:
                    return {"type": "sorting_algorithm", "selection": algo_map[token_type]}
            
            # Array input
            if isinstance(child, AlgoDSLParser.ArrayInputContext):
                numbers = []
                for i in range(child.getChildCount()):
                    node = child.getChild(i)
                    if hasattr(node, 'getText'):
                        text = node.getText()
                        try:
                            numbers.append(int(text))
                        except ValueError:
                            pass
                return {"type": "array_input", "array": numbers}
            
            # Visualize command (legacy)
            if isinstance(child, AlgoDSLParser.VisualizeCommandContext):
                array_literal = child.arrayLiteral()
                if array_literal:
                    array_input_ctx = array_literal.arrayInput()
                    if array_input_ctx:
                        numbers = []
                        for i in range(array_input_ctx.getChildCount()):
                            node = array_input_ctx.getChild(i)
                            if hasattr(node, 'getText'):
                                text = node.getText()
                                try:
                                    numbers.append(int(text))
                                except ValueError:
                                    pass
                        return {"type": "visualize", "algorithm": "bubble sort", "array": numbers}
            
            return None
        except Exception as e:
            # If ANTLR parsing fails, return None
            return None

    # Available sorting algorithms
    SORTING_ALGORITHMS = [
        ("1", "Bubble Sort", "bubble"),
        ("2", "Merge Sort", "merge"),
        ("3", "Selection Sort", "selection"),
        ("4", "Insertion Sort", "insertion"),
        ("5", "Quick Sort", "quick"),
        ("6", "Heap Sort", "heap")
    ]

    @staticmethod
    def _get_algorithm_principle(algorithm_name: str) -> str:
        """Return the principle/overview explanation for an algorithm."""
        principles = {
            "Bubble Sort": (
                "Bubble Sort is a simple comparison-based sorting algorithm. "
                "It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. "
                "The pass through the list is repeated until no swaps are needed, which means the list is sorted. "
                "The algorithm gets its name because smaller elements 'bubble' to the top of the list. "
                "Time Complexity: O(n²) worst/average case, O(n) best case (when already sorted). "
                "Space Complexity: O(1) - in-place sorting."
            ),
            "Selection Sort": (
                "Selection Sort divides the input list into two parts: a sorted sublist and an unsorted sublist. "
                "The algorithm repeatedly finds the minimum element from the unsorted part and places it at the beginning of the sorted part. "
                "This process continues until the entire list is sorted. "
                "Time Complexity: O(n²) for all cases. "
                "Space Complexity: O(1) - in-place sorting."
            ),
            "Insertion Sort": (
                "Insertion Sort builds the sorted array one element at a time. "
                "It takes each element from the input and inserts it into the correct position in the already sorted portion. "
                "The algorithm is similar to how you might sort playing cards in your hands. "
                "Time Complexity: O(n²) worst/average case, O(n) best case (when already sorted). "
                "Space Complexity: O(1) - in-place sorting."
            ),
            "Quick Sort": (
                "Quick Sort is a divide-and-conquer algorithm. "
                "It picks a 'pivot' element and partitions the array around the pivot, placing smaller elements before it and larger elements after it. "
                "The algorithm then recursively sorts the sub-arrays on either side of the pivot. "
                "Time Complexity: O(n log n) average case, O(n²) worst case (when pivot is always smallest/largest). "
                "Space Complexity: O(log n) average case due to recursion stack."
            ),
            "Merge Sort": (
                "Merge Sort is a divide-and-conquer algorithm that divides the array into two halves, sorts them separately, and then merges them back together. "
                "The algorithm recursively splits the array until each sub-array contains a single element (which is already sorted), then merges them in sorted order. "
                "Time Complexity: O(n log n) for all cases - consistent performance. "
                "Space Complexity: O(n) - requires additional space for merging."
            ),
            "Heap Sort": (
                "Heap Sort uses a binary heap data structure to sort elements. "
                "First, it builds a max-heap from the input array, where the largest element is at the root. "
                "Then it repeatedly extracts the maximum element from the heap and places it at the end of the sorted portion, rebuilding the heap after each extraction. "
                "Time Complexity: O(n log n) for all cases. "
                "Space Complexity: O(1) - in-place sorting (if we ignore the recursion stack)."
            ),
        }
        return principles.get(algorithm_name, "Algorithm principle not available.")

    def __init__(self) -> None:
        self.sessions: Dict[str, AlgorithmSession] = {}

    def _get_or_create(self, session_id: str) -> AlgorithmSession:
        if session_id not in self.sessions:
            self.sessions[session_id] = AlgorithmSession()
        return self.sessions[session_id]

    def handle_command(self, session_id: str, command: str) -> Dict[str, Any]:
        session = self._get_or_create(session_id)

        # Handle array input if waiting for array (check this first, before ANTLR)
        if session.waiting_for_array:
            # Try to parse as array with ANTLR first
            parsed = self._parse_with_antlr(command)
            if parsed and parsed.get("type") == "array_input":
                arr = parsed.get("array", [])
                if arr:
                    session.waiting_for_array = False
                    algorithm = session.selected_algorithm
                    
                    if algorithm == "Bubble Sort":
                        session.algorithm = "Bubble Sort"
                        session.state = BubbleSortState(array=arr)
                    elif algorithm == "Selection Sort":
                        session.algorithm = "Selection Sort"
                        session.state = SelectionSortState(array=arr)
                    elif algorithm == "Insertion Sort":
                        session.algorithm = "Insertion Sort"
                        session.state = InsertionSortState(array=arr)
                    elif algorithm == "Quick Sort":
                        session.algorithm = "Quick Sort"
                        session.state = QuickSortState(array=arr)
                    elif algorithm == "Merge Sort":
                        session.algorithm = "Merge Sort"
                        session.state = MergeSortState(array=arr)
                    elif algorithm == "Heap Sort":
                        session.algorithm = "Heap Sort"
                        session.state = HeapSortState(array=arr)
                    else:
                        return {
                            "status": "error",
                            "message": f"Unknown algorithm: {algorithm}"
                        }
                    
                    return session.state.step()
            
            # Fallback: try to parse as array string
            try:
                arr = self._parse_array(command)
                session.waiting_for_array = False
                algorithm = session.selected_algorithm
                
                if algorithm == "Bubble Sort":
                    session.algorithm = "Bubble Sort"
                    session.state = BubbleSortState(array=arr)
                elif algorithm == "Selection Sort":
                    session.algorithm = "Selection Sort"
                    session.state = SelectionSortState(array=arr)
                elif algorithm == "Insertion Sort":
                    session.algorithm = "Insertion Sort"
                    session.state = InsertionSortState(array=arr)
                elif algorithm == "Quick Sort":
                    session.algorithm = "Quick Sort"
                    session.state = QuickSortState(array=arr)
                elif algorithm == "Merge Sort":
                    session.algorithm = "Merge Sort"
                    session.state = MergeSortState(array=arr)
                elif algorithm == "Heap Sort":
                    session.algorithm = "Heap Sort"
                    session.state = HeapSortState(array=arr)
                else:
                    return {
                        "status": "error",
                        "message": f"Unknown algorithm: {algorithm}"
                    }
                
                return session.state.step()
            except ValueError:
                return {
                    "status": "error",
                    "message": "Invalid array format. Please enter numbers separated by commas (e.g., 5,2,8,1,9)."
                }

        # Handle sorting algorithm selection if in sorting menu (check before ANTLR)
        if session.menu_state == "sort":
            # Try to parse as sorting algorithm selection
            parsed = self._parse_with_antlr(command)
            if parsed and parsed.get("type") == "sorting_algorithm":
                return self._handle_sorting_algorithm_selection(session, parsed["selection"])
            else:
                # Also check if it's a number that could be an algorithm
                cmd_lower = command.strip().lower()
                if cmd_lower in ["1", "2", "3", "4", "5", "6"]:
                    return self._handle_sorting_algorithm_selection(session, cmd_lower)
                # Check for keyword matches
                for num, name, keyword in self.SORTING_ALGORITHMS:
                    if keyword in cmd_lower or name.lower() in cmd_lower:
                        return self._handle_sorting_algorithm_selection(session, num)
                # Invalid selection, show menu again
                return self._get_sorting_menu()

        # Try to parse with ANTLR for other commands
        parsed = self._parse_with_antlr(command)
        
        if parsed:
            cmd_type = parsed.get("type")
            if session.waiting_for_array:
                if cmd_type == "array_input":
                    # Use the parsed array from ANTLR
                    arr = parsed.get("array", [])
                    if arr:
                        session.waiting_for_array = False
                        algorithm = session.selected_algorithm
                        
                        if algorithm == "Bubble Sort":
                            session.algorithm = "Bubble Sort"
                            session.state = BubbleSortState(array=arr)
                        elif algorithm == "Selection Sort":
                            session.algorithm = "Selection Sort"
                            session.state = SelectionSortState(array=arr)
                        elif algorithm == "Insertion Sort":
                            session.algorithm = "Insertion Sort"
                            session.state = InsertionSortState(array=arr)
                        elif algorithm == "Quick Sort":
                            session.algorithm = "Quick Sort"
                            session.state = QuickSortState(array=arr)
                        elif algorithm == "Merge Sort":
                            session.algorithm = "Merge Sort"
                            session.state = MergeSortState(array=arr)
                        elif algorithm == "Heap Sort":
                            session.algorithm = "Heap Sort"
                            session.state = HeapSortState(array=arr)
                        else:
                            return {
                                "status": "error",
                                "message": f"Unknown algorithm: {algorithm}"
                            }
                        
                        return session.state.step()
                    else:
                        return {
                            "status": "error",
                            "message": "Invalid array format. Please enter numbers separated by commas (e.g., 5,2,8,1,9)."
                        }
                else:
                    # Try to parse as array even if ANTLR didn't recognize it
                    try:
                        arr = self._parse_array(command)
                        session.waiting_for_array = False
                        algorithm = session.selected_algorithm
                        
                        if algorithm == "Bubble Sort":
                            session.algorithm = "Bubble Sort"
                            session.state = BubbleSortState(array=arr)
                        elif algorithm == "Selection Sort":
                            session.algorithm = "Selection Sort"
                            session.state = SelectionSortState(array=arr)
                        elif algorithm == "Insertion Sort":
                            session.algorithm = "Insertion Sort"
                            session.state = InsertionSortState(array=arr)
                        elif algorithm == "Quick Sort":
                            session.algorithm = "Quick Sort"
                            session.state = QuickSortState(array=arr)
                        elif algorithm == "Merge Sort":
                            session.algorithm = "Merge Sort"
                            session.state = MergeSortState(array=arr)
                        elif algorithm == "Heap Sort":
                            session.algorithm = "Heap Sort"
                            session.state = HeapSortState(array=arr)
                        else:
                            return {
                                "status": "error",
                                "message": f"Unknown algorithm: {algorithm}"
                            }
                        
                        return session.state.step()
                    except ValueError:
                        return {
                            "status": "error",
                            "message": "Invalid array format. Please enter numbers separated by commas (e.g., 5,2,8,1,9)."
                        }
            
            # Handle sorting algorithm selection if in sorting menu
            if session.menu_state == "sort":
                if cmd_type == "sorting_algorithm":
                    return self._handle_sorting_algorithm_selection(session, parsed["selection"])
                else:
                    # Invalid selection, show menu again
                    return self._get_sorting_menu()
            
            # Menu command
            if cmd_type == "menu":
                session.menu_state = None
                session.waiting_for_array = False
                return self._get_main_menu()
            
            # Menu selection
            if cmd_type == "menu_selection":
                menu = parsed["menu"]
                session.menu_state = menu
                if menu == "sort":
                    return self._get_sorting_menu()
                elif menu == "path":
                    session.menu_state = None
                    return {
                        "status": "success",
                        "type": "info",
                        "message": "Got pathfinding command",
                    }
                elif menu == "struct":
                    session.menu_state = None
                    return {
                        "status": "success",
                        "type": "info",
                        "message": "Got structure command",
                    }
            
            # Next command
            if cmd_type == "next":
                if not session.state:
                    raise ValueError(
                        "No active algorithm. Start a sorting algorithm first."
                    )
                return session.state.step()
            
            # Explain command
            if cmd_type == "explain":
                if not session.algorithm or not session.state:
                    raise ValueError("No active algorithm to explain. Start a sorting session first.")
                
                algorithm_name = session.algorithm
                state = session.state
                
                # Get algorithm principle
                principle = self._get_algorithm_principle(algorithm_name)
                
                # Build step-by-step explanation based on algorithm type
                step_explanation = ""
                
                if isinstance(state, BubbleSortState):
                    recent_history = state.history[-5:] if hasattr(state, 'history') else []
                    history_text = (
                        "\n".join(f"- {entry}" for entry in recent_history)
                        if recent_history
                        else "- The algorithm is ready to start but no comparisons have been made yet."
                    )
                    if not state.completed and len(state.array) > 1:
                        if state.j >= len(state.array) - 1:
                            next_hint = (
                                f"The next pass will begin at index 0 after completing pass {state.i + 1}."
                            )
                        else:
                            next_hint = (
                                f"Upcoming action: compare indices {state.j} and {state.j + 1} "
                                f"({state.array[state.j]} vs {state.array[state.j + 1]})."
                            )
                    elif state.completed:
                        next_hint = "All elements are sorted. No further actions are required."
                    else:
                        next_hint = "Array of length 0 or 1; no actions required."

                    original = state.original_array if hasattr(state, 'original_array') else state.array
                    step_explanation = (
                        f"Current Progress:\n"
                        f"- Original array: {original}\n"
                        f"- Current array: {state.array}\n"
                        f"- Pass completed: {state.i}\n"
                        f"- Recent actions:\n{history_text}\n"
                        f"- {next_hint}"
                    )
                elif isinstance(state, (SelectionSortState, InsertionSortState, QuickSortState, MergeSortState, HeapSortState)):
                    # For other algorithms, provide current state information
                    if hasattr(state, 'completed') and state.completed:
                        step_explanation = (
                            f"Current Progress:\n"
                            f"- Array: {state.array}\n"
                            f"- Status: Sorting complete. All elements are in sorted order."
                        )
                    else:
                        step_explanation = (
                            f"Current Progress:\n"
                            f"- Array: {state.array}\n"
                            f"- Status: Algorithm is in progress. Use 'next' to see the next step."
                        )
                else:
                    step_explanation = (
                        f"Current Progress:\n"
                        f"- Array: {state.array if hasattr(state, 'array') else 'N/A'}\n"
                        f"- Status: Algorithm is running."
                    )
                
                # Combine principle and step-by-step explanation
                explanation = (
                    f"=== {algorithm_name} Explanation ===\n\n"
                    f"Algorithm Principle:\n{principle}\n\n"
                    f"{step_explanation}"
                )

                return {
                    "status": "success",
                    "type": "explanation",
                    "algorithm": algorithm_name,
                    "explanation": explanation,
                }
            
            # Reset command
            if cmd_type == "reset":
                session.reset()
                return {
                    "status": "success",
                    "type": "info",
                    "message": "Session reset.",
                }
            
            # Visualize command (legacy)
            if cmd_type == "visualize":
                algo = parsed.get("algorithm", "bubble sort")
                arr = parsed.get("array", [])
                if algo == "bubble sort":
                    session.algorithm = "Bubble Sort"
                    session.state = BubbleSortState(array=arr)
                    return session.state.step()
                else:
                    raise ValueError("Unknown algorithm. Supported: Bubble Sort.")
        
        # If ANTLR parsing failed, return error
        raise ValueError(
            "Unknown command or invalid syntax. Available commands: 'menu', 'sorting', '1-6' (algorithm selection), "
            "'next', 'explain', 'reset', or array input (e.g., '5,2,8,1,9')."
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

    def _get_main_menu(self) -> Dict[str, Any]:
        """Return the main selection menu."""
        menu_text = (
            "Hello, what are we going to do today, developer?\n"
            "1. Sorting algorithms.\n"
            "2. Pathfinding algorithms.\n"
            "3. Data structures"
        )
        
        return {
            "status": "success",
            "type": "greeting",
            "message": menu_text,
        }

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


