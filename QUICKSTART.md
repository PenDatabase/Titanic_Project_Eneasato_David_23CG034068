# ============================================================================
# TITANIC SURVIVAL PREDICTION SYSTEM - QUICK START GUIDE
# ============================================================================

## 📋 PREREQUISITES

Before you begin, ensure you have:
- ✅ Python 3.8 or higher installed
- ✅ pip package manager
- ✅ Internet connection (for downloading dependencies)
- ✅ Text editor or IDE (VS Code, PyCharm, etc.)
- ✅ Git (optional, for version control)

## 🚀 STEP-BY-STEP SETUP INSTRUCTIONS

### STEP 1: Download the Titanic Dataset
1. Visit: https://www.kaggle.com/c/titanic/data
2. Download the file: `train.csv`
3. Place `train.csv` in the project root directory (same folder as app.py)

### STEP 2: Install Python Dependencies

Open a terminal/command prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

If you encounter any issues, try:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### STEP 3: Train the Machine Learning Model

1. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Navigate to: `model/model_building.ipynb`

3. Run all cells in the notebook:
   - Click "Cell" → "Run All"
   - Wait for all cells to execute (this may take 2-3 minutes)

4. Verify that `titanic_survival_model.pkl` has been created in the `model/` folder

### STEP 4: Run the Web Application

In your terminal, run:

```bash
python app.py
```

You should see output like:
```
======================================================================
TITANIC SURVIVAL PREDICTION SYSTEM
======================================================================
Initializing application...
✓ Model loaded successfully
  - Features: ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']
  - Test Accuracy: 0.8324
  - ROC-AUC Score: 0.8721

✓ Application ready!
======================================================================

Starting Flask server...
Access the application at: http://127.0.0.1:5000
Press CTRL+C to quit
```

### STEP 5: Access the Application

1. Open your web browser
2. Go to: http://localhost:5000 or http://127.0.0.1:5000
3. You should see the Titanic Survival Prediction interface

## 🧪 TESTING THE APPLICATION

Try these test cases:

### Test Case 1: High Survival Probability
- Passenger Class: 1st Class
- Sex: Female
- Age: 25
- Fare: £100
- Embarked: Cherbourg (C)
- **Expected Result:** Survived (high probability)

### Test Case 2: Low Survival Probability
- Passenger Class: 3rd Class
- Sex: Male
- Age: 60
- Fare: £8
- Embarked: Southampton (S)
- **Expected Result:** Did Not Survive (high probability)

### Test Case 3: Medium Probability
- Passenger Class: 2nd Class
- Sex: Female
- Age: 35
- Fare: £30
- Embarked: Queenstown (Q)
- **Expected Result:** Survived (medium-high probability)

## 🐛 TROUBLESHOOTING

### Problem: "Model file not found"
**Solution:**
- Ensure you've run the `model_building.ipynb` notebook completely
- Check that `titanic_survival_model.pkl` exists in the `model/` folder
- Verify the file path is correct

### Problem: "Module not found" or Import errors
**Solution:**
```bash
pip install --upgrade -r requirements.txt
```

### Problem: "train.csv not found"
**Solution:**
- Download `train.csv` from Kaggle
- Place it in the project root directory (not in a subfolder)

### Problem: "Port 5000 already in use"
**Solution:**
- Kill the process using port 5000, OR
- Change the port in `app.py` (line with `app.run(port=5000)`)

### Problem: Python version issues
**Solution:**
- Ensure Python 3.8 or higher is installed
- Check version: `python --version`
- If needed, download from: https://www.python.org/downloads/

## 📦 PROJECT STRUCTURE VERIFICATION

Ensure your project has this structure:

```
Your_Project_Folder/
├── app.py                          ✓ Main Flask application
├── requirements.txt                ✓ Dependencies
├── train.csv                       ✓ Dataset (download from Kaggle)
├── README.md                       ✓ Documentation
├── Procfile                        ✓ Deployment config
├── runtime.txt                     ✓ Python version
├── .gitignore                      ✓ Git ignore rules
├── Titanic_hosted_webGUI_link.txt  ✓ Deployment info
│
├── model/
│   ├── model_building.ipynb        ✓ Training notebook
│   └── titanic_survival_model.pkl  ✓ Trained model (after running notebook)
│
├── static/
│   └── style.css                   ✓ Styling
│
├── templates/
│   └── index.html                  ✓ Web interface
│
└── tests/
    └── test_app.py                 ✓ Unit tests
```

## 🌐 DEPLOYMENT TO PRODUCTION

### Option 1: Render.com (Recommended - Free Tier Available)

1. Create account at https://render.com
2. Connect your GitHub repository
3. Create new "Web Service"
4. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click "Create Web Service"
6. Wait for deployment (5-10 minutes)
7. Access your live URL!

### Option 2: PythonAnywhere.com (Free Tier Available)

1. Create account at https://www.pythonanywhere.com
2. Go to "Files" tab and upload all project files
3. Go to "Web" tab and create new web app
4. Choose "Manual configuration" and Python 3.x
5. Edit WSGI configuration file:
   ```python
   import sys
   path = '/home/yourusername/your-project-folder'
   if path not in sys.path:
       sys.path.append(path)
   from app import app as application
   ```
6. Reload web app
7. Access at: https://yourusername.pythonanywhere.com

### Option 3: Streamlit Cloud (If converting to Streamlit)

1. Create account at https://streamlit.io/cloud
2. Connect GitHub repository
3. Deploy directly from GitHub
4. Access your live URL

## 📝 BEFORE SUBMISSION CHECKLIST

- ☐ Model has been trained (titanic_survival_model.pkl exists)
- ☐ Application runs locally without errors
- ☐ All test cases work correctly
- ☐ Tested on different input combinations
- ☐ GitHub repository created and code pushed
- ☐ Application deployed to hosting platform
- ☐ Live URL is accessible and working
- ☐ Updated `Titanic_hosted_webGUI_link.txt` with:
  - Your name
  - Matric number
  - Algorithm used
  - Model persistence method
  - Live URL
  - GitHub repository link
- ☐ All required files follow the project structure
- ☐ README.md updated with your information

## 🎓 SUBMISSION INFORMATION

**Course:** COS331 - Artificial Intelligence
**Institution:** Covenant University
**Session:** 2025/2026
**Deadline:** Friday, February 5, 2026, 11:59 PM
**Platform:** Scorac.com

## 📞 SUPPORT

If you encounter any issues:
1. Check the troubleshooting section above
2. Review error messages carefully
3. Search for similar issues online
4. Contact your course instructor
5. Ask classmates for help

## 🎉 CONGRATULATIONS!

Once everything is working:
- ✅ Your model is trained and accurate
- ✅ Your web application is running
- ✅ You can make predictions
- ✅ Your project is deployed online
- ✅ You're ready to submit!

## 📚 ADDITIONAL RESOURCES

- **Kaggle Titanic Competition:** https://www.kaggle.com/c/titanic
- **Flask Documentation:** https://flask.palletsprojects.com/
- **scikit-learn Documentation:** https://scikit-learn.org/stable/
- **Random Forest Classifier:** https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
- **Render Deployment Guide:** https://render.com/docs
- **PythonAnywhere Tutorial:** https://help.pythonanywhere.com/

## 💡 TIPS FOR SUCCESS

1. **Start Early:** Don't wait until the deadline
2. **Test Thoroughly:** Try various input combinations
3. **Document Issues:** Keep track of any problems you encounter
4. **Backup Your Work:** Use Git for version control
5. **Deploy Early:** Test your deployment well before submission
6. **Read Error Messages:** They often tell you exactly what's wrong
7. **Ask Questions:** Don't hesitate to seek help when needed

---

**Good luck with your project! 🚢🎓**

---

*For questions or issues, contact your course instructor or check the README.md file.*
