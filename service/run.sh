killall test_service*
python3 -u neotestservice.py -p 23606 -n "testservice_23606"> `date +%F_%H_%M_%S_23606`.log 2>&1 &
python3 -u neotestservice.py -p 23616 -n "testservice_23616"> `date +%F_%H_%M_%S_23616`.log 2>&1 &
python3 -u neotestservice.py -p 23626 -n "testservice_23626"> `date +%F_%H_%M_%S_23626`.log 2>&1 &
python3 -u neotestservice.py -p 23636 -n "testservice_23636"> `date +%F_%H_%M_%S_23636`.log 2>&1 &
