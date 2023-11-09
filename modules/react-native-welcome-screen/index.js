import React from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

const WelcomeScreen = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to Task Planner App</Text>
      <Text style={styles.subtitle}>Organize your tasks and be more productive!</Text>
      <Button
        title="Get Started"
        onPress={() => navigation.navigate('Tasks')}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  subtitle: {
    fontSize: 16,
    marginBottom: 40,
  },
});


export default {
  title: "welcome-screen",
  navigator: WelcomeScreen
};