# SharePoint-Sync-web-tool
This is a basic a API to aid in synching directories from any location ot any location  
## Main Use case  
We need to move files froma local sharepoint directory to a Cloud sharepoint directory

# How to install!
The script is based on python 3.10.8, be sure to have this installed first before running this project.  

1. run ```git clone https://github.com/edmondsylar/SharePoint-Sync-HFB.git``` from the directory where you want to store your project.

2. The file named requirements holds all the required libraries to install in-order to make the API run fluidly

2.5 (Optional step)
### Create a virtualen to run our proect from  
``` 
    1. python -m virtualenv env - Create Virtualenv
    Activate virtualenv
    2. source env/Scripts/activate | linux and Git bash users
    2.5 env\Scripts\activate.bat | Windows Users (CMD).
```

3. From the same directory, run ```pip install -r requirements.txt```. this will install all the requirements listed in the requirements file.  

After the installation is complete, we are not ready to run the project on our new environment.

## Running the App.
Run ```python app.py ``` from the app's root directory.  
if command runs successfully, you should see something like below in our terminal.

```
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5100
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 542-934-434
```
Finally, accedd your app from either localhost:5100 or http://127.0.0.1:5100.  
From the homepage, you should see a form with 2 fields as named below.
1. Parent Directory - This is the directory frrom which we need to pick our files.
2. Child Directory - This the folder to which we are copying the files

## How to use the app
1. Enter the Parent Directory and Child Directory in the form fields.
2. Click on the Start Sync button.
3. Wait for the process to complete and a message returned to you Sychronization Complete.
4. Check the Child Directory to see if the files have been copied.

## How to run tests
1. Run ```pytest``` from the root directory of the project.
2. If all tests pass, you should see something like below in your terminal.
```
============================= test session starts ==============================
platform win32 -- Python 3.10.0, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\edmon\Documents\GitHub\SharePoint-Sync-HFB
collected 1 item

tests\test_app.py .                                                      [100%]

============================== 1 passed in 0.02s ===============================
```

## Contributing
Contributions, issues and feature requests are welcome!

Feel free to check the issues page.

## Show your support
Give a ⭐️ if you like this project!

## Acknowledgments
- Hat tip to anyone whose code was used
- Inspiration
- etc

## 📝 License
This project is [MIT](https://opensource.org/licenses/MIT) licensed.
