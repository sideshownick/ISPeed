# ISPeed

## Installation instructions

1. Install the speed test tool from http://startrinity.com/InternetQuality/ContinuousBandwidthTester.aspx#cli
  * there are different downlods for different platforms
2. Set up a google sheets project and allow API access using API access and a Service account https://docs.gspread.org/en/latest/oauth2.html
3. Install gsheets and run the attached script

### 1. Install the speed test tool 

```bash
mkdir startrinity_cst
cd startrinity_cst
wget http://startrinity.com/InternetQuality/startrinity_cst_linux_arm.tar.gz
tar xzvf startrinity_cst_linux_arm.tar.gz
./CST.CrossPlatform --download-limit 100 --upload-limit 10 --output-measurements
```

* **Note:** you may get memory errors with too high limits on r-pi (>150)

### 2. Set up google sheets

1. Follow the instructions here: https://docs.gspread.org/en/latest/oauth2.html to:
    1. set up a project 
        * Go to https://console.developers.google.com/project and create a new project (or select the one you already have).
    2. allow API access
        1. In the box labeled “Search for APIs and Services”, search for “Google Drive API” and enable it.
        2. In the box labeled “Search for APIs and Services”, search for “Google Sheets API” and enable it.
    3. add a service account
        1. Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
        2. Fill out the form
        3. Click “Create” and “Done”.
        4. Press “Manage service accounts” above Service Accounts.
        5. Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.
        6. Select JSON key type and press “Create”.
        7. You will automatically download a JSON file with credentials. It may look like this:
```json
{
    "type": "service_account",
    "project_id": "api-project-XXX",
    "private_key_id": "2cd … ba4",
    "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
    "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
    "client_id": "473 … hd.apps.googleusercontent.com",
    ...
}
```
* make a note of the value for the `"client_email"` key
2. Set up a new google sheet and give it a name such as `Logging`
* delete all rows except the header row: `datetime` `speed/Mbps`
3. Grant access to the sheet to the email address in the `<some_long_name>.json` file downloaded in step 1
4. move the `WHATEVER.json` file to the pi and and rename it to `.config/gspread/service_account.json` in the home directory

### 3. Install gsheets and run the attached script

```bash
pip install gspread
wget https://github.bath.ac.uk/nm268/ISPeed/blob/master/speedtest.py
python speeddata.py
```

Edit crontab to automatically run the script at regular intervals:
```bash
crontab -e
```
Add the line:   
```59 * * * * python speedtest.py```    
(CTRL-X saves the file)
* in this example it runs on the 59th minute of every hour then saves the as the average reading over the last half of that minute.
