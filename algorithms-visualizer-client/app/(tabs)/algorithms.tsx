import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, ScrollView } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const ALGORITHM_CATEGORIES = [
  {
    id: 'sorting',
    title: 'Sorting Algorithms',
    icon: 'swap-vertical',
    description: 'Learn how sorting algorithms work',
    algorithms: ['Bubble Sort', 'Quick Sort', 'Merge Sort', 'Selection Sort', 'Insertion Sort', 'Heap Sort'],
  },
  {
    id: 'pathfinding',
    title: 'Pathfinding Algorithms',
    icon: 'map',
    description: 'Find the shortest path',
    algorithms: ['BFS', 'DFS', 'Dijkstra', 'A*'],
  },
  {
    id: 'data-structures',
    title: 'Data Structures',
    icon: 'layers',
    description: 'Understand data organization',
    algorithms: ['Array', 'Stack', 'Queue', 'Linked List', 'Binary Tree', 'Hash Table', 'Trie'],
  },
];

export default function AlgorithmsScreen() {
  const handleCategoryPress = (categoryId: string) => {
    // TODO: Navigate to specific algorithm category
    console.log(`Selected category: ${categoryId}`);
  };

  return (
    <ScrollView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Choose Algorithm Category</Text>
        <Text style={styles.subtitle}>
          Select a category to start learning algorithms
        </Text>
      </View>

      <View style={styles.categories}>
        {ALGORITHM_CATEGORIES.map((category) => (
          <TouchableOpacity
            key={category.id}
            style={styles.categoryCard}
            onPress={() => handleCategoryPress(category.id)}
          >
            <View style={styles.categoryHeader}>
              <View style={styles.iconContainer}>
                <Ionicons name={category.icon as any} size={32} color="#007AFF" />
              </View>
              <View style={styles.categoryInfo}>
                <Text style={styles.categoryTitle}>{category.title}</Text>
                <Text style={styles.categoryDescription}>{category.description}</Text>
              </View>
              <Ionicons name="chevron-forward" size={20} color="#6B7280" />
            </View>
            
            <View style={styles.algorithmsList}>
              {category.algorithms.map((algorithm, index) => (
                <View key={index} style={styles.algorithmItem}>
                  <View style={styles.algorithmDot} />
                  <Text style={styles.algorithmName}>{algorithm}</Text>
                </View>
              ))}
            </View>
          </TouchableOpacity>
        ))}
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f8ff',
  },
  header: {
    padding: 24,
    paddingTop: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#111827',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    color: '#6B7280',
    lineHeight: 24,
  },
  categories: {
    padding: 24,
    paddingTop: 0,
    gap: 16,
  },
  categoryCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 20,
    shadowColor: '#000',
    shadowOffset: {
      width: 0,
      height: 2,
    },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 4,
  },
  categoryHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 16,
  },
  iconContainer: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: '#f0f8ff',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 16,
  },
  categoryInfo: {
    flex: 1,
  },
  categoryTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#111827',
    marginBottom: 4,
  },
  categoryDescription: {
    fontSize: 14,
    color: '#6B7280',
  },
  algorithmsList: {
    gap: 8,
  },
  algorithmItem: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 4,
  },
  algorithmDot: {
    width: 6,
    height: 6,
    borderRadius: 3,
    backgroundColor: '#007AFF',
    marginRight: 12,
  },
  algorithmName: {
    fontSize: 14,
    color: '#374151',
  },
});







