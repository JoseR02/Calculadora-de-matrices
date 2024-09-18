# Calculadora de matrices or Matrix calculetor

### Matrix Operations:

- Addition: Computes the sum of two matrices.

- Multiplication: Computes the product of two matrices.

- Transpose: Computes the transpose of the first matrix.

- Reduction: Checks if the first matrix is in reduced row echelon form.

### Matrix Input:

Users can specify the dimensions of two matrices and then input their elements through dynamically generated entry fields.
Help and Information:

Detailed help dialogs are available for each matrix operation, explaining the rules and procedures involved.
An instructional guide on how to use the application is provided.
Credits:

Displays information about the developers and references used for the application.
How to Use
Input Matrix Dimensions:

Enter the number of rows and columns for both matrices in the provided fields.
Click the "Ingresar matrices" button to open a new window where you can input the elements of the matrices.
Perform Matrix Operations:

After entering the matrices, use the buttons in the left frame to perform operations such as addition, multiplication, transpose, and reduction.
View Results:

Results are displayed in pop-up message boxes, providing the output of the selected operation.
Help and Credits:

Use the help buttons next to each operation to get detailed instructions.
Click the "Creditos" button to view developer information and references.
Code Overview

### Class App:

Inherits from ctk.CTk and tk.Tk.
Initializes the application window and sets up the interface.
Defines methods for creating the GUI frames and buttons.
Frame Creation (create_frame and create_frame2 Methods):

create_frame: Sets up the main menu frame with buttons for matrix operations and other functionalities.
create_frame2: Sets up the frame for matrix dimension inputs and buttons for actions like matrix entry and operation explanations.
Matrix Operations Methods:

boton_suma, boton_producto, boton_transpuesta, boton_reduccion: Perform respective matrix operations and display results.
boton_help_suma, boton_help_producto, boton_help_transpuesta, boton_help_reduccion: Show help dialogs with rules for the respective operations.
Matrix Input and Display Methods:

ingresar_matriz: Opens a new window for entering matrix elements based on specified dimensions.
mostrar_matrices: Displays the currently stored matrices.
Utility Methods:

boton_salida: Confirms and exits the application.
ayuda_funciona: Provides instructions on how to use the application.
creditos_usuarios: Displays credits and references.

# Installation and Requirements

### Ensure you have the following packages installed:

- tkinter
- customtkinter
- numpy
### You can install the necessary packages using pip.
