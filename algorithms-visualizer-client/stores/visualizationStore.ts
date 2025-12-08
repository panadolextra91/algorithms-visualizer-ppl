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
  step: number;
  data: {
    array?: number[];
    highlighted_indices?: number[];
    sorted_indices?: number[];
    grid?: VisualizationGridData;
  };
  explanation: string;
  isFinal?: boolean;
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

