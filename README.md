# test_login

### Requirements on MacOS
1. virtualenv 
   (if you don't have it in your mac, you can use homebrew to install)
2. chromedriver (same as virtualenv)

### Before Starting the test, you need to run commands below by sequence :
1. to activate the virtual environments

```shell
source venv/bin/activate
```
2. install packages in the requirements
```shell
pip install -r requirements.txt
```
3. add env.py under the test directory, edit the content based on the env.py.example

### Notes
1. Where to find chrome profile path
   - type **chrome://version/** in chrome search bar
2. Make sure to turn off the 2FA authentication for your google account
