# Quotation Calculator App

## Overview

The **Quotation Calculator App** is a Python-based desktop application designed to simplify and streamline the process of generating accurate quotations. This app allows users to input required details, calculate costs based on predefined parameters, and generate professional, ready-to-use quotations efficiently. It is built using the **PyQt** and **PySide** frameworks, ensuring a user-friendly graphical interface.

---

## Features

- **User-Friendly Interface**: Built with PyQt/PySide to provide an intuitive GUI for seamless navigation.
- **Dynamic Input Fields**: Allows users to enter custom data, such as product/service names, quantities, unit prices, and discounts.
- **Real-Time Calculations**: Automatically calculates total costs, including tax and discount adjustments.
- **Customizable Settings**: Configure tax rates, discounts, and currency formats to suit specific needs.
- **Quotation Export**: Generate and save quotations in printable formats like PDF or Excel.
- **Data Validation**: Ensures accurate input of numerical and text fields to minimize errors.

---

## Technologies Used

- **Python**: Core programming language used for the app's functionality.
- **PyQt / PySide**: Frameworks used to develop the graphical user interface.
- **NumPy**: For performing advanced mathematical calculations.
- **Fpdf2 or ReportLab**: To generate PDF files for the quotations.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- Required Python libraries:
  ```bash
  pip install PyQt5 numpy fpdf2
  ```

### Steps to Run the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/michaeldapaah/quotation-calculator.git
   cd quotation-calculator
   ```
2. Install dependencies using pip.
3. Run the main Python file:
   ```bash
   python app.py
   ```
4. The app window will open, allowing you to start generating quotations.

---

## Usage

1. Launch the application.
2. Fill in the required details in the input fields (e.g., item name, quantity, unit price).
3. Adjust the tax rate and discount if necessary.
4. Click the **"Calculate"** button to generate the total quotation.
5. Use the **"Export"** option to save the quotation as a PDF or other formats.

---

## Screenshots

_(Include images of the app interface to provide a visual guide for users.)_

---

## Future Enhancements

- **Database Integration**: Save and retrieve client and quotation data for future use.
- **Cloud Sync**: Enable users to access their quotations across devices.
- **Multi-Currency Support**: Automatically convert currencies based on real-time exchange rates.
- **Theming**: Add light and dark modes for better usability.

---

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to the branch.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

Developed by **Michael Teye Yaw Dapaah**

- **Email**: michaeldapaah0@gmail.com
- **GitHub**: [michaeldapaah](https://github.com/michaeldapaah)
