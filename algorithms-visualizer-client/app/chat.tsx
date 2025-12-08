import React, { useState, useEffect, useRef, useCallback } from 'react';
import {
  View,
  StyleSheet,
  StatusBar,
  Text,
  TextInput,
  TouchableOpacity,
  ScrollView,
  KeyboardAvoidingView,
  Platform,
  ActivityIndicator,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';
import ApiClient, { ApiResponse } from '@/services/api/client';
import SessionManager from '@/services/session/SessionManager';
import { VisualizationMessage } from '@/components/charts';
import PathfindingGrid from '@/components/pathfinding/PathfindingGrid';
import { useVisualizationStore } from '@/stores/visualizationStore';

type MessageType = 'text' | 'visualization_card' | 'menu' | 'await_array' | 'await_grid';

interface MenuOption {
  id: string;
  label: string;
}

interface Message {
  id: string;
  text: string;
  isUser: boolean;
  timestamp: Date;
  type?: MessageType;
  options?: MenuOption[];
  algorithm?: string;
  grid_size?: { rows: number; cols: number };
}

export default function ChatScreen() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputText, setInputText] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId, setSessionId] = useState<string>('');
  const [isNextLoading, setIsNextLoading] = useState(false);
  const scrollViewRef = useRef<ScrollView>(null);

  const currentVisualizationStep = useVisualizationStore(state =>
    state.currentIndex >= 0 ? state.steps[state.currentIndex] : null
  );
  const visualizationIndex = useVisualizationStore(state => state.currentIndex);
  const totalVisualizationSteps = useVisualizationStore(state => state.steps.length);
  const hasPreviousStep = useVisualizationStore(state => state.currentIndex > 0);
  const hasNextCachedStep = useVisualizationStore(
    state => state.currentIndex >= 0 && state.currentIndex < state.steps.length - 1
  );
  const currentVisualizationAlgorithm = useVisualizationStore(state => state.algorithm);
  const addVisualizationStep = useVisualizationStore(state => state.addStep);
  const goPreviousStep = useVisualizationStore(state => state.goPrevious);
  const goNextCached = useVisualizationStore(state => state.goNextCached);
  const resetVisualization = useVisualizationStore(state => state.reset);

  const ensureVisualizationMessage = () => {
    setMessages(prev => {
      const exists = prev.some(msg => msg.type === 'visualization_card');
      if (exists) {
        return prev;
      }
      const visualizationMessage: Message = {
        id: `visualization-${Date.now()}`,
        text: '',
        isUser: false,
        timestamp: new Date(),
        type: 'visualization_card',
      };
      return [...prev, visualizationMessage];
    });
  };

  const maybeHandleVisualizationResponse = (response: ApiResponse): boolean => {
    if (
      response.type === 'visualization_step' &&
      response.algorithm &&
      response.data &&
      (Array.isArray(response.data.array) || response.data.grid) &&
      response.explanation
    ) {
      if (
        currentVisualizationAlgorithm &&
        response.algorithm !== currentVisualizationAlgorithm
      ) {
        resetVisualization();
      }

      const isFinalStep =
        (response.step ?? 0) === -1 ||
        (response.data.sorted_indices?.length || 0) === response.data.array.length;

      addVisualizationStep({
        algorithm: response.algorithm,
        step: response.step ?? 0,
        data: {
          array: response.data.array,
          highlighted_indices: response.data.highlighted_indices || [],
          sorted_indices: response.data.sorted_indices || [],
          grid: (response as any).data?.grid,
        },
        explanation: response.explanation,
        isFinal: isFinalStep,
      });
      ensureVisualizationMessage();
      return true;
    }
    return false;
  };

  const convertResponseToMessages = useCallback(
    (response: ApiResponse): Message[] => {
      if (response.type === 'menu' || response.type === 'sorting_menu') {
        return [
          {
            id: `${response.type}-${Date.now()}`,
            text: response.message || 'Choose an option below.',
            isUser: false,
            timestamp: new Date(),
            type: 'menu',
            options: response.options || [],
          },
        ];
      }

      if (response.type === 'await_array') {
        return [
          {
            id: `await-array-${Date.now()}`,
            text:
              response.message ||
              'Enter the array as comma-separated integers, e.g., 5, 1, 3.',
            isUser: false,
            timestamp: new Date(),
            type: 'await_array',
            algorithm: response.algorithm,
          },
        ];
      }

      if (response.type === 'await_grid') {
        return [
          {
            id: `await-grid-${Date.now()}`,
            text: response.message || 'Configure the grid for pathfinding.',
            isUser: false,
            timestamp: new Date(),
            type: 'await_grid',
            algorithm: response.algorithm,
            grid_size: response.grid_size || { rows: 15, cols: 15 },
          },
        ];
      }

      const text =
        response.message ||
        response.explanation ||
        (response.status === 'error'
          ? 'An error occurred. Please try again.'
          : 'No response from server');

      return [
        {
          id: `server-${Date.now()}`,
          text,
          isUser: false,
          timestamp: new Date(),
          type: 'text',
        },
      ];
    },
    []
  );

  const handleServerResponse = useCallback(
    (response: ApiResponse) => {
      const newMessages = convertResponseToMessages(response);
      if (newMessages.length) {
        setMessages(prev => [...prev, ...newMessages]);
      }
    },
    [convertResponseToMessages]
  );

  useEffect(() => {
    // Initialize session and load greeting
    const initializeChat = async () => {
      try {
        const id = await SessionManager.getSessionId();
        setSessionId(id);

        // Load greeting message
        const greeting = await ApiClient.getGreeting();
        if (greeting.status === 'success') {
          const handled = maybeHandleVisualizationResponse(greeting);
          if (!handled) {
            handleServerResponse(greeting);
          }
        }
      } catch (error: any) {
        console.error('Failed to initialize chat:', error);
        // Show error message
        const errorMessage: Message = {
          id: 'error',
          text:
            error?.message ||
            'Failed to connect to server. Make sure the server is running on port 8069.',
          isUser: false,
          timestamp: new Date(),
          type: 'text',
        };
        setMessages([errorMessage]);
      }
    };

    initializeChat();
  }, [handleServerResponse]);

  useEffect(() => {
    // Auto-scroll to bottom when new messages arrive
    if (messages.length > 0) {
      setTimeout(() => {
        scrollViewRef.current?.scrollToEnd({ animated: true });
      }, 100);
    }
  }, [messages]);

  const sendCommand = useCallback(
    async (rawText: string, displayText?: string) => {
      const trimmed = rawText.trim();
      if (!trimmed || isLoading) {
        return;
      }

      const userMessage: Message = {
        id: Date.now().toString(),
        text: displayText || trimmed,
        isUser: true,
        timestamp: new Date(),
        type: 'text',
      };

      if (trimmed.toLowerCase() === 'reset') {
        resetVisualization();
      }

      setMessages(prev => [...prev, userMessage]);
      setInputText('');
      setIsLoading(true);

      try {
        const response = await ApiClient.sendCommand(sessionId, trimmed);

        const handled = maybeHandleVisualizationResponse(response);
        if (!handled) {
          handleServerResponse(response);
        }
      } catch (error: any) {
        console.error('Failed to send message:', error);
        const errorMessage: Message = {
          id: (Date.now() + 1).toString(),
          text: error?.message || 'Failed to send message. Please try again.',
          isUser: false,
          timestamp: new Date(),
          type: 'text',
        };
        setMessages(prev => [...prev, errorMessage]);
      } finally {
        setIsLoading(false);
        setIsNextLoading(false);
      }
    },
    [handleServerResponse, isLoading, maybeHandleVisualizationResponse, resetVisualization, sessionId]
  );

  const handleSendMessage = () => {
    sendCommand(inputText);
  };

  const handlePreviousStep = () => {
    if (!currentVisualizationStep) {
      return;
    }
    const moved = goPreviousStep();
    if (!moved) {
      const infoMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: 'You are already at the first step.',
        isUser: false,
        timestamp: new Date(),
        type: 'text',
      };
      setMessages(prev => [...prev, infoMessage]);
    }
  };

  const handleNextStep = async () => {
    if (goNextCached()) {
      return;
    }

    if (
      !sessionId ||
      isNextLoading ||
      isLoading ||
      !currentVisualizationStep ||
      currentVisualizationStep.isFinal
    ) {
      return;
    }

    setIsNextLoading(true);

    try {
      const response = await ApiClient.sendCommand(sessionId, 'next');
      const handled = maybeHandleVisualizationResponse(response);
      if (!handled) {
        const serverMessage: Message = {
          id: (Date.now() + 1).toString(),
          text: response.message || response.explanation || 'No response from server',
          isUser: false,
          timestamp: new Date(),
          type: 'text',
        };
        setMessages(prev => [...prev, serverMessage]);
      }
    } catch (error: any) {
      console.error('Failed to fetch next step:', error);
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: error?.message || 'Failed to fetch next step. Please try again.',
        isUser: false,
        timestamp: new Date(),
        type: 'text',
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsNextLoading(false);
    }
  };

  const renderMessage = (message: Message) => {
    if (message.type === 'visualization_card') {
      if (!currentVisualizationStep) {
        return <React.Fragment key={message.id} />;
      }

      return (
        <View key={message.id} style={styles.visualizationWrapper}>
          <VisualizationMessage
            algorithm={currentVisualizationStep.algorithm}
            step={currentVisualizationStep.step}
            data={currentVisualizationStep.data}
            explanation={currentVisualizationStep.explanation}
            onNextStep={handleNextStep}
            onPreviousStep={handlePreviousStep}
            loadingNext={isNextLoading}
            canGoPrevious={hasPreviousStep}
            canGoNext={
              !isNextLoading &&
              (hasNextCachedStep || !currentVisualizationStep.isFinal)
            }
            currentIndex={visualizationIndex >= 0 ? visualizationIndex : undefined}
            totalSteps={totalVisualizationSteps}
          />
        </View>
      );
    }

    if (message.type === 'menu') {
      // Render menu as plain text, just like regular messages
      return (
        <View
          key={message.id}
          style={[
            styles.messageContainer,
            styles.serverMessage,
          ]}
        >
          <Text
            style={[
              styles.messageText,
              styles.serverText,
            ]}
          >
            {message.text.split('\n').map((line, index, arr) => (
              <Text key={`${message.id}-${index}`}>
                {line}
                {index < arr.length - 1 ? '\n' : ''}
              </Text>
            ))}
          </Text>
        </View>
      );
    }

    if (message.type === 'await_array') {
      // Render await_array as plain text, just like regular messages
      return (
        <View
          key={message.id}
          style={[
            styles.messageContainer,
            styles.serverMessage,
          ]}
        >
          <Text
            style={[
              styles.messageText,
              styles.serverText,
            ]}
          >
            {message.text.split('\n').map((line, index, arr) => (
              <Text key={`${message.id}-${index}`}>
                {line}
                {index < arr.length - 1 ? '\n' : ''}
              </Text>
            ))}
          </Text>
        </View>
      );
    }

    if (message.type === 'await_grid') {
      return (
        <View key={message.id} style={styles.gridWrapper}>
          <PathfindingGrid
            algorithm={message.algorithm || 'Pathfinding'}
            gridSize={message.grid_size || { rows: 15, cols: 15 }}
            sessionId={sessionId}
            onGridConfigured={() => {
              // Grid configured, visualization will start
              // The server response will be handled by maybeHandleVisualizationResponse
            }}
          />
        </View>
      );
    }

    // Render regular text message
    return (
      <View
        key={message.id}
        style={[
          styles.messageContainer,
          message.isUser ? styles.userMessage : styles.serverMessage,
        ]}
      >
        <Text
          style={[
            styles.messageText,
            message.isUser ? styles.userText : styles.serverText,
          ]}
        >
          {message.text.split('\n').map((line, index, arr) => (
            <Text key={`${message.id}-${index}`}>
              {line}
              {index < arr.length - 1 ? '\n' : ''}
            </Text>
          ))}
        </Text>
      </View>
    );
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#f0f8ff" />
      
      <KeyboardAvoidingView
        style={styles.keyboardAvoidingView}
        behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
        keyboardVerticalOffset={Platform.OS === 'ios' ? 0 : 20}
      >
        {/* Messages Area */}
        <ScrollView
          ref={scrollViewRef}
          style={styles.messagesContainer}
          contentContainerStyle={styles.messagesContent}
          showsVerticalScrollIndicator={false}
        >
          {messages.map(renderMessage)}
          {isLoading && (
            <View style={styles.loadingContainer}>
              <ActivityIndicator size="small" color="#127a7f" />
            </View>
          )}
        </ScrollView>

        {/* Input Area */}
        <View style={styles.inputContainer}>
          <View style={styles.inputWrapper}>
            <TextInput
              style={styles.textInput}
              value={inputText}
              onChangeText={setInputText}
              placeholder="Type your message..."
              placeholderTextColor="#9CA3AF"
              multiline
              maxLength={500}
            />
            <TouchableOpacity
              style={[
                styles.sendButton,
                (inputText.trim() && !isLoading) ? styles.sendButtonActive : styles.sendButtonInactive,
              ]}
              onPress={handleSendMessage}
              disabled={!inputText.trim() || isLoading}
            >
              {isLoading ? (
                <ActivityIndicator size="small" color="#9CA3AF" />
              ) : (
                <Ionicons
                  name="send"
                  size={20}
                  color={inputText.trim() ? '#FFFFFF' : '#9CA3AF'}
                />
              )}
            </TouchableOpacity>
          </View>
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f0f8ff',
  },
  keyboardAvoidingView: {
    flex: 1,
  },
  messagesContainer: {
    flex: 1,
  },
  messagesContent: {
    padding: 16,
    paddingBottom: 8,
  },
  messageContainer: {
    marginVertical: 4,
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderRadius: 20,
    maxWidth: '85%',
    alignSelf: 'flex-start',
  },
  userMessage: {
    backgroundColor: '#127a7f',
    alignSelf: 'flex-end',
    marginLeft: '15%',
  },
  serverMessage: {
    backgroundColor: '#bec8d1',
    alignSelf: 'flex-start',
    marginRight: '15%',
  },
  messageText: {
    fontSize: 16,
    lineHeight: 22,
  },
  userText: {
    color: '#f0f8ff',
  },
  serverText: {
    color: '#373b3e',
  },
  inputContainer: {
    backgroundColor: '#f0f8ff',
    paddingHorizontal: 16,
    paddingTop: 12,
    paddingBottom: 0,
    flex: 0,
  },
  inputWrapper: {
    flexDirection: 'row',
    alignItems: 'flex-end',
    backgroundColor: '#FFFFFF',
    borderRadius: 24,
    paddingHorizontal: 16,
    paddingVertical: 8,
    paddingBottom: 12,
    minHeight: 48,
    maxHeight: 200,
    marginBottom: 16,
  },
  textInput: {
    flex: 1,
    fontSize: 16,
    color: '#111827',
    paddingVertical: 8,
    paddingHorizontal: 4,
    textAlignVertical: 'top',
  },
  sendButton: {
    width: 40,
    height: 40,
    borderRadius: 20,
    justifyContent: 'center',
    alignItems: 'center',
    marginLeft: 8,
  },
  sendButtonActive: {
    backgroundColor: '#127a7f',
  },
  sendButtonInactive: {
    backgroundColor: '#E5E7EB',
  },
  loadingContainer: {
    paddingVertical: 12,
    alignItems: 'center',
  },
  visualizationWrapper: {
    marginVertical: 8,
    marginHorizontal: 16,
  },
  gridWrapper: {
    marginVertical: 8,
    marginHorizontal: 16,
  },
  menuContainer: {
    marginVertical: 8,
    padding: 16,
    borderRadius: 16,
    backgroundColor: '#ffffff',
    shadowColor: '#000',
    shadowOpacity: 0.08,
    shadowRadius: 8,
    shadowOffset: { width: 0, height: 2 },
    elevation: 2,
  },
  menuTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: '#0f172a',
    marginBottom: 8,
  },
  menuDescription: {
    marginBottom: 12,
  },
  menuDescriptionText: {
    color: '#475569',
    lineHeight: 20,
  },
  menuOptionsWrapper: {
    marginTop: 8,
  },
  menuOptionRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingVertical: 12,
    paddingHorizontal: 16,
    borderRadius: 12,
    backgroundColor: '#e0f2fe',
    borderWidth: 1,
    borderColor: '#bae6fd',
  },
  menuOptionRowSpacing: {
    marginTop: 8,
  },
  menuOptionLabel: {
    fontSize: 16,
    color: '#0f172a',
  },
  menuOptionBadge: {
    fontSize: 14,
    fontWeight: '600',
    color: '#0369a1',
  },
  menuHint: {
    marginTop: 12,
    fontSize: 14,
    color: '#475569',
  },
  promptContainer: {
    marginVertical: 8,
    padding: 16,
    backgroundColor: '#fff7ed',
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#fed7aa',
  },
  promptTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: '#9a3412',
    marginBottom: 6,
  },
  promptText: {
    color: '#7c2d12',
    lineHeight: 20,
  },
});


