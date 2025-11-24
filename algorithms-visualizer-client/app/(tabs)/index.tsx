import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { router } from 'expo-router';
import { Ionicons } from '@expo/vector-icons';

export default function HomeScreen() {
  const handleStartVisualization = () => {
    router.push('/algorithms');
  };

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Algorithms Visualizer</Text>
        <Text style={styles.subtitle}>
          Learn algorithms through interactive visualizations
        </Text>
      </View>

      <View style={styles.content}>
        <TouchableOpacity
          style={styles.startButton}
          onPress={handleStartVisualization}
        >
          <Ionicons name="play" size={24} color="#FFFFFF" />
          <Text style={styles.startButtonText}>Start Learning</Text>
        </TouchableOpacity>

        <View style={styles.features}>
          <View style={styles.feature}>
            <Ionicons name="code-slash" size={32} color="#007AFF" />
            <Text style={styles.featureTitle}>Sorting Algorithms</Text>
            <Text style={styles.featureDescription}>
              Bubble Sort, Quick Sort, Merge Sort, and more
            </Text>
          </View>

          <View style={styles.feature}>
            <Ionicons name="map" size={32} color="#007AFF" />
            <Text style={styles.featureTitle}>Pathfinding</Text>
            <Text style={styles.featureDescription}>
              BFS, DFS, Dijkstra, A* algorithms
            </Text>
          </View>

          <View style={styles.feature}>
            <Ionicons name="layers" size={32} color="#007AFF" />
            <Text style={styles.featureTitle}>Data Structures</Text>
            <Text style={styles.featureDescription}>
              Arrays, Trees, Hash Tables, and more
            </Text>
          </View>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f8ff',
  },
  header: {
    padding: 24,
    paddingTop: 40,
    alignItems: 'center',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#111827',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    color: '#6B7280',
    textAlign: 'center',
    lineHeight: 24,
  },
  content: {
    flex: 1,
    padding: 24,
    justifyContent: 'center',
  },
  startButton: {
    backgroundColor: '#007AFF',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 16,
    paddingHorizontal: 32,
    borderRadius: 12,
    marginBottom: 40,
    shadowColor: '#007AFF',
    shadowOffset: {
      width: 0,
      height: 4,
    },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 8,
  },
  startButtonText: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: '600',
    marginLeft: 8,
  },
  features: {
    gap: 24,
  },
  feature: {
    backgroundColor: '#FFFFFF',
    padding: 20,
    borderRadius: 12,
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 4,
  },
  featureTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#111827',
    marginTop: 12,
    marginBottom: 8,
  },
  featureDescription: {
    fontSize: 14,
    color: '#6B7280',
    textAlign: 'center',
    lineHeight: 20,
  },
});







