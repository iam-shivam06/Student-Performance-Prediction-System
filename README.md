# 🎓 Student Performance Prediction System

## 📌 Overview

**Student Performance Prediction System** is a Machine Learning-based web application that estimates a student's final exam score using important academic and lifestyle factors.

The application uses a Random Forest Regression algorithm to analyze student information and predict an estimated exam score out of 100.

Built using Python, Scikit-learn, and Streamlit, it provides an interactive interface where users can enter student details and instantly view prediction results.

## ✨ Features

- 🎓 Predict estimated student exam scores
- 📚 Analyze daily study hours
- 📊 Consider student attendance percentage
- 📝 Evaluate previous exam performance
- 📋 Include assignment scores
- 😴 Consider daily sleep hours
- 🤖 Random Forest Regression model
- 📈 Visualize predicted exam scores
- 🎯 Categorize predicted performance:
  - Excellent
  - Good
  - Average
  - Needs Improvement
- 🖥️ Interactive Streamlit dashboard

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Algorithm | Random Forest Regression |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| Model Storage | Joblib |
| Frontend / Web Framework | Streamlit |

## 📂 Project Structure

```text
Student-Performance-Prediction/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── run_project.bat
│
├── dataset/
│   └── student_data.csv (generated during training)
│
└── model/
    └── student_model.pkl (generated during training)
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Student-Performance-Prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd Student-Performance-Prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Train the Machine Learning Model

```bash
python train_model.py
```

This step automatically:

- Generates a synthetic student dataset.
- Splits data into training and testing sets.
- Trains a Random Forest Regression model.
- Evaluates the model using MAE and R² Score.
- Saves the trained model as `student_model.pkl`.

### 7. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## 🧠 Machine Learning Workflow

1. Generate synthetic student performance data.
2. Select relevant academic and lifestyle features.
3. Split the dataset into training and testing sets.
4. Train a Random Forest Regression model.
5. Evaluate predictions using MAE and R² Score.
6. Save the trained model using Joblib.
7. Load the model into the Streamlit application.
8. Generate estimated exam scores from user inputs.

## 📊 Input Features

| Feature | Description |
|---|---|
| Study Hours | Daily study hours |
| Attendance | Attendance percentage |
| Previous Score | Previous exam score |
| Assignment Score | Assignment performance |
| Sleep Hours | Daily sleep duration |

## 🎯 Performance Categories

| Predicted Score | Category |
|---|---|
| 75–100 | Excellent |
| 60–74.9 | Good |
| 40–59.9 | Average |
| Below 40 | Needs Improvement |

## 🔮 Future Improvements

- Train using real-world student datasets.
- Explore additional regression algorithms.
- Improve prediction accuracy and validation.
- Add interactive performance analytics.
- Include more student-related features.
- Deploy the application online.

## ⚠️ Disclaimer

This project uses synthetically generated data for educational and demonstration purposes.

The predictions are not scientifically validated for real academic decisions and should not be used to evaluate actual student performance.

## 👨‍💻 Author

**Shivam Sahani**

## 📄 License

This project is intended for educational and learning purposes.
