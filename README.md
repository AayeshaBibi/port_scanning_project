# Open Port Scanner with GUI

## 📌 What This Project Does
Scans the open TCP ports of any IP address using a simple Python GUI.

## 🧪 How to Run This Project on Jupyter Notebook with Anaconda

### Step 1: Install Anaconda
Download from https://www.anaconda.com/products/distribution

### Step 2: Create Environment (Optional)
conda create -n portscanner python=3.10 -y
conda activate portscanner

### Step 3: Launch Jupyter Notebook
jupyter notebook

### Step 4: In Jupyter Notebook, run:
!python port_scanner_gui.py

## Alternate: Run directly using Anaconda Prompt
cd path\to\open_port_scanner_project
python port_scanner_gui.py

## 📄 Output
- Results shown in GUI
- Saved in 'scan_report.txt'

## Requirements
- tk
- socket
