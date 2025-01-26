rem pytest -s -v -n auto TestCases/Reg_uer_Test_.py --browser =Firefox
rem pytest -s -v -n auto TestCases/Reg_uer_Test_.py --browser =Chrome
rem pytest -s -v -n 1 --html=Reports/report.html TestCases/User_login_test_.py --browser=Chrome
rem pytest -s -v -n 1 --html=Reports/report.html TestCases/User_login_test_.py --browser=Firefox

rem pytest -s -v -m sanity --html=Reports/report.html TestCases/ --browser=Chrome
rem pytest -s -v -m sanity --html=Reports/report.html TestCases/Reg_uer_Test_.py --browser=Chrome
rem pytest -s -v -m sanity and regration --html=Reports/report.html TestCases/ --browser=Chrome
pytest -s -v -m sanity --html=Reports/report.html TestCases/Reg_uer_Test_.py
rem pytest -s -v -m sanity or regration --html=Reports/report.html TestCases/ --browser=Chrome
rem pytest -s -v -m sanity or regration --html=Reports/report.html TestCases/Reg_uer_Test_.py --browser=Chrome


rem pytest -s -v -m sanity --html=Reports/report.html TestCases/ --browser=Firefox
rem pytest -s -v -m sanity --html=Reports/report.html TestCases/Reg_uer_Test_.py --browser=Firefox
rem pytest -s -v -m sanity and regration --html=Reports/report.html TestCases/ --browser=Firefox
rem pytest -s -v -m sanity and regration --html=Reports/report.html TestCases/Reg_uer_Test_.py --browser=Firefox
rem pytest -s -v -m sanity or regration --html=Reports/report.html TestCases/ --browser=Chrome
rem pytest -s -v -m sanity or regration --html=Reports/report.html TestCases/Reg_uer_Test_.py --browser=Firefox