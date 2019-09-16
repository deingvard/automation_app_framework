**Run commands in terminal IDE**
1. python3 -m venv env
2. source env/bin/activate
3. pip install -r requirements.txt
4. cd test
5. pytest test/test_login.py --alluredir=allure-results

**Test Results**

- Test results will be collected into the following folders:
target/allure-results/xxxxx-xxxxx-test.xml file will contain information about test steps (Allure)
