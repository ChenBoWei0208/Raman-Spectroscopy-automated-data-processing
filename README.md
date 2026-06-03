## Description
This is an automated Raman spectra data processing tool built with Python >=3.8 and PySide6 (Qt). 

### Key Features (Underconstruction):
* **Spectra Drawing & Mapping:** Visualize Raman spectra and generate spatial intensity maps.
* **Data Analysis:** Perform intensity calculations and baseline corrections.
* **Machine Learning:** Integrated unsupervised learning tools such as Principal Component Analysis (PCA) for spectra classification.

## 🚀 Quick Start (How to Run)
   
Follow these steps to get the project up and running on your local machine:

### 1. Download the Project
Click the green **Code** button at the top right, then select **Download ZIP** and extract it. 
Alternatively, you can clone this repository using Git:

```bash
git clone https://github.com/ChenBoWei0208/Raman-Spectroscopy-automated-data-processing.git
cd Raman-Spectroscopy-automated-data-processing
```
### 2. Install Dependencies
Open your Terminal or Command Prompt (CMD), navigate to the project directory, and run the following command to install all required packages:

Correct Path:
└── Raman-Spectroscopy-automated-data-processing-main/  <-- You should be here!
    ├── widget.py
    ├── ui_form.py
    └── requirements.txt

Then install:
```bash
pip install -r requirements.txt
```
If your terminal says No such file or directory: 'requirements.txt', it means you are stuck in the outer wrapper folder. Simply run:
```Bash
cd Raman-Spectroscopy-automated-data-processing-main
```
### 3. Run the Application
Once the installation is complete, run the main file widget.py to launch the GUI window:
```bash
python widget.py
