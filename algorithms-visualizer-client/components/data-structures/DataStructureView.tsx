import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { DataStructureState } from '@/stores/visualizationStore';

interface Props {
  state: DataStructureState;
}

const colors = {
  border: '#CBD5E1',
  text: '#0F172A',
  highlight: '#0EA5E9',
  visited: '#A5B4FC',
  background: '#F8FAFC',
};

const Box: React.FC<{
  value: number | string;
  highlighted?: boolean;
  label?: string;
}> = ({ value, highlighted, label }) => (
  <View
    style={[
      styles.box,
      highlighted && { borderColor: colors.highlight, backgroundColor: '#E0F2FE' },
    ]}
  >
    <Text style={styles.boxValue}>{value}</Text>
    {label ? <Text style={styles.boxLabel}>{label}</Text> : null}
  </View>
);

const DataStructureView: React.FC<Props> = ({ state }) => {
  if (state.type === 'array') {
    const highlightedSet = new Set(state.highlighted_indices || []);
    return (
      <View style={styles.row}>
        {(state.values || []).map((v, idx) => (
          <Box key={idx} value={v} highlighted={highlightedSet.has(idx)} label={idx.toString()} />
        ))}
      </View>
    );
  }

  if (state.type === 'stack') {
    const top = state.top_index ?? -1;
    return (
      <View style={[styles.columnReverse, { alignItems: 'center' }]}>
        {(state.values || []).map((v, idx) => {
          const absoluteIdx = idx; // bottom->top order because of columnReverse
          const isTop = (state.values?.length || 0) - 1 - idx === top;
          return (
            <Box
              key={absoluteIdx}
              value={v}
              highlighted={isTop}
              label={isTop ? 'top' : undefined}
            />
          );
        })}
      </View>
    );
  }

  if (state.type === 'queue') {
    const front = state.front_index ?? -1;
    const rear = state.rear_index ?? -1;
    return (
      <View style={styles.row}>
        {(state.values || []).map((v, idx) => {
          const isFront = idx === front;
          const isRear = idx === rear;
          const label = isFront ? 'front' : isRear ? 'rear' : undefined;
          return <Box key={idx} value={v} highlighted={isFront || isRear} label={label} />;
        })}
      </View>
    );
  }

  if (state.type === 'linked_list') {
    const visited = new Set(state.visited_indices || []);
    const nodes = state.nodes || [];
    return (
      <View style={[styles.row, styles.wrap]}>
        {nodes.map((node, idx) => {
          const isVisited = visited.has(idx);
          const isHead = state.head_index === idx;
          const isCurrent = state.current_index === idx;
          return (
            <View key={idx} style={styles.linkNode}>
              <Box
                value={node.value}
                highlighted={isCurrent}
                label={isHead ? 'head' : isVisited ? 'visited' : undefined}
              />
              {node.next !== null && node.next !== undefined ? <Text style={styles.arrow}>→</Text> : null}
            </View>
          );
        })}
      </View>
    );
  }

  return (
    <View style={styles.fallback}>
      <Text style={styles.fallbackText}>Unsupported data structure view.</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  row: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    flexWrap: 'wrap',
    gap: 8,
  },
  columnReverse: {
    flexDirection: 'column-reverse',
    gap: 8,
  },
  box: {
    minWidth: 44,
    minHeight: 44,
    paddingHorizontal: 10,
    paddingVertical: 8,
    borderWidth: 2,
    borderColor: colors.border,
    borderRadius: 8,
    backgroundColor: colors.background,
    alignItems: 'center',
    justifyContent: 'center',
  },
  boxValue: {
    fontSize: 16,
    fontWeight: '600',
    color: colors.text,
  },
  boxLabel: {
    marginTop: 2,
    fontSize: 11,
    color: '#475569',
  },
  linkNode: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  arrow: {
    marginHorizontal: 6,
    color: '#475569',
    fontSize: 16,
  },
  fallback: {
    padding: 12,
    borderRadius: 8,
    backgroundColor: '#FEF2F2',
    borderWidth: 1,
    borderColor: '#FCA5A5',
    alignItems: 'center',
  },
  fallbackText: {
    color: '#991B1B',
    fontWeight: '600',
  },
});

export default DataStructureView;

