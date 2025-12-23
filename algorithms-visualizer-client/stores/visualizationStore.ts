import { create } from 'zustand';

export interface VisualizationGridData {
  start: number[];
  end: number[];
  barriers: number[][];
  grid_size: { rows: number; cols: number };
  visited?: number[][];
  path?: number[][];
  frontier?: number[][];
}

export interface VisualizationStepData {
  algorithm: string;
  dataStructure?: string;
  step: number;
  data: {
    array?: number[];
    highlighted_indices?: number[];
    sorted_indices?: number[];
    grid?: VisualizationGridData;
    dataStructureState?: DataStructureState;
  };
  explanation: string;
  isFinal?: boolean;
}

export interface DataStructureState {
  type: 'array' | 'stack' | 'queue' | 'linked_list';
  values?: number[];
  highlighted_indices?: number[];
  // Stack-specific
  top_index?: number;
  operation?: string;
  pushed_value?: number;
  popped_value?: number;
  // Queue-specific
  front_index?: number;
  rear_index?: number;
  enqueued_value?: number;
  dequeued_value?: number;
  // Linked list specific
  nodes?: { value: number; next: number | null }[];
  head_index?: number | null;
  current_index?: number | null;
  visited_indices?: number[];
}

interface VisualizationStore {
  steps: VisualizationStepData[];
  currentIndex: number;
  algorithm?: string;
  addStep: (step: VisualizationStepData) => void;
  goNextCached: () => boolean;
  goPrevious: () => boolean;
  reset: () => void;
}

export const useVisualizationStore = create<VisualizationStore>((set, get) => ({
  steps: [],
  currentIndex: -1,
  algorithm: undefined,
  addStep: (step: VisualizationStepData) => {
    set(state => {
      const isDifferentAlgorithm =
        state.algorithm && state.algorithm !== step.algorithm;

      const stepsBase = isDifferentAlgorithm
        ? []
        : state.steps.slice(0, state.currentIndex + 1);

      const updatedSteps = [...stepsBase, step];

      return {
        steps: updatedSteps,
        currentIndex: updatedSteps.length - 1,
        algorithm: step.algorithm,
      };
    });
  },
  goNextCached: () => {
    const { currentIndex, steps } = get();
    if (currentIndex < steps.length - 1) {
      set({ currentIndex: currentIndex + 1 });
      return true;
    }
    return false;
  },
  goPrevious: () => {
    const { currentIndex } = get();
    if (currentIndex > 0) {
      set({ currentIndex: currentIndex - 1 });
      return true;
    }
    return false;
  },
  reset: () => set({ steps: [], currentIndex: -1, algorithm: undefined }),
}));

