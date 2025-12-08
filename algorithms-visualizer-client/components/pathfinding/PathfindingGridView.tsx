import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { VisualizationGridData } from '@/stores/visualizationStore';

interface Props {
  grid: VisualizationGridData;
}

const PathfindingGridView: React.FC<Props> = ({ grid }) => {
  const rows = grid.grid_size.rows;
  const cols = grid.grid_size.cols;

  const startKey = `${grid.start[0]}-${grid.start[1]}`;
  const endKey = `${grid.end[0]}-${grid.end[1]}`;

  const barrierSet = new Set(grid.barriers.map(([r, c]) => `${r}-${c}`));
  const visitedSet = new Set((grid.visited || []).map(([r, c]) => `${r}-${c}`));
  const pathSet = new Set((grid.path || []).map(([r, c]) => `${r}-${c}`));
  const frontierSet = new Set((grid.frontier || []).map(([r, c]) => `${r}-${c}`));

  const cellSize = Math.min(320 / cols, 320 / rows);

  const renderCell = (r: number, c: number) => {
    const key = `${r}-${c}`;
    const isStart = key === startKey;
    const isEnd = key === endKey;
    const isBarrier = barrierSet.has(key);
    const isPath = pathSet.has(key);
    const isVisited = visitedSet.has(key);
    const isFrontier = frontierSet.has(key);

    let backgroundColor = '#f9fafb';
    if (isBarrier) backgroundColor = '#111827';
    else if (isStart) backgroundColor = '#10b981';
    else if (isEnd) backgroundColor = '#ef4444';
    else if (isPath) backgroundColor = '#fbbf24';
    else if (isFrontier) backgroundColor = '#38bdf8';
    else if (isVisited) backgroundColor = '#3b82f6';

    return (
      <View
        key={key}
        style={[
          styles.cell,
          {
            width: cellSize,
            height: cellSize,
            backgroundColor,
          },
        ]}
      />
    );
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Grid Progress</Text>
      <View style={styles.grid}>
        {Array.from({ length: rows }).map((_, r) => (
          <View key={`row-${r}`} style={styles.row}>
            {Array.from({ length: cols }).map((_, c) => renderCell(r, c))}
          </View>
        ))}
      </View>
      <View style={styles.legend}>
        <LegendItem label="Start" color="#10b981" />
        <LegendItem label="End" color="#ef4444" />
        <LegendItem label="Barrier" color="#111827" />
        <LegendItem label="Visited" color="#3b82f6" />
        <LegendItem label="Frontier" color="#38bdf8" />
        <LegendItem label="Path" color="#fbbf24" />
      </View>
    </View>
  );
};

const LegendItem = ({ label, color }: { label: string; color: string }) => (
  <View style={styles.legendItem}>
    <View style={[styles.legendSwatch, { backgroundColor: color }]} />
    <Text style={styles.legendLabel}>{label}</Text>
  </View>
);

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#ffffff',
    borderRadius: 12,
    padding: 12,
  },
  title: {
    fontSize: 16,
    fontWeight: '600',
    color: '#0f172a',
    marginBottom: 8,
  },
  grid: {
    alignItems: 'center',
    justifyContent: 'center',
  },
  row: {
    flexDirection: 'row',
  },
  cell: {
    borderWidth: 0.5,
    borderColor: '#e5e7eb',
    margin: 0.25,
  },
  legend: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginTop: 12,
    gap: 8,
  },
  legendItem: {
    flexDirection: 'row',
    alignItems: 'center',
    marginRight: 8,
  },
  legendSwatch: {
    width: 14,
    height: 14,
    borderRadius: 3,
    marginRight: 6,
  },
  legendLabel: {
    fontSize: 12,
    color: '#374151',
  },
});

export default PathfindingGridView;


