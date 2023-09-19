# End-to-End Property Price Predictor

Welcome to the End-to-End Property Price Predictor GitHub repository. This project is designed to provide a comprehensive property price prediction system for Bengaluru using real-world datasets. It encompasses data preprocessing, data cleaning, regression model building, and the creation of an interactive web interface for property price predictions.

## Repository Structure

The repository is organized into three main directories:

### 1. Model Directory

- **Dataset**: Contains the dataset used for training and testing the property price prediction model.
- **Jupyter Notebook**: This notebook comprises the entire codebase for data preprocessing, exploratory data analysis (EDA), and model training. The trained model is then exported for use in the backend server.

### 2. Server Directory

- **util.py**: This utility file contains functions necessary for data processing and predictions.
- **server.py**: The server script receives HTTP GET requests from the website, processes them using the trained machine learning model, and sends the model's prediction back to the webpage.

### 3. Web Server Directory

- **HTML, CSS, and JavaScript Files**: These files collectively form the frontend of the webpage. They create the user interface (UI) where users can input property details and receive predicted property prices as output.

## Dependencies

To run this project successfully, you'll need the following dependencies:

- **Python**: Version 3.11.4
- **Conda**: Version 23.7.4
- **NumPy**: Version 1.25.1
- **Pandas**: Version 2.0.3
- **Matplotlib**: Version 3.7.2
- **Scikit-Learn**: Version 1.3.0
- **Seaborn**: Version 0.12.2

## Usage

1. Start by exploring the Jupyter Notebook in the "Model" directory for a detailed walkthrough of data preprocessing, EDA, and model training.

2. Move to the "Server" directory and run `server.py` to start the backend server, which will listen for incoming HTTP GET requests and provide predictions.

3. In the "Web Server" directory, open the HTML file to access the interactive web interface. Input property details and receive property price predictions from the trained model.

## Contribution

Contributions to this project are welcome! Feel free to fork the repository, make improvements, and submit pull requests. If you have ideas for enhancements or new features, please open an issue to discuss them.

Enjoy exploring and using the End-to-End Property Price Predictor!
