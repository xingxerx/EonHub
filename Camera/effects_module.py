import numpy as np
import random
import cv2

def apply_random_transformation(frame):
    """Applies a random transformation to the frame (e.g., shift, rotation)."""
    rows, cols, _ = frame.shape
    # Example: Random shift
    shift_x = random.randint(-20, 20)
    shift_y = random.randint(-20, 20)
    M = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
    shifted_frame = cv2.warpAffine(frame, M, (cols, rows))
    return shifted_frame

def superposition_effect(frame, num_layers=2, alpha=0.5):
    """
    Simulates a superposition effect by blending multiple copies of the frame.
    """
    layers = []
    for _ in range(num_layers):
        # Apply a random transformation to each layer (e.g., slight shift, rotation)
        transformed_frame = apply_random_transformation(frame)
        layers.append(transformed_frame)

    # Blend the layers together
    blended_frame = np.zeros_like(frame, dtype=np.float32)
    for layer in layers:
        blended_frame += layer * alpha
    blended_frame = np.clip(blended_frame, 0, 255).astype(np.uint8)
    return blended_frame
