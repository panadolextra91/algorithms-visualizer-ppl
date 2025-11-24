import React, { useState } from 'react';
import { View, StyleSheet, Dimensions, Text, LayoutChangeEvent } from 'react-native';

const { width: SCREEN_WIDTH } = Dimensions.get('window');

interface BarChartProps {
  data: number[];
  highlightedIndices?: number[];
  sortedIndices?: number[];
  swappingIndices?: number[];
  maxValue?: number;
}

const BarChart: React.FC<BarChartProps> = ({
  data,
  highlightedIndices = [],
  sortedIndices = [],
  swappingIndices = [],
  maxValue,
}) => {
  const [containerWidth, setContainerWidth] = useState<number>(SCREEN_WIDTH - 32);

  // Handle empty data
  if (!data || data.length === 0) {
    return (
      <View style={styles.container}>
        <Text style={styles.emptyText}>No data to display</Text>
      </View>
    );
  }

  // Calculate max value if not provided
  const max = maxValue || Math.max(...data, 1);
  const chartWidth = containerWidth;
  const totalSpacing = (data.length - 1) * 4;
  const rawWidth = (chartWidth - totalSpacing) / data.length;
  const barWidth = Math.max(8, Math.min(rawWidth, 60)); // clamp width to keep bars visible and within card

  const getBarColor = (index: number): string => {
    // Check if swapping (highest priority)
    if (swappingIndices.includes(index)) {
      return '#EF4444'; // Red
    }
    // Check if highlighted/comparing
    if (highlightedIndices.includes(index)) {
      return '#F59E0B'; // Yellow
    }
    // Check if sorted
    if (sortedIndices.includes(index)) {
      return '#10B981'; // Green
    }
    // Default unsorted
    return '#6B7280'; // Gray
  };

  const getBarHeight = (value: number): number => {
    const maxHeight = 200; // Maximum bar height in pixels
    return (value / max) * maxHeight;
  };

  const handleLayout = (event: LayoutChangeEvent) => {
    const { width } = event.nativeEvent.layout;
    if (width && Math.abs(width - containerWidth) > 1) {
      setContainerWidth(width);
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.chartContainer} onLayout={handleLayout}>
        {data.map((value, index) => {
          const height = getBarHeight(value);
          const color = getBarColor(index);

          return (
            <View key={index} style={styles.barWrapper}>
              <View
                style={[
                  styles.bar,
                  {
                    width: barWidth,
                    height,
                    backgroundColor: color,
                  },
                ]}
              />
              <Text style={styles.barLabel}>{value}</Text>
            </View>
          );
        })}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    paddingVertical: 16,
    paddingHorizontal: 16,
  },
  chartContainer: {
    flexDirection: 'row',
    alignItems: 'flex-end',
    justifyContent: 'center',
    height: 250,
    paddingBottom: 30, // Space for labels
  },
  barWrapper: {
    alignItems: 'center',
    marginHorizontal: 2,
  },
  bar: {
    borderRadius: 4,
    minHeight: 4,
  },
  barLabel: {
    marginTop: 4,
    fontSize: 12,
    fontWeight: '600',
    color: '#374151',
  },
  emptyText: {
    textAlign: 'center',
    color: '#6B7280',
    fontSize: 14,
    paddingVertical: 20,
  },
});

export default BarChart;
