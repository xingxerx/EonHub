import tensorflow as tf

# Define a simple model (replace with your actual model)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(3,)),  # Example input shape
    tf.keras.layers.Dense(1)  # Example output
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Save the model in .keras format
model.save('emotional_resonance.keras')

print("Model saved to emotional_resonance.keras")
