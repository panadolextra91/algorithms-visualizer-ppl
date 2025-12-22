import React, { useState, useCallback } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Alert,
} from 'react-native';
import ApiClient, { ApiResponse } from '@/services/api/client';

type CellType = 'empty' | 'start' | 'end' | 'barrier';

interface PathfindingGridProps {
  algorithm: string;
  gridSize: { rows: number; cols: number };
  sessionId: string;
  onGridConfigured: () => void;
  onVisualizationResponse?: (response: ApiResponse) => void;
}

export default function PathfindingGrid({
  algorithm,
  gridSize,
  sessionId,
  onGridConfigured,
  onVisualizationResponse,
}: PathfindingGridProps) {
  const { rows, cols } = gridSize;
  const [grid, setGrid] = useState<CellType[][]>(
    Array(rows).fill(null).map(() => Array(cols).fill('empty' as CellType))
  );
  const [mode, setMode] = useState<'start' | 'end' | 'barrier' | 'erase'>('start');
  const [startPos, setStartPos] = useState<[number, number] | null>(null);
  const [endPos, setEndPos] = useState<[number, number] | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleCellPress = useCallback(
    (row: number, col: number) => {
      const newGrid = grid.map(r => [...r]);
      const currentCell = grid[row][col];

      if (mode === 'start') {
        // Remove old start
        if (startPos) {
          newGrid[startPos[0]][startPos[1]] = 'empty';
        }
        // Set new start
        if (currentCell !== 'end') {
          newGrid[row][col] = 'start';
          setStartPos([row, col]);
        }
      } else if (mode === 'end') {
        // Remove old end
        if (endPos) {
          newGrid[endPos[0]][endPos[1]] = 'empty';
        }
        // Set new end
        if (currentCell !== 'start') {
          newGrid[row][col] = 'end';
          setEndPos([row, col]);
        }
      } else if (mode === 'barrier') {
        if (currentCell !== 'start' && currentCell !== 'end') {
          newGrid[row][col] = currentCell === 'barrier' ? 'empty' : 'barrier';
        }
      } else if (mode === 'erase') {
        if (currentCell === 'start') {
          setStartPos(null);
        } else if (currentCell === 'end') {
          setEndPos(null);
        }
        if (currentCell !== 'start' && currentCell !== 'end') {
          newGrid[row][col] = 'empty';
        }
      }

      setGrid(newGrid);
    },
    [grid, mode, startPos, endPos]
  );

  const handleDefaultMap = useCallback(
    async (difficulty: 'easy' | 'medium' | 'hard') => {
      console.log('[PathfindingGrid] Requesting default map:', {
        algorithm,
        difficulty,
        sessionId,
      });
      try {
        const response = await ApiClient.sendCommand(sessionId, difficulty);
        console.log('[PathfindingGrid] Default map response:', {
          status: response.status,
          type: response.type,
          message: response.message,
          response,
        });
        if (response.status === 'success') {
          onGridConfigured();
        } else {
          console.error('[PathfindingGrid] Default map error:', response.message);
          Alert.alert('Error', response.message || 'Failed to load default map');
        }
      } catch (error: any) {
        console.error('[PathfindingGrid] Error loading default map:', {
          error,
          message: error.message,
          stack: error.stack,
        });
        Alert.alert('Error', error.message || 'Failed to load default map');
      }
    },
    [sessionId, onGridConfigured, algorithm]
  );

  const handleStartVisualization = useCallback(async () => {
    if (isSubmitting) {
      console.log('[PathfindingGrid] Already submitting, ignoring click');
      return;
    }

    if (!startPos || !endPos) {
      Alert.alert('Error', 'Please set both start and end points');
      return;
    }

    setIsSubmitting(true);

    const barriers: [number, number][] = [];
    grid.forEach((row, r) => {
      row.forEach((cell, c) => {
        if (cell === 'barrier') {
          barriers.push([r, c]);
        }
      });
    });

    const gridConfig = {
      algorithm,
      start: startPos,
      end: endPos,
      barriers: barriers,
      grid_size: { rows, cols },
    };

    const gridConfigJson = JSON.stringify(gridConfig);
    console.log('[PathfindingGrid] Sending grid configuration:', {
      algorithm,
      sessionId,
      gridConfig,
      jsonString: gridConfigJson,
      barriersCount: barriers.length,
    });

    try {
      const response = await ApiClient.sendCommand(
        sessionId,
        gridConfigJson
      );
      console.log('[PathfindingGrid] Server response:', {
        status: response.status,
        type: response.type,
        message: response.message,
        response,
      });
      if (response.status === 'success') {
        // Notify parent (Chat) so it can feed this into the visualization store
        if (onVisualizationResponse) {
          onVisualizationResponse(response);
        }
        onGridConfigured();
      } else {
        console.error('[PathfindingGrid] Server returned error:', response.message);
        Alert.alert('Error', response.message || 'Failed to start visualization');
        setIsSubmitting(false);
      }
    } catch (error: any) {
      console.error('[PathfindingGrid] Error sending grid config:', {
        error,
        message: error.message,
        stack: error.stack,
      });
      Alert.alert('Error', error.message || 'Failed to start visualization');
      setIsSubmitting(false);
    }
  }, [grid, startPos, endPos, sessionId, onGridConfigured, onVisualizationResponse, isSubmitting]);

  const cellSize = Math.min(300 / cols, 300 / rows);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{algorithm} - Grid Configuration</Text>
      
      {/* Mode selector */}
      <View style={styles.modeContainer}>
        <TouchableOpacity
          style={[styles.modeButton, mode === 'start' && styles.modeButtonActive]}
          onPress={() => setMode('start')}
        >
          <Text style={[styles.modeButtonText, mode === 'start' && styles.modeButtonTextActive]}>
            Start
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.modeButton, mode === 'end' && styles.modeButtonActive]}
          onPress={() => setMode('end')}
        >
          <Text style={[styles.modeButtonText, mode === 'end' && styles.modeButtonTextActive]}>
            End
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.modeButton, mode === 'barrier' && styles.modeButtonActive]}
          onPress={() => setMode('barrier')}
        >
          <Text style={[styles.modeButtonText, mode === 'barrier' && styles.modeButtonTextActive]}>
            Barrier
          </Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.modeButton, mode === 'erase' && styles.modeButtonActive]}
          onPress={() => setMode('erase')}
        >
          <Text style={[styles.modeButtonText, mode === 'erase' && styles.modeButtonTextActive]}>
            Erase
          </Text>
        </TouchableOpacity>
      </View>

      {/* Grid */}
      <ScrollView horizontal showsHorizontalScrollIndicator={false}>
        <View style={styles.gridContainer}>
          {grid.map((row, rowIdx) => (
            <View key={rowIdx} style={styles.row}>
              {row.map((cell, colIdx) => (
                <TouchableOpacity
                  key={`${rowIdx}-${colIdx}`}
                  style={[
                    styles.cell,
                    {
                      width: cellSize,
                      height: cellSize,
                    },
                    cell === 'start' && styles.cellStart,
                    cell === 'end' && styles.cellEnd,
                    cell === 'barrier' && styles.cellBarrier,
                  ]}
                  onPress={() => handleCellPress(rowIdx, colIdx)}
                />
              ))}
            </View>
          ))}
        </View>
      </ScrollView>

      {/* Default maps */}
      <View style={styles.defaultMapsContainer}>
        <Text style={styles.defaultMapsTitle}>Or use preset maps:</Text>
        <View style={styles.defaultMapsButtons}>
          <TouchableOpacity
            style={styles.defaultMapButton}
            onPress={() => handleDefaultMap('easy')}
          >
            <Text style={styles.defaultMapButtonText}>Easy</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.defaultMapButton}
            onPress={() => handleDefaultMap('medium')}
          >
            <Text style={styles.defaultMapButtonText}>Medium</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.defaultMapButton}
            onPress={() => handleDefaultMap('hard')}
          >
            <Text style={styles.defaultMapButtonText}>Hard</Text>
          </TouchableOpacity>
        </View>
      </View>

      {/* Start button */}
      <TouchableOpacity
        style={[
          styles.startButton,
          ((!startPos || !endPos) || isSubmitting) && styles.startButtonDisabled,
        ]}
        onPress={handleStartVisualization}
        disabled={!startPos || !endPos || isSubmitting}
      >
        <Text style={styles.startButtonText}>
          {isSubmitting ? 'Starting...' : 'Start Visualization'}
        </Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 16,
    backgroundColor: '#ffffff',
    borderRadius: 12,
    marginVertical: 8,
  },
  title: {
    fontSize: 18,
    fontWeight: '600',
    color: '#0f172a',
    marginBottom: 12,
    textAlign: 'center',
  },
  modeContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginBottom: 16,
    gap: 8,
  },
  modeButton: {
    flex: 1,
    paddingVertical: 8,
    paddingHorizontal: 12,
    borderRadius: 8,
    backgroundColor: '#e5e7eb',
    alignItems: 'center',
  },
  modeButtonActive: {
    backgroundColor: '#127a7f',
  },
  modeButtonText: {
    fontSize: 14,
    fontWeight: '500',
    color: '#374151',
  },
  modeButtonTextActive: {
    color: '#ffffff',
  },
  gridContainer: {
    alignItems: 'center',
    marginBottom: 16,
  },
  row: {
    flexDirection: 'row',
  },
  cell: {
    borderWidth: 1,
    borderColor: '#d1d5db',
    backgroundColor: '#f9fafb',
    margin: 0.5,
  },
  cellStart: {
    backgroundColor: '#10b981',
  },
  cellEnd: {
    backgroundColor: '#ef4444',
  },
  cellBarrier: {
    backgroundColor: '#1f2937',
  },
  defaultMapsContainer: {
    marginBottom: 16,
  },
  defaultMapsTitle: {
    fontSize: 14,
    fontWeight: '500',
    color: '#374151',
    marginBottom: 8,
  },
  defaultMapsButtons: {
    flexDirection: 'row',
    gap: 8,
  },
  defaultMapButton: {
    flex: 1,
    paddingVertical: 10,
    paddingHorizontal: 16,
    borderRadius: 8,
    backgroundColor: '#dbeafe',
    borderWidth: 1,
    borderColor: '#93c5fd',
    alignItems: 'center',
  },
  defaultMapButtonText: {
    fontSize: 14,
    fontWeight: '500',
    color: '#1e40af',
  },
  startButton: {
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
    backgroundColor: '#127a7f',
    alignItems: 'center',
  },
  startButtonDisabled: {
    backgroundColor: '#9ca3af',
  },
  startButtonText: {
    fontSize: 16,
    fontWeight: '600',
    color: '#ffffff',
  },
});

