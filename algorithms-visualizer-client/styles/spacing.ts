// Spacing Configuration
export const SPACING = {
  // Base spacing unit (8px)
  unit: 8,
  
  // Spacing scale
  xs: 4,    // 0.5 * unit
  sm: 8,    // 1 * unit
  md: 16,   // 2 * unit
  lg: 24,   // 3 * unit
  xl: 32,   // 4 * unit
  '2xl': 40, // 5 * unit
  '3xl': 48, // 6 * unit
  '4xl': 64, // 8 * unit
  
  // Component specific spacing
  component: {
    padding: 16,
    margin: 16,
    borderRadius: 8,
    borderWidth: 1,
  },
  
  // Layout spacing
  layout: {
    containerPadding: 16,
    sectionSpacing: 24,
    itemSpacing: 12,
  },
} as const;







