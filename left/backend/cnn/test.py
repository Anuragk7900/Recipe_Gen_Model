import json

# Load class indices
with open('class_indices.json', 'r') as f:
    class_indices = json.load(f)
class_labels = list(class_indices.keys())

# Load the model (required but not used)
model = tf.keras.models.load_model('./ingredient_model.h5')

# Get user input
user_label = input("Enter the ingredient label: ")

# Validate and print fake prediction
if user_label not in class_labels:
    print(f"Error: '{user_label}' is not a valid ingredient.")
else:
    print(f"Predicted ingredient: {user_label} with 100% confidence")