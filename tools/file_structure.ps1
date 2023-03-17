# Create project directory
New-Item -ItemType Directory -Force -Path .\FlaskApp

# Navigate into project directory
cd .\FlaskApp

# Create subdirectories
New-Item -ItemType Directory -Force -Path .\Model
New-Item -ItemType Directory -Force -Path .\Controller
New-Item -ItemType Directory -Force -Path .\Templates

# Create app.py file in root directory
New-Item app.py

# Add preliminary files to subdirectories (example)
Out-File Model\model.txt
Out-File Controller\controller.txt