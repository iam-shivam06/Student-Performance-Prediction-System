# Student Performance Prediction System

An educational Machine Learning project that estimates a student's exam score
from study hours, attendance, previous exam score, assignment score, and sleep hours.

## Technologies
- Python
- Pandas and NumPy
- Scikit-learn (Random Forest Regression)
- Streamlit
- Matplotlib
- Joblib

## Project structure
```text
Student-Performance-Prediction/
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── .gitignore
├── run_project.bat
├── dataset/
│   └── (student_data.csv is generated during training)
└── model/
    └── (student_model.pkl is generated during training)
```

## Run on Windows (VS Code)

1. Install Python 3.10 or newer and VS Code.
2. Extract this ZIP file.
3. Open the extracted `Student-Performance-Prediction` folder in VS Code.
4. Open Terminal > New Terminal.
5. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt and run:

   ```cmd
   venv\Scripts\activate.bat
   ```

6. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

7. Train the model and generate the sample dataset:

   ```bash
   python train_model.py
   ```

8. Start the web app:

   ```bash
   streamlit run app.py
   ```

The app should open in your browser. If it does not, open the local URL printed in the terminal.

## Quick start
On Windows, after Python is installed, you can double-click `run_project.bat`.
The first run installs dependencies, trains the model, and starts Streamlit.
An internet connection is needed for installing Python packages.

## GitHub upload
Create a new GitHub repository, then run these commands in the project folder:

```bash
git init
git add .
git commit -m "Initial project upload"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_REPOSITORY_URL` with the URL of your own GitHub repository.

## Important note
The project creates a synthetic dataset for demonstration and learning. Its predictions
are not validated for real academic decisions and should not be treated as actual exam results.
