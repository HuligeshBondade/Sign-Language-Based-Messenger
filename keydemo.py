import tkinter as tk

# Function to handle key press events
def on_key_press(event):
    # Get the key that was pressed
    key = event.keysym

    # Display the pressed key in the console
    print("Key pressed:", key)

    # Add your custom logic here based on the pressed key
    # For example, you can perform different actions based on different keys

# Create the main application window
root = tk.Tk()
root.title("Key Press Events")

# Bind the key press event to the function
root.bind("<Key>", on_key_press)

# Run the Tkinter event loop
root.mainloop()
