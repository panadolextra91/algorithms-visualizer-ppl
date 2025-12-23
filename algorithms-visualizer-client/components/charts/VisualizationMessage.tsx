import React from 'react';
import { View, StyleSheet, Text, TouchableOpacity, ActivityIndicator } from 'react-native';
import BarChart from './BarChart';
import DataStructureView from '../data-structures/DataStructureView';

import { DataStructureState, VisualizationGridData } from '@/stores/visualizationStore';
import PathfindingGridView from '../pathfinding/PathfindingGridView';

interface VisualizationMessageProps {
  algorithm: string;
  step: number;
  data: {
    array?: number[];
    highlighted_indices?: number[];
    sorted_indices?: number[];
    grid?: VisualizationGridData;
    dataStructureState?: DataStructureState;
  };
  explanation: string;
  onNextStep?: () => void;
  onPreviousStep?: () => void;
  loadingNext?: boolean;
  canGoPrevious?: boolean;
  canGoNext?: boolean;
  currentIndex?: number;
  totalSteps?: number;
}

const VisualizationMessage: React.FC<VisualizationMessageProps> = ({
  algorithm,
  step,
  data,
  explanation,
  onNextStep,
  onPreviousStep,
  loadingNext = false,
  canGoPrevious = false,
  canGoNext = true,
  currentIndex,
  totalSteps,
}) => {
  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.algorithmName}>{algorithm}</Text>
        <Text style={styles.stepText}>
          Step {step}
          {totalSteps && totalSteps > 0 && currentIndex !== undefined
            ? `  (${currentIndex + 1}/${totalSteps})`
            : ''}
        </Text>
      </View>
      
      {data.grid ? (
        <PathfindingGridView grid={data.grid} />
      ) : data.dataStructureState ? (
        <DataStructureView state={data.dataStructureState} />
      ) : (
        <BarChart
          data={data.array || []}
          highlightedIndices={data.highlighted_indices || []}
          sortedIndices={data.sorted_indices || []}
        />
      )}
      
      <View style={styles.explanationContainer}>
        <Text style={styles.explanationText}>{explanation}</Text>
      </View>

      {(onNextStep || onPreviousStep) && (
        <View style={styles.actionsRow}>
          {onPreviousStep && (
            <TouchableOpacity
              style={[
                styles.navButton,
                (!canGoPrevious || loadingNext) && styles.navButtonDisabled,
              ]}
              onPress={onPreviousStep}
              disabled={!canGoPrevious || loadingNext}
            >
              <Text style={styles.navButtonText}>Previous</Text>
            </TouchableOpacity>
          )}
          {onNextStep && (
            <TouchableOpacity
              style={[
                styles.navButton,
                (!canGoNext || loadingNext) && styles.navButtonDisabled,
              ]}
              onPress={onNextStep}
              disabled={!canGoNext || loadingNext}
            >
              {loadingNext ? (
                <ActivityIndicator size="small" color="#FFFFFF" />
              ) : (
                <Text style={styles.navButtonText}>Next</Text>
              )}
            </TouchableOpacity>
          )}
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 16,
    marginVertical: 8,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 4,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  algorithmName: {
    fontSize: 18,
    fontWeight: '600',
    color: '#111827',
  },
  stepText: {
    fontSize: 14,
    fontWeight: '500',
    color: '#6B7280',
  },
  explanationContainer: {
    marginTop: 12,
    paddingTop: 12,
    borderTopWidth: 1,
    borderTopColor: '#E5E7EB',
  },
  explanationText: {
    fontSize: 14,
    lineHeight: 20,
    color: '#374151',
  },
  actionsRow: {
    marginTop: 16,
    flexDirection: 'row',
    justifyContent: 'flex-end',
  },
  navButton: {
    backgroundColor: '#127a7f',
    paddingVertical: 10,
    paddingHorizontal: 18,
    borderRadius: 999,
    minWidth: 110,
    alignItems: 'center',
    marginLeft: 12,
  },
  navButtonDisabled: {
    opacity: 0.5,
  },
  navButtonText: {
    color: '#FFFFFF',
    fontSize: 14,
    fontWeight: '600',
  },
});

export default VisualizationMessage;
