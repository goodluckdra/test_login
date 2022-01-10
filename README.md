# test_login

### Requirements on MacOS
1. virtualenv 
   (if you don't have it in your mac, you can use homebrew to install)
2. chromedriver (same as virtualenv, install by brew)

### Before Starting the test, you need to run commands below by sequence :
1. To create and activate the virtual environments at the root (```test_login/```)
```shell
virtualenv venv
```
```shell
source venv/bin/activate
```
2. Install packages in the requirements
```shell
pip install -r requirements.txt
```
3. Add ```env.py``` under the ```qaexam``` directory, edit the content based on the env.py.example
### Pytest to login imdb via Google account
- Go to the directory ```tests```
- Run the command below:
```shell
pytest test_imdb_login.py
```
- Screenshots is saved under ```tests/screenshots_pic/```. The file is named after the rule: timestamp + status

### Notes
1. Where to find chrome profile path
   - type **chrome://version/** in chrome search bar
2. Make sure to turn off the 2FA authentication for your google account

3. To execute the ```imdb_login.py```, you have to add the ```__init__.py``` under the root directory. And the screenshots is expected to saved at ```utils/screenshots/```
