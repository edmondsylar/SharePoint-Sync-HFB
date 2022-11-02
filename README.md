# SharePoint-Sync-HFB  
This is a basic a API to aid in synching directories from any location ot any location  
## Main Use case  
We need to move files froma local sharepoint directory to a Cloud sharepoint directory  

# HowTo
The homepage located at route "/" has a form with 2 fields as named below.  
1. Parent Directory - This is the directory frrom which we need to pick our files.  
2. Child Directory - This the folder to which we are copying the files  

# How to install!
The script is based on python 3.10.8, be sure to have this installed first before running this project.  

1. run ```git clone https://github.com/edmondsylar/SharePoint-Sync-HFB.git``` from the directory where you want to store your project.

2. The file named requirements holds all the required libraries to install in-order to make the API run fluidly

2.5 (Optional step)
### Create a virtualen to run our proect from  
``` 
    1. python -m virtualenv env - Create Virtualenv
    Activate virtualenv
    2. source env\Scripts\activate | linux and Git bash users
    2.5 env\Scripts\activate.bat | Windows Users (CMD).
```

3. From the same directory, run ```pip install -r requirements.txt```. this will install all the requirements listed in the requirements file.  

After the installation is complete, we are not ready to run the project on our new environment.

## Running the App.

